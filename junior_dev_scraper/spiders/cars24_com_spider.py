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
                'year': products.css('._1i1E6::text').get().split(' |', 1)[0],
                'link': products.attrib['href'],
                'price': products.css('.aApXW ._7yds2::text').get().replace(',', ''),
                'model': products.css('h3.RZ4T7::text').get().split(' ', 1)[1],
                'mileage': products.css('ul._3ZoHn li:nth-of-type(2)::text').get().replace(',', '').replace(' km', ''),
            }
    # Good luck
