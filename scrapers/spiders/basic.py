import scrapy
import mmh3

from listing.models import Listing

import difflib

from scrapy.mail import MailSender

import logging

from asgiref.sync import sync_to_async

from bs4 import BeautifulSoup


class BasicSpider(scrapy.Spider):
    name = "basic"

    def __init__(self, listing_id, crawl_url, selector, *args, **kwargs):
        super(BasicSpider, self).__init__(*args, **kwargs)
        self.id = listing_id
        self.crawl_url = crawl_url
        self.selector = selector

        logger = logging.getLogger('django')
        logger.info('spider initializing...')
        print('spider initializing...')

    def start_requests(self):
        logger = logging.getLogger('django')
        logger.info('spider starting requests...')
        print('spider starting requests...')
        yield scrapy.Request(url=self.crawl_url, callback=self.parse)

    async def parse(self, response):
        logger = logging.getLogger('django')
        logger.info('spider parsing...')
        print('spider parsing...')

        html = response.css(self.selector).get()
        html_hash = mmh3.hash(html, 99)
        listing = await Listing.objects.aget(id=self.id)

        print(f'GOT HASH {html_hash}')

        if listing.content_hash == None:
            listing.content = html
            listing.content_hash = html_hash
            await self.save_listing(listing)
        elif listing.content_hash != html_hash:
            parsed_old_html = list(BeautifulSoup(listing.content, 'lxml').stripped_strings)
            parsed_new_html = list(BeautifulSoup(html, 'lxml').stripped_strings)
            diff = difflib.HtmlDiff().make_file(
                fromlines=parsed_old_html,
                tolines=parsed_new_html
            )

            user = await self.get_listing_user(listing)
            user.email_user(
                subject=f'[webobsrv] Change on {self.crawl_url}',
                message=f'This is to notify you that there has been a change on {self.crawl_url}',
                from_email='webobsrv@gmail.com',
                html_message=diff
            )

            listing.content = html
            listing.content_hash = html_hash
            await self.save_listing(listing)

        yield {
            'html': html
        } 

    @sync_to_async
    def get_listing_user(self, listing):
        return listing.user
    
    @sync_to_async
    def save_listing(self, listing):
        listing.save()