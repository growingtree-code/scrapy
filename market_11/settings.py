
BOT_NAME = 'market_11'

SPIDER_MODULES = ['market_11.spiders']
NEWSPIDER_MODULE = 'market_11.spiders'
# DOWNLOAD_DELAY = 1
ROBOTSTXT_OBEY = False
FEED_EXPORT_ENCODING = 'cp949'#or utf-8 한글깨질경우
DUPEFILTER_CLASS = 'scrapy.dupefilters.BaseDupeFilter' #비슷한 주소로 요청하는 코드가 여러개여도 모두 실행 될 수 있게

ITEM_PIPELINES = {
    'market_11.pipelines.Market11Pipeline': 300,
}                                        
FEED_EXPORT_FIELDS = ['main_category_name', 'sub_category_name', 'ranking', 'title', 'ori_price', 'dis_price']   