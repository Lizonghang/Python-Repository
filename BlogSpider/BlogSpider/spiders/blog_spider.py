# coding=utf-8
import scrapy
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from scrapy.http import Request
from bs4 import BeautifulSoup
import urllib2
import urllib


class toxni_spider(scrapy.Spider):
    name = 'toxni.com'
    start_urls = ['http://toxni.com']
    start = True

    urls = []

    def parse(self, response):
        if self.start:
            selector = scrapy.Selector(response)
            for link in selector.xpath('//h2[@class="post-title"]/a/@href').extract():
                domain = '/'.join(response.url.split('/')[0:3])
                if domain not in link:
                    link = domain + link
                self.urls.append(link)
            self.start = False
            yield Request(self.urls.pop(), callback=self.parse)
        else:
            selector = scrapy.Selector(response)
            head_link = '/'.join(response.url.split('/')[0:3])
            title = selector.xpath('//h1[@class="post-title"]/text()').extract()[0]
            date = selector.xpath('//time[@class="post-date"]/@datetime').extract()[0]
            author = 'toxni'
            article = self.reset_article(selector.xpath('//section[@class="post-content"]/*').extract(), head_link)
            self.handler(title, date, author, article)
            if len(self.urls):
                yield Request(self.urls.pop(), callback=self.parse)

    def reset_article(self, article_div, head_link):
        article_content = ''
        for ele in article_div:
            article_content += ele
        soup = BeautifulSoup(article_content, 'lxml')
        for tag in soup.find_all(['a', 'img']):
            if tag.name == 'a':
                if 'http' not in tag['href']:
                    tag['href'] = head_link + tag['href']
            elif tag.name == 'img':
                if 'http' not in tag['src']:
                    tag['src'] = head_link + tag['src']
        for tag in soup.find_all(attrs={'class': True}):
            del tag['class']
        return soup.prettify()

    def handler(self, title, date, author, article):
        post_data = {'title': title, 'date': date, 'author': author, 'article': article}
        req = urllib2.Request('http://127.0.0.1:8000/test/', data=urllib.urlencode(post_data))
        print urllib2.urlopen(req).read()


class lypeer_spider(scrapy.Spider):
    name = 'lypeer.com'
    start_urls = ['http://blog.csdn.net/luoyanglizi/']
    start = True

    urls = []

    def parse(self, response):
        if self.start:
            selector = scrapy.Selector(response)
            for link in selector.xpath('//span[@class="link_title"]/a/@href').extract():
                domain = '/'.join(response.url.split('/')[0:3])
                if domain not in link:
                    link = domain + link
                self.urls.append(link)
            self.start = False
            yield Request(self.urls.pop(), callback=self.parse)
        else:
            selector = scrapy.Selector(response)
            head_link = '/'.join(response.url.split('/')[0:3])
            title = selector.xpath('//span[@class="link_title"]/a/text()').extract()[0]
            date = selector.xpath('//span[@class="link_postdate"]/text()').extract()[0].split()[0]
            author = 'lypeer'
            article = self.reset_article(selector.xpath('//div[@class="markdown_views"]/*').extract(), head_link)
            self.handler(title, date, author, article)
            if len(self.urls):
                yield Request(self.urls.pop(), callback=self.parse)

    def reset_article(self, article_div, head_link):
        article_content = ''
        for ele in article_div:
            article_content += ele
        soup = BeautifulSoup(article_content, 'lxml')
        for tag in soup.find_all(['a', 'img']):
            if tag.name == 'a':
                if 'http' not in tag['href']:
                    tag['href'] = head_link + tag['href']
            elif tag.name == 'img':
                if 'http' not in tag['src']:
                    tag['src'] = head_link + tag['src']
        for tag in soup.find_all(attrs={'class': True}):
            del tag['class']
        return soup.prettify()

    def handler(self, title, date, author, article):
        post_data = {'title': title, 'date': date, 'author': author, 'article': article}
        req = urllib2.Request('http://127.0.0.1:8000/publish/', data=urllib.urlencode(post_data))
        print urllib2.urlopen(req).read()
