import asyncio
import aiohttp
import logging
import time
from aiohttp_socks import ProxyConnector, ProxyType
import socket

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('proxy_check.log'),
        logging.StreamHandler()
    ]
)

def is_valid_socks5_format(proxy_info):
    """Basic format check for proxy (ip:port)"""
    try:
        ip, port = proxy_info.split(':')
        port = int(port)
        # Simple IP format check
        socket.inet_aton(ip)
        return 0 <= port <= 65535
    except (ValueError, socket.error):
        return False

async def check_proxy(proxy_info, semaphore, valid_proxies):
    """Check if a proxy is working and supports SOCKS5"""
    async with semaphore:
        # Skip if not in valid format
        if not is_valid_socks5_format(proxy_info):
            logging.warning(f"Proxy {proxy_info} - SKIPPED: Invalid format")
            return

        proxy_url = f"socks5://{proxy_info}"
        connector = ProxyConnector(
            proxy_type=ProxyType.SOCKS5,
            host=proxy_info.split(':')[0],
            port=int(proxy_info.split(':')[1]),
            verify_ssl=False
        )
        
        try:
            async with aiohttp.ClientSession(connector=connector) as session:
                # First test if it supports SOCKS5 by making a simple request
                async with session.get('http://google.com', timeout=aiohttp.ClientTimeout(total=5)) as response:
                    if response.status == 200:
                        valid_proxies.append(proxy_info)
                        logging.info(f"Proxy {proxy_info} - SUCCESS: SOCKS5 confirmed")
                    else:
                        logging.warning(f"Proxy {proxy_info} - FAILED: Status {response.status}")
        except Exception as e:
            logging.warning(f"Proxy {proxy_info} - FAILED: Not SOCKS5 or unreachable - {str(e)}")

async def main():
    # Read proxies from file
    try:
        with open('proxy.txt', 'r') as f:
            proxies = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        logging.error("proxy.txt not found!")
        return
    
    proxy_count = len(proxies)
    logging.info(f"Found {proxy_count} proxies to check")
    
    # Use a semaphore to limit concurrent connections
    semaphore = asyncio.Semaphore(200)
    valid_proxies = []
    
    # Create tasks for all proxies
    tasks = [
        check_proxy(proxy, semaphore, valid_proxies)
        for proxy in proxies
    ]
    
    # Run all tasks concurrently
    await asyncio.gather(*tasks)
    
    # Save only working SOCKS5 proxies
    with open('checked.txt', 'w') as f:
        for proxy in valid_proxies:
            f.write(f"{proxy}\n")
    
    logging.info(f"Found {len(valid_proxies)} working SOCKS5 proxies out of {proxy_count}")
    logging.info("Results saved to checked.txt")

if __name__ == "__main__":
    # Required packages: pip install aiohttp aiohttp-socks
    try:
        import aiohttp
        import aiohttp_socks
    except ImportError:
        logging.error("Please install required packages: pip install aiohttp aiohttp-socks")
        exit(1)
    
    start_time = time.time()
    
    # Run the async main function
    asyncio.run(main())
    
    execution_time = time.time() - start_time
    logging.info(f"Completed in {execution_time:.2f} seconds")
