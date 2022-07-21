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

        for idx, name in enumerate(category_names):

            yield scrapy.Request(url="https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&cornerNo="+str(idx), 
                                  callback=self.parse_subcategory,
                                  meta={'maincategory_name':category_names[idx],'index':idx})

    def parse_subcategory(self, response):
        print('parse_subcategory', response.meta['maincategory_name'])        
        subcategory_names = response.css('div.best_category_box ul#metaCtgrUl li button::text').getall()#왼쪽 서브카테고리가 아닌 startURL 페이지 내 중간위치에 있는 메뉴에 서브 카테고리 전체
        
        subcategory_lists = response.css('div.sub_category_box li a::attr("onclick")').re('\(.*\)')
        subcategory_idcs = []
        for i in subcategory_lists:
            if i[2] == ',':
                subcategory_idcs.append((int(i[1]),int(i[3:-1])))
            else:
                subcategory_idcs.append((int(i[1:3]),int(i[4:-1])))
        
        for idx, sub in enumerate(subcategory_idcs):
            if sub[0] == response.meta['index']:
                yield scrapy.Request(url="https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&cornerNo=" + str(sub[0]) + "&dispCtgrNo=" + str(sub[1]), 
                                     callback=self.parse_items,
                                     meta={'maincategory_name':response.meta['maincategory_name'], 
                                                                      'subcategory_name':subcategory_names[idx]}
                                    )
            else:
                continue

    def parse_items(self, response):
        print('parse_items', response.meta['maincategory_name'], response.meta['subcategory_name']) #확인용
        best_items = response.css('div.viewtype.catal_ty')

        for idx, item in enumerate(best_items[1].css('li')): 
                                                            
            doc = Market11Item()        
            ranking = idx + 1 
            title = item.css(' div.box_pd.ranking_pd a div.pname p::text').get().strip() 
            ori_price = item.css(' div.box_pd.ranking_pd a div.pname div.price_info.cfix span.price_detail s::text').get()
            dis_price = item.css(' div.box_pd.ranking_pd a div.pname div.price_info.cfix span.price_detail strong.sale_price::text').get()
            
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