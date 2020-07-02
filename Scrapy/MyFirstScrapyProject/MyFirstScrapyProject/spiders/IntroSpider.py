import scrapy

filename = 'BooksTitles.txt'

class IntroSpider(scrapy.Spider):
    name = "IntroSpider"
    
    def start_requests(self):
        urls = ["http://books.toscrape.com/catalogue/page-2.html"]

        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self,response):
        bookList = response.css("article.product_pod > h3 > a::attr(title)").extract()
        print(bookList)

        with open(filename,'a+') as f:
            for bookTitle in bookList:
                f.write(bookTitle + "\n")