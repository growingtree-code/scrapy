import scrapy

class Market11Item(scrapy.Item):

    ranking = scrapy.Field()               # 상품 순위
    main_category_name = scrapy.Field()    # 메인 카테고리명
    sub_category_name = scrapy.Field()     # 서브 카테고리명
    title = scrapy.Field()                 # 상품명
    ori_price = scrapy.Field()             # 기존 가격
    dis_price = scrapy.Field()             # 할인 가격

    pass
