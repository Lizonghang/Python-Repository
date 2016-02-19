# -*- coding=utf-8 -*-
import urllib
import urllib2
import cookielib
import re


class GetInformation:
    def __init__(self, passinfo):
        self.headers = {
            'User-Agent': '''Mozilla/5.0 (Windows NT 6.3; WOW64)
                            AppleWebKit/537.36 (KHTML, like Gecko)
                            Chrome/42.0.2311.152 Safari/537.36 LBBROWSER'''
        }
        self.username = passinfo['username']
        self.passkey = passinfo['passkey']

    def login(self):
        login_url = 'https://uis.uestc.edu.cn/amserver/UI/Login?goto=http%3A%2F%2Fportal.uestc.edu.cn%2Flogin.portal'
        postdata = urllib.urlencode({
            'IDToken0': '',
            'IDToken1': self.username,
            'IDToken2': self.passkey,
            'IDButton': 'Submit',
            'goto': 'aHR0cDovL3BvcnRhbC51ZXN0Yy5lZHUuY24vbG9naW4ucG9ydGFs',
            'encoded': 'true',
            'gx_charset': 'UTF-8'
        })
        cookieJar = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))
        urllib2.install_opener(opener)
        urllib2.urlopen(urllib2.Request(login_url, data=postdata, headers=self.headers))

    def getHome(self):
        self.login()
        info_source = 'http://eams.uestc.edu.cn/eams/home!childmenus.action?menu.id=844'
        req = urllib2.Request(info_source, headers=self.headers)
        html = urllib2.urlopen(req)
        return html.read()

    def parsePage(self, html):
        pageMatch = re.compile(r'<a href=\"(.*?)\".*?myTitle=\"(.*?)\".*?>.*?</a>')
        matchPages = re.findall(pageMatch, html)
        subPages = dict()
        for eachPage in matchPages:
            subPages[eachPage[1].decode('utf-8')] = 'http://eams.uestc.edu.cn' + eachPage[0]
        return subPages

    def getInfo(self, choosePage, url):
        allInfo = urllib2.urlopen(urllib2.Request(url, headers=self.headers)).read()
        f = open(choosePage + '.html', 'wb')
        f.write(allInfo)
        f.close()
        print '''
-------------------------------------------------------------------------------
您所需要的信息已保存到相应的文件,请注意查收
-------------------------------------------------------------------------------\n\n'''