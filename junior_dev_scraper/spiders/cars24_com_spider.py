import scrapy
import json
import re
from benedict import benedict
from w3lib.url import add_or_replace_parameter

# See https://www.cars24.com/ae/buy-used-cars-dubai/


class Car24ComSpider(scrapy.Spider):
    name = 'cars24_com_spider'
    api_url = 'https://listing-service.c24.tech/v2/vehicle?isSeoFilter=true&sf=city:DU&sf=gaId:1120805531.1696266648&size=25&spath=buy-used-cars-dubai&page={}&variant=filterV5'
    start_page = 0
    catalog_headers = {
        'X_country': 'AE',
        'X_vehicle_type': 'CAR'
    }
    
    total_products = 0

    def start_requests(self):
        yield scrapy.Request(self.api_url.format(self.start_page), headers=self.catalog_headers, callback=self.parse)

    def parse(self, response):
        data = json.loads(response.text)
        
        products = data.get('results', [])
       

        for product in products:
            
            brand = product.get('make')
            model = product.get('model')
            year = product.get('year')
            city = product.get('city')
            appointment_id = product.get('appointmentId')
            engine = product.get('engineSize')
            price = product.get('price')
            model = product.get('model')
            modelParsed = "-".join(word.lower() for word in model.split())
            mileage = product.get('odometerReading')
            link = f'https://www.cars24.com/ae/buy-used-{brand.lower()}-{modelParsed}-{year.lower()}-cars-{city.lower()}-{appointment_id.lower()}'

            yield {
                'brand': brand,
                'engineSize': engine,
                'year': year,
                'link': link,
                'price': price,
                'model': model,
                'mileage': mileage,
            }
            self.total_products += 1
            
        
        if self.total_products < data['total']:
            self.start_page += 1
            yield scrapy.Request(self.api_url.format(self.start_page), headers=self.catalog_headers, callback=self.parse)
    # Good luck

