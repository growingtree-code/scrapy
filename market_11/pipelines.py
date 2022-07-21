#데이터 후저리 부분
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

class Market11Pipeline:
    def process_item(self, item, spider):
        if int(item['ranking'])<=5:
            return item
        else:
            raise DropItem("순위권 밖",item)
        return item
