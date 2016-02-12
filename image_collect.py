# -*- coding=utf-8 -*-
"""
    实例化时需要init_urls参数,包括了要搜索的所有起点
"""
import urllib
import urllib2
import re
import httplib
import sys
import socket
import os


class ImageCollect:
    def __init__(self, init_urls):
        self.exist = []
        self.list_urls = init_urls
        self.images = []
        self.headers = {
                          'User-Agent': '''Mozilla/5.0 (Windows NT 6.3; WOW64)
                            AppleWebKit/537.36 (KHTML, like Gecko)
                            Chrome/42.0.2311.152 Safari/537.36 LBBROWSER'''
        }
        self.count = 1
        self.image_count = 0
        reload(sys)
        sys.setdefaultencoding('utf-8')
        urllib2.socket.setdefaulttimeout(10)

    def spider(self):
        url_index = 0
        while url_index < len(self.list_urls):
            root_url = self.list_urls[url_index]
            if root_url in self.exist:
                url_index += 1
                continue
            print u'开始请求URL: %s' % root_url
            req = urllib2.Request(root_url, headers=self.headers)
            page_message = urllib2.urlopen(req).read()
            self.exist.append(root_url)
            title = self.find_title(page_message)
            self.get_images(page_message, title)
            root_url = root_url.replace('.html', '')
            count = 2
            while True:
                current_url = root_url + '_%s.html' % count
                try:
                    req = urllib2.Request(current_url, headers=self.headers)
                    myPage = urllib2.urlopen(req)
                except urllib2.HTTPError, err:
                    if err.code == 404:
                        print u'搜索完成:%s' % title
                        self.count = 1
                        break
                print u'请求URL: %s' % current_url
                page_message = myPage.read()
                self.get_images(page_message, title)
                count += 1
            url_index += 1
        print u'爬虫进程结束,找到图片%s个' % self.image_count

    def find_title(self, page_message):
        myMatch = re.search(r'<title>(.*?)</title>', page_message, re.S)
        title = 'NO TITLE'
        if myMatch:
            try:
                title = myMatch.group(1).decode('utf-8').strip()
            except UnicodeDecodeError:
                title = myMatch.group(1).decode('GBK').strip()
            title = title.replace('-', ' ').replace('|', ' ').replace(':', ' ').replace('/', ' ') \
                .replace('>', ' ').replace('\r', ' ').replace('\n', ' ').replace("\"", ' ') \
                .replace('*', ' ').replace('<', ' ').replace('?', ' ')
        return title

    def get_images(self, page_message, title):
        image_match = re.compile(r'src=\"(.*?\.jpg)\"')
        image_list = re.findall(image_match, page_message)
        for image in image_list:
            if image not in self.images:
                file_path = './images/' + title
                file_name = '/image%s.jpg' % self.count
                if not os.path.exists('./images'):
                    os.mkdir('./images')
                if not os.path.exists(file_path):
                    os.mkdir(file_path)
                try:
                    urllib.urlretrieve(image, file_path + file_name)
                except socket.timeout:
                    continue
                except IOError:
                    continue
                self.count += 1
                self.image_count += 1
                self.images.append(image)