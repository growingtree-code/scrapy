import scrapy


class St11BestSpider(scrapy.Spider):
    name = 'st11_best'
    allowed_domains = ['https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&cornerNo=0']
    start_urls = ['https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&cornerNo=0']

    def parse(self, response):
        pass
