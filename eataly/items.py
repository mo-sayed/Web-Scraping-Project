# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EatalyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    RestName = scrapy.Field()
    Rating = scrapy.Field()
    # Cuisine = scrapy.Field()
    Dollar_sign = scrapy.Field()
    Nbr_reviews = scrapy.Field()
    City = scrapy.Field()
