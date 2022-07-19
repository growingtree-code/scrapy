
BOT_NAME = 'market_11'

SPIDER_MODULES = ['market_11.spiders']
NEWSPIDER_MODULE = 'market_11.spiders'
# DOWNLOAD_DELAY = 1
ROBOTSTXT_OBEY = False
FEED_EXPORT_ENCODING = 'cp949'#or utf-8 한글깨질경우

#settings.py
ITEM_PIPELINES = {
    'st11.pipelines.St11Pipeline': 300,     # 숫자(0 ~ 1000 입력)는 Pipeline의 적용 순서를 의미
}                                           # 숫자가 작은 것부터 차례대로 적용됨