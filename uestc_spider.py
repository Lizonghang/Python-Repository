# -*- coding=utf-8 -*-
import urllib
import urllib2
import re
import cookielib
import httplib
import sys
import socket


class UESTCSpider:
    def __init__(self):
        self.exist_urls = []
        self.list_urls = ['http://www.uestc.edu.cn/', 'http://portal.uestc.edu.cn/index.portal']
        self.getAuthorization_url = \
            'https://uis.uestc.edu.cn/amserver/UI/Login?goto=http%3A%2F%2Fportal.uestc.edu.cn%2Flogin.portal'
        self.postdata = urllib.urlencode({
                                            'IDToken0': '',
                                            'IDToken1': '2014010912008',
                                            'IDToken2': '199014',
                                            'IDButton': 'Submit',
                                            'goto': 'aHR0cDovL3BvcnRhbC51ZXN0Yy5lZHUuY24vbG9naW4ucG9ydGFs',
                                            'encoded': 'true',
                                            'gx_charset': 'UTF-8'
        })
        self.headers = {
                          'User-Agent': '''Mozilla/5.0 (Windows NT 6.3; WOW64)
                            AppleWebKit/537.36 (KHTML, like Gecko)
                            Chrome/42.0.2311.152 Safari/537.36 LBBROWSER'''
        }

        urllib2.socket.setdefaulttimeout(10)
        self.title_count = 0
        reload(sys)
        sys.setdefaultencoding('utf-8')

    def spider(self):
        self.get_authorization()
        url_index = 0
        while url_index < len(self.list_urls):
            current_url = self.list_urls[url_index]
            if current_url in self.exist_urls:
                print u'已访问过，跳过'
                continue
            print u'正在请求URL: %s' % current_url
            try:
                req = urllib2.Request(current_url, headers=self.headers)
                myPage = urllib2.urlopen(req)
            except urllib2.URLError:
                print u'爬虫报告:服务器崩溃'
                continue
            except urllib2.HTTPError:
                print u'爬虫报告:服务器崩溃'
                continue
            except socket.timeout, err:
                print u'爬虫报告:连接超时,跳过'
                continue
            except httplib.BadStatusLine, err:
                print u'爬虫报告:服务器状态异常'
                continue
            finally:
                url_index = url_index + 1
            self.save_page(myPage)
            self.exist_urls.append(current_url)
        print u'爬虫进程结束,保存所有链接'
        self.save_link(self.exist_urls)
        print u'本次搜索的URL总计%s个' % len(self.exist_urls)
        print u'程序正常结束,欢迎使用UESTC网站爬虫'

    def get_authorization(self):
        cookie_jar = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie_jar))
        urllib2.install_opener(opener)
        req = urllib2.Request(self.getAuthorization_url, data=self.postdata, headers=self.headers)
        info = urllib2.urlopen(req)
        with open('Authorization.html', 'wb') as f:
            f.write(info.read())
        print u'获取登陆权限成功,COOKIE信息: %s' % cookie_jar

    def save_page(self, myPage):
        page_message = myPage.read()
        title = self.find_title(page_message)
        print u'保存文件:%s' % title + '.html'
        with open('./save_data/' + title + '.html', 'wb') as f:
            f.write(page_message)
        self.find_link(page_message)

    def find_title(self, page_message):
        myMatch = re.search(r'<title>(.*?)</title>', page_message, re.S)
        title = u'无标题'
        if myMatch:
            try:
                title = myMatch.group(1).decode('utf-8').strip()
            except UnicodeDecodeError:
                title = myMatch.group(1).decode('GBK').strip()
            title = title.replace('-', ' ').replace('|', ' ').replace(':', ' ').replace('/', ' ') \
                .replace('>', ' ').replace('\r', ' ').replace('\n', ' ').replace("\"", ' ') \
                .replace('*', ' ').replace('<', ' ').replace('?', ' ')
        self.title_count += 1
        return ('%s_' % self.title_count) + title

    def find_link(self, page_message):
        urlMatch = re.compile(r'<a.*?href=\"(https?://[0-9a-zA-Z_./]*?\.uestc\..*?)\".*?>.*?</a>')
        link_list = re.findall(urlMatch, page_message)
        for link in link_list:
            if link not in self.list_urls:
                try:
                    print u'找到新的链接: %s' % link
                except UnicodeDecodeError:
                    print u'找到新的链接: %s' % link.decode('GBK')
                self.list_urls.append(link)

    def save_link(self, urls):
        with open('UESTC_Link.html', 'wb') as f:
            for url in urls:
                f.write(url + '\n')