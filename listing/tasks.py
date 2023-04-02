from celery import shared_task

from scrapers.spiders.basic import BasicSpider
from .models import Listing

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

import logging

@shared_task(name='crawl')
def crawl(listing_id, crawl_url, selector):
    # logger = logging.getLogger('django')

    # logger.info('crawl task starting...')
    print('crawl task starting...')

    process = CrawlerProcess(settings=get_project_settings())

    process.crawl(BasicSpider, listing_id=listing_id, crawl_url=crawl_url, selector=selector)
    process.start(stop_after_crawl=False) # the script will block here until the crawling is finished

@shared_task(name='test_task')
def test_task(listing_id):
    print('task starting...')