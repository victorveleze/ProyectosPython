import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose
from scrapy.loader.processors import TakeFirst
from ..items import ItemloaderItem

class ProductDetails(scrapy.Spider):
    name = "ItemLoaderSpider"

    start_urls = ["https://www.amazon.com/s?k=macbook&ref=nb_sb_noss"]

    def parse(self,response):
        searchResults = response.css("div.s-result-list > div.s-result-item.s-asin")

        for product in searchResults:
            productLoader = ItemLoader(item=ItemloaderItem(),selector=product)

            productLoader.default_output_processor = TakeFirst()

            productLoader.add_css('title','.a-size-medium::text')
            productLoader.add_css('price','.a-price span::text')
            productLoader.add_css('link','.a-link-normal::attr(href)')
        
            yield productLoader.load_item()