BOT_NAME = 'eataly'

SPIDER_MODULES = ['eataly.spiders']
NEWSPIDER_MODULE = 'eataly.spiders'

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'

ROBOTSTXT_OBEY = False

DOWNLOAD_DELAY = 3

ITEM_PIPELINES = {
   'eataly.pipelines.EatalyPipeline': 100,
}
