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
    def __init__(self, init_url, up_index, bottom_index):
        self.init_url = init_url
        self.images = []
        self.headers = {
                          'User-Agent': '''Mozilla/5.0 (Windows NT 6.3; WOW64)
                            AppleWebKit/537.36 (KHTML, like Gecko)
                            Chrome/42.0.2311.152 Safari/537.36 LBBROWSER'''
        }
        self.count = 1
        self.index_count = up_index
        self.bottom_index = bottom_index
        reload(sys)
        sys.setdefaultencoding('utf-8')
        urllib2.socket.setdefaulttimeout(10)

    def spider(self):
        while self.index_count > self.bottom_index:
            root_url = self.init_url + str(self.index_count) + '.html'
            print u'尝试请求:%s' % root_url
            try:
                req = urllib2.Request(root_url, headers=self.headers)
                page_message = urllib2.urlopen(req).read()
			#except urllib2.URLError:
			#	self.index_count -= 1
			#	continue
            except urllib2.HTTPError:
                self.index_count -= 1
                continue
            print u'请求URL:%s' % root_url
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
            self.index_count -= 1
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
                self.images.append(image)