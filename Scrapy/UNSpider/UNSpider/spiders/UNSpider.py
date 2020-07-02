import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

filename = "UNPrograms.txt"

class GenSpiderCrawl(CrawlSpider):
    name = "UNProgramCrawler"

    allowed_domains = ["un.org"]
    start_urls = ["https://www.un.org/es/sections/what-we-do/index.html"]

    rules = (Rule(LinkExtractor(allow=("what-we-do"),
                                deny=("zh/sections","ru/sections","ar/sections")),
                                callback='parse_page'),)

    def parse_page(self,response):
        programsList = response.css("div.col-md-7.teaser > h4 > a::text").extract()

        for program in programsList:
            with open(filename,'a+') as f:
                f.write(program + "\n")