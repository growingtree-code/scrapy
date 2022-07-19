import scrapy

class St11Spider(scrapy.Spider):
    name = 'st11_best'
    
    def start_requests(self): 
        coco = 123
        yield scrapy.Request(url="https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&cornerNo=0",
                             callback=self.parse_mainpages, 
                             meta={'coco123':coco})
        
    def parse_mainpages(self, response): 
        print("@@@@@@@ parse_mainpages 성공!!!! @@@@@@@", response.meta['coco123']) 
                
        print(response.css('div.best_category_box li button::text').getall()) 