import scrapy
from market_11.items import Market11Item

class Spider11Spider(scrapy.Spider):
    name = 'spider_11'
    allowed_domains = ['www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain']
    start_urls = ['http://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain']
                

    def parse(self, response):
                titles = response.css('div#bestPrdList div.viewtype.catal_ty ul li div a div.pname p::text').getall()
                for t in titles:         # t에 상품명 데이터 저장
                    item = Market11Item()    # (2) 객체 = <Item 이름>()
                    item['title'] = t
                    print(item)
                
                    # (3-a) 객체['필드 이름'] = 추출한 데이터
                    yield item           # (3-b) yield 객체

