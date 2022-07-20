import scrapy
from market_11.items import Market11Item

class St11Spider(scrapy.Spider):
    name = 'st11_best'
    
    def start_requests(self):
        yield scrapy.Request(url="https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&cornerNo=0",
                         callback=self.parse_mainpages)
        
    def parse_mainpages(self, response):
        print("parse_mainpages") 
        category_names = response.css('div.best_category_box ul#metaCtgrUl li button::text').getall() 
        for idx, name in enumerate(category_names):
            
            yield scrapy.Request(url="https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&cornerNo="+str(idx), 
                                  callback=self.parse_items, 
                                  meta={'maincategory_name':category_names[idx], 'subcategory_name':'All'})


    def parse_items(self, response):
        print('parse_items', response.meta['maincategory_name'], response.meta['subcategory_name']) #확인용
        best_items = response.css('div.viewtype.catal_ty')

        for idx, item in enumerate(best_items[1].css('li')): 
                                                            
            doc = Market11Item()        
            ranking = idx + 1 
            title = item.css('div.box_pd.ranking_pd a div.pname p::text').get().strip() 
            ori_price = item.css('div.box_pd.ranking_pd a div.pname div.price_info.cfix span.price_detail s::text').get()
            dis_price = item.css('div.box_pd.ranking_pd a div.pname div.price_info.cfix span.price_detail strong.sale_price::text').get()
            
            if ori_price == None: 
                ori_price = dis_price

            ori_price = ori_price.replace(',','').replace('원','')
            dis_price = dis_price.replace(',','').replace('원','')
            
            doc['main_category_name'] = response.meta['maincategory_name']
            doc['sub_category_name'] = response.meta['subcategory_name']
            doc['ranking'] = ranking
            doc['title'] = title
            doc['ori_price'] = ori_price
            doc['dis_price'] = dis_price
    
            yield doc