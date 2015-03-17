# -*- coding: utf-8 -*-
#<div class="index_box">
#     <div class="index_box_lit"><a href='/duPont-REGISTRY-Homes---April-2015_255937.html'><img src='/upimg/allimg/150309/1939430_lit.jpg' width=85 height=113 align=left></a></div>
#    <div class="index_box_title list_title"><a href='/duPont-REGISTRY-Homes---April-2015_255937.html'>duPont REGISTRY Homes - April 2015</a></div>
#    <div class="index_box_info list_title">English | HQ PDF | 116 pages | 34 MB Download http://longfiles.com/kbe3qrpxf800/duPont_REGISTRY_Homes_-_April_2015.pdf.html http://onmirror.com/ndf09h7ly8q2/duPont_REGISTRY_Homes_-_April_2015.pdf.html...</div>
#    <div class="index_box_tools">( Category:<a href='/Magazine/index.html'>Magazine</a> Date:09 Mar 2015 )</div>
#</div>


import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector


from eb3k.items import eb3KItem

class eb3kSpider(CrawlSpider):
    name = "eb3k"
    allowed_domains = ["ebook3000.com"]
    start_urls = (
        'http://www.ebook3000.com/',
    )

    rules = (Rule (SgmlLinkExtractor(allow=("index_\d\.htm", ),restrict_xpaths=('//div[@class="change_page"]',))
    , callback="parse_items", follow= True),
    )

    #def parse(self, response):
    #    for sel in response.xpath('//div[@class="index_box"]'):
    #        item = eb3KItem()
    #        item['url'] = response.url.rstrip('/')
    #        item['title'] = sel.xpath('div[2]/a/text()').extract()
    #        item['thumb'] = sel.xpath('div[1]/a/img/@src').extract()
    #        item['page'] = sel.xpath('div[1]/a/@href').extract()
    #        item['image'] = ['N/A'] 
    #        item['link'] = ['N/A']

    #        yield item

    def parse_items(self, response):
        items = []
        for sel in response.xpath('//div[@class="index_box"]'):
            item = eb3KItem()
            item['url'] = response.url.rstrip('/')
            item['title'] = sel.xpath('div[2]/a/text()').extract()
            item['thumb'] = sel.xpath('div[1]/a/img/@src').extract()
            item['page'] = sel.xpath('div[1]/a/@href').extract()
            item['image'] = ['N/A'] 
            item['link'] = ['N/A']

            item['image_urls'] = sel.xpath('div[1]/a/img/@src').extract()
            items.append(item)

        return(items)

