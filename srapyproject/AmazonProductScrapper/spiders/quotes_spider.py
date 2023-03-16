import scrapy
from ..items import AmazonproductscrapperItem
class QuoteSpider(scrapy.Spider):
    name = "amazon"
    start_urls = [
        "https://www.amazon.com/b?node=283155"
    ]
    def parse(self, response):
        items = AmazonproductscrapperItem()
        # products = response.css('div.p13n-gridRow _cDEzb_grid-row_3VsqC::text').extract()
        # product = response.css('div#gridItemRoot').extract()
        #
        # for i in product:
        #     product_name = i.css('div.p13n-sc-truncate-desktop-type2  p13n-sc-truncated::text').extract()
        #     product_price = i.css('span._cDEzb_p13n-sc-price_3mJ9Z::text').extract()
        #     product_stars = i.css('span.a-icon-alt::text').extract()
        #     product_ratings = i.css('span.a-size-small::text').extract()

        p = response.css('div.p13n-sc-uncoverable-faceout')

        product_name = p.css('div.p13n-sc-truncate-desktop-type2 p13n-sc-truncated::text').extract()
        product_price = response.css('._cDEzb_p13n-sc-price_3mJ9Z , #p13n-asin-index-7 .p13n-sc-truncated').css('::text').extract()
        product_stars = response.css('span.a-icon-alt::text').extract()
        product_ratings = response.css('.a-size-small::text').extract()

        items['product_name'] = product_name
        items['product_price'] = product_price
        items['product_stars'] = product_stars
        items['product_ratings'] = product_ratings


        yield items





