# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose 

def convertPrice(price):
    if price:
        price = price.replace(',','')
        return price.replace('$','')

def shortenAmazonLink(link):
    productId = link.split('/')[-1]
    return "https://amazon.com/es/" + productId

class ItemloaderItem(scrapy.Item):
    title = scrapy.Field()

    price = scrapy.Field(input_processor = MapCompose(convertPrice))
    link = scrapy.Field(input_processor = MapCompose(shortenAmazonLink))
