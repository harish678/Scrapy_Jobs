import scrapy


class ISROSpider(scrapy.Item):
    Location = scrapy.Field()
    Post = scrapy.Field()
    Advertisement_Number = scrapy.Field()