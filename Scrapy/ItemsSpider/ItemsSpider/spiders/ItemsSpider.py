import scrapy
from ..items import ItemsSpiderItem

filename = "Items.txt"

class ProductDetails(scrapy.Spider):
    name = "ItemsSpider"

    start_urls = ["https://www.amazon.com/s?k=macbook&ref=nb_sb_noss"]

    def parse(self,response):
        searchResults = response.css("div.s-result-list > div.s-result-item.s-asin")

        for product in searchResults:
            title = product.css(".a-size-medium::text").extract_first()
            price = product.css(".a-price span::text").extract_first()
            link = product.css(".a-link-normal::attr(href)").extract_first()

            productItem = ItemsSpiderItem()

            productItem['title'] = title
            productItem['price'] = price
            productItem['link'] = link

            with open(filename,'a+') as f:
                f.write("title: "+ title + "\n")
                f.write("price: "+ str(price) + "\n")
                f.write("link: "+ str(link) + "\n")

            yield productItem
        
