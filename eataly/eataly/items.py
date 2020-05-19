import scrapy


class EatalyItem(scrapy.Item):
    
    RestName = scrapy.Field()
    Rating = scrapy.Field()
    Dollar_sign = scrapy.Field()
    Nbr_reviews = scrapy.Field()
    City = scrapy.Field()
    # Cuisine = scrapy.Field()