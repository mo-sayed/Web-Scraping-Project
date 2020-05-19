from scrapy import Spider, Request
from eataly.items import EatalyItem

class eataly(Spider):
    name = "eataly_spider"
    allowed_urls = ['https://www.yelp.com/']
    start_urls = [('https://www.yelp.com/search?find_desc=italian&find_loc=seattle%20wa&ns=1&start=0')]

    def parse(self, response):
    # the parse function is for nagivating through the different pages of yelp reviews for the 300 most review 
    # Italian/Pizza/Mediterranean restaurants within each of the potential cities

        #Starting with Italian restaurants in Seattle WA, San Francisco CA, Austin TX, Washington DC, San Jose CA, Miami FL
        potential_cities = ['Seattle WA', 'San Francisco CA', 'Austin TX', 'Washington DC', 'San Jose CA', 'Miami FL']   
        # potential_cities --> Cities to consider based on comparison of income/population/density with current Eataly locations
        potential_cities_url = []         # link for all the potential cities
        yelp_pages_url = []               # link for all the yelp pages of potential cities
        potential_cities_split = []       # potential cities split into nested lists to use for searching cities within the url
        potential_cities_format = 'https://www.yelp.com/search?find_desc=Restaurants&find_loc={}&sortby=review_count&cflt=italian%2Cpizza%2Cmediterranean&start={}'
        # input location and review number start(multiples of 30) using below

        for i in potential_cities:
            potential_cities_split.append(i.split(" "))
            # print("First for loop", '-'*80)
        for j in potential_cities_split:
            if len(j)==2:
                potential_cities_url.append(j[0] + '%2C%20' + j[1])
                # print("First if ", '-'*80)
            if (len(j)==3):
                potential_cities_url.append(j[0] + '%20' + j[1] + '%2C%20' + j[2])
                # print("Second if ", '-'*80)
            if (len(j)==4):
                potential_cities_url.append(j[0] + '%20' + j[1] + '%20' + j[2] + '%2C%20' + j[3])
                # san%20luis%20obispo%20california
        # print(potential_cities_url, '*'*80)

        for m in potential_cities_url:
            # print('Test here above range of 0 to 150', '$'*50)
            for n in range(0,151,30):
                # print('Test here above cities_url append', '&'*50)
                yelp_pages_url.append(potential_cities_format.format(m,n))
                # print(potential_cities_format.format(m,n))
                # print(yelp_pages_url)
                # print('2nd for loop', '-'*80)
            # print('3rd for loop', '-'*80)

        for url in yelp_pages_url:
            yield Request(url=url, callback = self.parse_output)
            # print('last for loop', '-'*80)

    def parse_output(self, response):
        rows = response.xpath('//div[@class="lemon--div__373c0__1mboc arrange__373c0__2C9bH border-color--default__373c0__3-ifU"]').extract()
        for row in rows[2:]:
            RestName = response.xpath('//span[@class="lemon--span__373c0__3997G text__373c0__2Kxyz text-color--black-regular__373c0__2vGEn text-align--left__373c0__2XGa- text-weight--bold__373c0__1elNz text-size--inherit__373c0__2fB3p"]/a/text()').extract()
            Rating = response.xpath('//div[@class="lemon--div__373c0__1mboc attribute__373c0__1hPI_ display--inline-block__373c0__1ZKqC margin-r1__373c0__zyKmV border-color--default__373c0__3-ifU"]/span/div/@aria-label').extract()
            Dollar_sign = response.xpath('//div[@class="lemon--div__373c0__1mboc border-color--default__373c0__3-ifU"]/span/span/text()').extract()
            Nbr_reviews = " ".join(response.xpath('//*[@class="lemon--span__373c0__3997G text__373c0__2Kxyz reviewCount__373c0__2r4xT text-color--black-extra-light__373c0__2OyzO text-align--left__373c0__2XGa-"]/text()').extract())
            City = response.xpath('//div[@class="lemon--div__373c0__1mboc border-color--default__373c0__3-ifU overflow--hidden__373c0__2y4YK"]/input/@value').extract()
            # Cuisine = response.xpath('//span[@class="lemon--span__373c0__3997G text__373c0__2Kxyz text-color--black-extra-light__373c0__2OyzO text-align--left__373c0__2XGa-"]/a/text()').extract()

        item = EatalyItem()

        item['RestName'] = RestName
        item['Rating'] = Rating
        item['Dollar_sign'] = Dollar_sign
        item['Nbr_reviews'] = Nbr_reviews
        item['City'] = City
        # item['Cuisine'] = Cuisine
        
        yield item
