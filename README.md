# Pre-interview test for the position of Junior Developer at The Dutch Selection

## Introduction
At The Dutch Selection we collect data from the internet. We build scrapers using Python and Scrapy for our clients.

## Assignment
We would like you to build a scraper for the website [https://www.cars24.com/ae/buy-used-cars-dubai/](https://www.cars24.com/ae/buy-used-cars-dubai/). The scraper should collect the following data from car ads shown on the website:

- Brand / make of a car
- Engine size
- Year of manufacture
- Deeplink to the car details page
- Fuel Type
- Price
- Model
- Mileage

The scraper should be written in Python and Scrapy. The data should be exported to a CSV file.

## Deliverables
- A working scraper that can be run from the command line

## Tips
- We always start by inspecting the website in a browser to see what kind of requests are done and where the data we need comes from.
- You should not need to use any other libraries than are listed in the requirements.txt file.
- You should not need any kind of proxy server for this assignment.
- The Scrapy docs are a great resource: [https://docs.scrapy.org/en/latest/](https://docs.scrapy.org/en/latest/)
- Scrapy is all set up in this project, tweaking of the settings should not be necessary.
- The junior_dev_scraper/spiders/cars24_com_spider.py file is where you should put your code and should be the only file you need to edit.
- There is a theoretical chance you will be blocked from the site. If this happens, please let us know and show what you've got until that point.