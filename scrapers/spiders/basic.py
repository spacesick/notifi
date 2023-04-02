import scrapy
import mmh3

from listing.models import Listing

from difflib import Differ

from scrapy.mail import MailSender

import logging


class BasicSpider(scrapy.Spider):
    # name = "basic"
    # start_urls = [
    #     'https://scele.cs.ui.ac.id/',
    # ]
    

    def __init__(self, listing_id, url, selector, *args, **kwargs):
        super(BasicSpider, self).__init__(*args, **kwargs)
        self.id = listing_id
        self.name = listing_id
        self.url = url
        self.selector = selector
        self.emailer = MailSender()

        logger = logging.getLogger('django')
        logger.info('spider initializing...')

    def start_requests(self):
        logger = logging.getLogger('django')
        logger.info('spider starting requests...')
        yield scrapy.Request(url=self.url, callback=self.parse)

    def parse(self, response):
        logger = logging.getLogger('django')
        logger.info('spider parsing...')

        html = response.css(self.selector).getall()
        html_hash = mmh3.hash(html, 99)
        listing = Listing.objects.get(id=self.id)

        if listing.content_hash != html_hash:
            listing.user.email_user(
                '[Notifi] There has been a change',
                'Some body',
                'notifi@noreply.com'
            )
            listing.content_hash = html_hash

        yield {
            'text': response.css(self.selector).getall()
        } 

    def send_email_to(self, email):
        logger = logging.getLogger('django')
        logger.info(f'spider emailing to {email}...')

        self.emailer.send(
            to=[email], 
            subject="[Notifi] There has been a change", 
            body="Some body", 
        )

