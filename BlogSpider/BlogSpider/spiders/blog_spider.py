# coding=utf-8
import scrapy
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from scrapy.http import Request
from bs4 import BeautifulSoup
import urllib2
import urllib
import json


class toxni_spider(scrapy.Spider):
    name = 'toxni.com'
    start_urls = ['http://toxni.com']
    start = True

    urls = []
    desc = []

    def parse(self, response):
        if self.start:
            selector = scrapy.Selector(response)
            for block in selector.xpath('//article'):
                link = block.xpath('header/h2/a/@href').extract()[0]
                domain = 'http://toxni.com'
                if 'http' not in link:
                    link = domain + link
                self.urls.append(link)
                self.desc.append(block.xpath('section/p/text()').extract()[0])
            self.start = False
            yield Request(self.urls.pop(), callback=self.parse)
        else:
            selector = scrapy.Selector(response)
            head_link = 'http://toxni.com'
            title = selector.xpath('//h1[@class="post-title"]/text()').extract()[0]
            date = selector.xpath('//time[@class="post-date"]/@datetime').extract()[0]
            author = 'toxni'
            article = self.reset_article(selector.xpath('//section[@class="post-content"]/*').extract(), head_link)
            desc = self.desc.pop()
            self.handler(title, date, author, article, desc)
            if len(self.urls):
                yield Request(self.urls.pop(), callback=self.parse)

    def reset_article(self, article_div, head_link):
        article_content = ''
        for ele in article_div:
            article_content += ele
        soup = BeautifulSoup(article_content, 'lxml')
        for tag in soup.find_all(['a', 'img']):
            if tag.name == 'a':
                if tag.has_attr('href'):
                    if 'http' not in tag['href']:
                        tag['href'] = head_link + tag['href']
            elif tag.name == 'img':
                if 'http' not in tag['src']:
                    tag['src'] = head_link + tag['src']
        for tag in soup.find_all(attrs={'class': True}):
            del tag['class']
        return soup.prettify()

    def handler(self, title, date, author, article, desc):
        post_data = {'title': title, 'date': date, 'author': author, 'article': article, 'desc': desc}
        req = urllib2.Request('http://127.0.0.1:8000/publish/', data=urllib.urlencode(post_data))
        print urllib2.urlopen(req).read()


class lypeer_spider(scrapy.Spider):
    name = 'lypeer.com'
    start_urls = ['http://blog.csdn.net/luoyanglizi/']
    start = True

    urls = []
    desc = []

    def parse(self, response):
        if self.start:
            selector = scrapy.Selector(response)
            for block in selector.xpath('//div[@class="list_item article_item"]'):
                link = block.xpath('div[@class="article_title"]/h1/span/a/@href').extract()[0]
                domain = 'http://blog.csdn.net'
                if 'http' not in link:
                    link = domain + link
                self.urls.append(link)
                self.desc.append(block.xpath('div[@class="article_description"]/text()').extract()[0])
            self.start = False
            yield Request(self.urls.pop(), callback=self.parse)
        else:
            selector = scrapy.Selector(response)
            head_link = 'http://blog.csdn.net'
            title = selector.xpath('//span[@class="link_title"]/a/text()').extract()[0].strip()
            date = selector.xpath('//span[@class="link_postdate"]/text()').extract()[0].split()[0]
            author = 'lypeer'
            article = self.reset_article(selector.xpath('//div[@class="markdown_views"]/*').extract(), head_link)
            desc = self.desc.pop().strip()
            self.handler(title, date, author, article, desc)
            if len(self.urls):
                yield Request(self.urls.pop(), callback=self.parse)

    def reset_article(self, article_div, head_link):
        article_content = ''
        for ele in article_div:
            article_content += ele
        soup = BeautifulSoup(article_content, 'lxml')
        for tag in soup.find_all(['a', 'img']):
            if tag.name == 'a':
                if tag.has_attr('href'):
                    if 'http' not in tag['href']:
                        tag['href'] = head_link + tag['href']
            elif tag.name == 'img':
                if 'http' not in tag['src']:
                    tag['src'] = head_link + tag['src']
        for tag in soup.find_all(attrs={'class': True}):
            del tag['class']
        return soup.prettify()

    def handler(self, title, date, author, article, desc):
        post_data = {'title': title, 'date': date, 'author': author, 'article': article, 'desc': desc}
        req = urllib2.Request('http://127.0.0.1:8000/publish/', data=urllib.urlencode(post_data))
        print urllib2.urlopen(req).read()


class lazycat_spider(scrapy.Spider):
    name = 'lazycat.com'
    start_urls = ['http://ilazycat.com/']
    start = True
    ready = False

    url_id = 1
    end_id = None
    urls = []

    def parse(self, response):
        if not self.ready:
            selector = scrapy.Selector(response)
            if self.start:
                self.end_id = int(
                    selector.xpath('//div[@class="pagenav clearfix"]/a[@title]/@href').extract()[0].split('/')[-1])
                self.start = False
            for link in selector.xpath('//h2[@class="post-title entry-title"]/a/@href').extract():
                domain = 'http://ilazycat.com'
                if 'http' not in link:
                    link = domain + link
                self.urls.append(link)
            if self.url_id != self.end_id:
                self.url_id += 1
                next_url = 'http://ilazycat.com/page/' + str(self.url_id)
                yield Request(next_url, callback=self.parse)
            else:
                self.ready = True
                yield Request(self.urls.pop(), callback=self.parse)
        else:
            selector = scrapy.Selector(response)
            head_link = '/'.join(response.url.split('/')[0:3])
            title = selector.xpath('//h1[@class="post-title entry-title"]/a/text()').extract()
            if len(title):
                title = title[0]
            author = 'lazycat'
            article = self.reset_article(selector.xpath('//div[@class="entry-content"]/*').extract(), head_link)
            desc = ''
            self.handler(title, author, article, desc)
            if len(self.urls):
                yield Request(self.urls.pop(), callback=self.parse)

    def reset_article(self, article_div, head_link):
        article_content = ''
        for ele in article_div:
            article_content += ele
        soup = BeautifulSoup(article_content, 'lxml')
        for tag in soup.find_all(['a', 'img']):
            if tag.name == 'a':
                if tag.has_attr('href'):
                    if 'http' not in tag['href']:
                        tag['href'] = head_link + tag['href']
            elif tag.name == 'img':
                if 'http' not in tag['src']:
                    tag['src'] = head_link + tag['src']
        for tag in soup.find_all(attrs={'class': True}):
            del tag['class']
        soup.find(id='anyShare').string = ''
        return soup.prettify()

    def handler(self, title, author, article, desc):
        post_data = {'title': title, 'author': author, 'article': article, 'desc': desc}
        req = urllib2.Request('http://127.0.0.1:8000/publish/', data=urllib.urlencode(post_data))
        print urllib2.urlopen(req).read()


class shadow_spider(scrapy.Spider):
    name = 'shadow.com'
    start_urls = ['http://shadowwood.me']
    start = True
    ready = False

    blist = []
    urls = []
    date_list = []
    desc = []

    def parse(self, response):
        if not self.ready:
            selector = scrapy.Selector(response)
            if self.start:
                for tlist in selector.xpath('//div[@class="row text-center theme-box"]/div/a/@href').extract():
                    if 'http' not in tlist:
                        tlist = 'http://shadowwood.me/' + tlist
                    self.blist.append(tlist)
                self.start = False
                yield Request(self.blist.pop(), callback=self.parse)
            else:
                for block in selector.xpath('//div[@class="col-md-12 col-lg-12 my-panel"]'):
                    link = block.xpath('a/@href').extract()[0]
                    if 'http' not in link:
                        link = 'http://shadowwood.me/' + link
                    self.urls.append(link)
                    date = block.xpath('p[@class="read-number"]/text()').extract()[1].split('|')[0].split(':')[1].replace(' ', '')
                    self.date_list.append(date)
                    self.desc.append(block.xpath('p/text()').extract()[0])
                if len(self.blist):
                    yield Request(self.blist.pop(), callback=self.parse)
                else:
                    self.ready = True
                    yield Request(self.urls.pop(), callback=self.parse)
        else:
            selector = scrapy.Selector(response)
            title = selector.xpath('//h3[@class="text-center article-head"]/text()').extract()[0].strip()
            author = 'shadow'
            date = self.date_list.pop()
            article = self.reset_article(selector.xpath('//div[@class="panel my-panel article-body"]/*').extract())
            desc = self.desc.pop().strip()
            self.handler(title, author, article, date, desc)
            if len(self.urls):
                yield Request(self.urls.pop(), callback=self.parse)

    def reset_article(self, article_div):
        article_content = ''
        for ele in article_div:
            article_content += ele
        soup = BeautifulSoup(article_content, 'lxml')
        for tag in soup.find_all(['a', 'img']):
            if tag.name == 'a':
                if tag.has_attr('href'):
                    if 'http' not in tag['href']:
                        tag['href'] = 'http://shadowwood.me/' + tag['href']
            elif tag.name == 'img':
                if 'http' not in tag['src']:
                    tag['src'] = 'http://shadowwood.me' + tag['src']
        for tag in soup.find_all(attrs={'class': True}):
            del tag['class']
        soup.find('h3').string = ''
        return soup.prettify()

    def handler(self, title, author, article, date, desc):
        post_data = {'title': title, 'author': author, 'article': article, 'date': date, 'desc': desc}
        req = urllib2.Request('http://127.0.0.1:8000/publish/', data=urllib.urlencode(post_data))
        print urllib2.urlopen(req).read()


class yasic_spider(scrapy.Spider):
    name = 'yasic.com'
    start_urls = ['http://yasicyu.com/']
    start = True
    ready = False

    type = []
    urls = []
    desc = []

    def parse(self, response):
        if not self.ready:
            selector = scrapy.Selector(response)
            if self.start:
                for mtype in selector.xpath('//div[@class="image-grid"]/a/@id').extract():
                    self.type.append(mtype)
                self.start = False
                yield Request('http://yasicyu.com/classification?type=' + self.type.pop(), callback=self.parse)
            else:
                for block in selector.xpath('//article'):
                    ltitle = block.xpath('div[@class="content"]/h2/text()').extract()[0]
                    self.urls.append('http://yasicyu.com/generic?title=' + ltitle)
                    self.desc.append(block.xpath('div[@class="content"]/p/text()').extract()[0])
                if len(self.type):
                    yield Request('http://yasicyu.com/classification?type=' + self.type.pop(), callback=self.parse)
                else:
                    self.ready = True
                    yield Request(self.urls.pop(), callback=self.parse)
        else:
            selector = scrapy.Selector(response)
            head_link = 'http://yasicyu.com'
            title = selector.xpath('//header[@class="major special"]/h2/text()').extract()[0]
            author = 'yasic'
            date = selector.xpath('//header[@class="major special"]/p[2]/text()').extract()[0].split(':')[1].replace(' ', '')
            article = self.reset_article(selector.xpath('//div[@id="write"]/*').extract(), head_link)
            desc = self.desc.pop()
            self.handler(title, author, article, date, desc)
            if len(self.urls):
                yield Request(self.urls.pop(), callback=self.parse)

    def reset_article(self, article_div, head_link):
        article_content = ''
        for ele in article_div:
            article_content += ele
        soup = BeautifulSoup(article_content, 'lxml')
        for tag in soup.find_all(['a', 'img']):
            if tag.name == 'a':
                if tag.has_attr('href'):
                    if 'http' not in tag['href']:
                        tag['href'] = head_link + tag['href']
            elif tag.name == 'img':
                if 'http' not in tag['src']:
                    tag['src'] = head_link + tag['src']
        for tag in soup.find_all(attrs={'class': True}):
            del tag['class']
        return soup.prettify()

    def handler(self, title, author, article, date, desc):
        post_data = {'title': title, 'author': author, 'article': article, 'date': date, 'desc': desc}
        req = urllib2.Request('http://127.0.0.1:8000/publish/', data=urllib.urlencode(post_data))
        print urllib2.urlopen(req).read()


class trotyl_spider(scrapy.Spider):
    name = 'trotyl.com'
    start_urls = ['http://www.trotyl.me']
    start = True
    ready = False

    url_id = 1
    end_id = None
    urls = []
    desc = []

    def parse(self, response):
        if not self.ready:
            selector = scrapy.Selector(response)
            if self.start:
                self.end_id = int(
                    selector.xpath('//span[@class="page-number"]/text()').extract()[0].split(' ')[-1])
                self.start = False
            domain = 'http://www.trotyl.me'
            for block in selector.xpath('//article'):
                link = block.xpath('div/header/h2/a/@href').extract()[0]
                if 'http' not in link:
                    link = domain + link
                self.urls.append(link)
                self.desc.append(block.xpath('div/section/p/text()').extract()[0])
            if self.url_id != self.end_id:
                self.url_id += 1
                next_url = 'http://www.trotyl.me/page/' + str(self.url_id)
                yield Request(next_url, callback=self.parse)
            else:
                self.ready = True
                yield Request(self.urls.pop(), callback=self.parse)
        else:
            selector = scrapy.Selector(response)
            head_link = 'http://www.trotyl.me'
            title = selector.xpath('//h1[@class="post-title"]/text()').extract()[0]
            author = 'trotyl'
            article = self.reset_article(selector.xpath('//section[@class="post-content"]/*').extract(), head_link)
            date = selector.xpath('//time/@datetime').extract()[0]
            desc = self.desc.pop()
            self.handler(title, author, article, date, desc)
            if len(self.urls):
                yield Request(self.urls.pop(), callback=self.parse)

    def reset_article(self, article_div, head_link):
        article_content = ''
        for ele in article_div:
            article_content += ele
        soup = BeautifulSoup(article_content, 'lxml')
        for tag in soup.find_all(['a', 'img']):
            if tag.name == 'a':
                if tag.has_attr('href'):
                    if 'http' not in tag['href']:
                        tag['href'] = head_link + tag['href']
            elif tag.name == 'img':
                if 'http' not in tag['src']:
                    tag['src'] = head_link + tag['src']
        for tag in soup.find_all(attrs={'class': True}):
            del tag['class']
        return soup.prettify()

    def handler(self, title, author, article, date, desc):
        post_data = {'title': title, 'author': author, 'article': article, 'date': date, 'desc': desc}
        req = urllib2.Request('http://127.0.0.1:8000/publish/', data=urllib.urlencode(post_data))
        print urllib2.urlopen(req).read()


class rapo_spider(scrapy.Spider):
    name = 'rapo.com'
    start_urls = ['http://www.rapospectre.com/detail/01/']

    url = 'http://www.rapospectre.com/detail/'

    def parse(self, response):
        data = json.loads(response.body)
        date = data['body']['blog']['classification']['create_time'].split(' ')[0]
        title = data['body']['blog']['sub_caption']
        author = 'rapo'
        article = data['body']['blog']['content']
        desc = ''
        next_id = data['body']['pagination']['next_id']
        this_id = data['body']['blog']['id']
        self.handler(title, author, article, date, desc)
        if next_id != this_id:
            next_url = self.url + str(next_id)
            yield Request(next_url, callback=self.parse)
        else:
            return

    def reset_article(self, article_div, head_link):
        article_content = ''
        for ele in article_div:
            article_content += ele
        soup = BeautifulSoup(article_content, 'lxml')
        for tag in soup.find_all(['a', 'img']):
            if tag.name == 'a':
                if tag.has_attr('href'):
                    if 'http' not in tag['href']:
                        tag['href'] = head_link + tag['href']
            elif tag.name == 'img':
                if 'http' not in tag['src']:
                    tag['src'] = head_link + tag['src']
        for tag in soup.find_all(attrs={'class': True}):
            del tag['class']
        return soup.prettify()

    def handler(self, title, author, article, date, desc):
        post_data = {'title': title, 'author': author, 'article': article, 'date': date, 'desc': desc}
        req = urllib2.Request('http://127.0.0.1:8000/publish/', data=urllib.urlencode(post_data))
        print urllib2.urlopen(req).read()


class snowbean_spider(scrapy.Spider):
    name = 'snowbean.com'
    start_urls = ['http://wuapnjie.github.io/']
    start = True

    urls = []
    desc = []

    def parse(self, response):
        if self.start:
            selector = scrapy.Selector(response)
            for block in selector.xpath('//article'):
                link = block.xpath('div/header/h1/a/@href').extract()[0]
                domain = 'http://wuapnjie.github.io'
                if 'http' not in link:
                    link = domain + link
                self.urls.append(link)
                self.desc.append(self.reset_article(block.xpath('div/div[@class="entry"]/*').extract(), domain))
            self.start = False
            yield Request(self.urls.pop(), callback=self.parse)
        else:
            selector = scrapy.Selector(response)
            head_link = 'http://wuapnjie.github.io'
            title = selector.xpath('//h1[@class="title"]/text()').extract()[0]
            date = selector.xpath('//time/@datetime').extract()[0].split('T')[0]
            author = 'snowbean'
            article = self.reset_article(selector.xpath('//div[@class="entry"]/*').extract(), head_link)
            desc = self.desc.pop()
            self.handler(title, date, author, article, desc)
            if len(self.urls):
                yield Request(self.urls.pop(), callback=self.parse)

    def reset_article(self, article_div, head_link):
        article_content = ''
        for ele in article_div:
            article_content += ele
        soup = BeautifulSoup(article_content, 'lxml')
        for tag in soup.find_all(['a', 'img']):
            if tag.name == 'a':
                if tag.has_attr('href'):
                    if 'http' not in tag['href']:
                        tag['href'] = head_link + tag['href']
            elif tag.name == 'img':
                if 'http' not in tag['src']:
                    tag['src'] = head_link + tag['src']
        for tag in soup.find_all(attrs={'class': True}):
            del tag['class']
        return soup.prettify()

    def handler(self, title, date, author, article, desc):
        post_data = {'title': title, 'date': date, 'author': author, 'article': article, 'desc': desc}
        req = urllib2.Request('http://127.0.0.1:8000/publish/', data=urllib.urlencode(post_data))
        print urllib2.urlopen(req).read()
