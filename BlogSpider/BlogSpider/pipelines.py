# -*- coding: utf-8 -*-
from BlogSpider.items import BlogspiderItem


class BlogspiderPipeline(object):
    def process_item(self, item, spider):
        return item
