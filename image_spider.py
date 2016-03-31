# -*- coding=utf-8 -*-
"""
    实例化时需要init_url参数,实例化后需要设置url_match参数
    init_url参数:用于程序的入口链接
    url_match参数:程序寻找新连接的依据
"""
import urllib
import urllib2
import re
import httplib
import sys
import socket
import os


class ImageSpider:
    def __init__(self, init_url):  # 实例化时需要一个入口URL
        self.url_match = ''  # 需要设置匹配URL的正则表达式
        self.exist_urls = []
        self.list_urls = [init_url, ]
        self.images = []
        self.headers = {
                          'User-Agent': '''Mozilla/5.0 (Windows NT 6.3; WOW64)
                            AppleWebKit/537.36 (KHTML, like Gecko)
                            Chrome/42.0.2311.152 Safari/537.36 LBBROWSER'''
        }
        self.image_count = 0
        reload(sys)
        sys.setdefaultencoding('utf-8')
        urllib2.socket.setdefaulttimeout(5)

    def spider(self):
        url_index = 0
        while url_index < len(self.list_urls):
            current_url = self.list_urls[url_index]
            print u'正在请求URL: %s' % current_url
            try:
                req = urllib2.Request(current_url, headers=self.headers)
                myPage = urllib2.urlopen(req)
            except urllib2.URLError:
                continue
            except urllib2.HTTPError:
                continue
            except socket.timeout:
                continue
            except httplib.BadStatusLine, err:
                continue
            finally:
                url_index = url_index + 1
            self.deal_page(myPage)
            self.exist_urls.append(current_url)
        print u'爬虫进程结束,找到图片%s个' % self.image_count

    def deal_page(self, myPage):
        try:
            page_message = myPage.read()
        except socket.timeout:
            return
        title = self.find_title(page_message)
        self.find_link(page_message)
        self.find_images(page_message)

    def find_title(self, page_message):
        myMatch = re.search(r'<title>(.*?)</title>', page_message, re.S)
        title = u'NO TITLE'
        if myMatch:
            try:
                title = myMatch.group(1).decode('utf-8').strip()
            except UnicodeDecodeError:
                title = myMatch.group(1).decode('GBK').strip()
            title = title.replace('-', ' ').replace('|', ' ').replace(':', ' ').replace('/', ' ') \
                .replace('>', ' ').replace('\r', ' ').replace('\n', ' ').replace("\"", ' ') \
                .replace('*', ' ').replace('<', ' ').replace('?', ' ')
        return title

    def find_link(self, page_message):
        link_match = re.compile(self.url_match)
        link_list = re.findall(link_match, page_message)
        for link in link_list:
            if link not in self.list_urls:
                print u'添加链接:%s' % link
                self.list_urls.append(link)

    def find_images(self, page_message):
        image_match = re.compile(r'src=\"(.*?\.[jpg|gif])\"')
        image_list = re.findall(image_match, page_message)
        for image in image_list:
            if image not in self.images:
                file_path = './images/'
                file_name = 'image%s.jpg' % self.image_count
                if not os.path.exists('./images'):
                    os.mkdir('images')
                try:
                    urllib.urlretrieve(image, file_path + file_name)
                except socket.timeout:
                    continue
                except IOError:
                    continue
                self.image_count += 1
                self.images.append(image)