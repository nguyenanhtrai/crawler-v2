import scrapy
from scrapy.item import Item, Field

class ImageItem(Item):
    type = Field()
    id_info_ebook = Field()
    folderGG = Field()
    image_url = Field()
    images = Field()
