# import scrapy
# from ..items import AmazonproductscrapperItem
# class QuoteSpider(scrapy.Spider):
#     name = "quotes"
#     start_urls = [
#         "https://quotes.toscrape.com/"
#     ]
#     def parse(self, response):
#         items = AmazonproductscrapperItem()
#
#         all_div_quotes = response.css('div.quote')
#
#         for quotes in all_div_quotes:
#             title = quotes.css('span.text::text').extract()
#             author = quotes.css('.author::text').extract()
#             tag = quotes.css('.tag::text').extract()
#
#             items['title'] = title
#             items['author'] = author
#             items['tag'] = tag
#
#             yield items
#
#         next_page = response.css('li.next a::attr(href)').get()
#
#         if next_page is not None:
#             yield response.follow(next_page, callback = self.parse)
