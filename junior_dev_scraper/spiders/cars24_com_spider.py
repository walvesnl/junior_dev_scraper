import scrapy
import json
import re
from benedict import benedict
from w3lib.url import add_or_replace_parameter

# See https://www.cars24.com/ae/buy-used-cars-dubai/


class Car24ComSpider(scrapy.Spider):
    name = 'cars24_com_spider'
    start_urls = ['https://www.cars24.com/ae/buy-used-cars-dubai/']

    def parse(self, response):
        for products in response.css('a._1Lu5u'):
            yield {
                'brand': products.css('h3.RZ4T7::text').get().split(' ', 1)[0],
                'engine': products.css('ul._3ZoHn li:nth-of-type(3)::text').get(),
                'year': ,
                'link': ,
                'price': ,
                'model': ,
                'mileage': ,
            }
    # Good luck
