
BOT_NAME = 'market_11'

SPIDER_MODULES = ['market_11.spiders']
NEWSPIDER_MODULE = 'market_11.spiders'
# DOWNLOAD_DELAY = 1
ROBOTSTXT_OBEY = False
FEED_EXPORT_ENCODING = 'cp949'#or utf-8 한글깨질경우
DUPEFILTER_CLASS = 'scrapy.dupefilters.BaseDupeFilter' #비슷한 주소로 요청하는 코드가 여러개여도 모두 실행 될 수 있게
#settings.py
# ITEM_PIPELINES = {
#     'market_11.pipelines.Market_11Pipeline': 300,     # 숫자(0 ~ 1000 입력)는 Pipeline의 적용 순서를 의미
# }                                           # 숫자가 작은 것부터 차례대로 적용됨