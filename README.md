# Notifi

A 1-day web app project for watching changes in other websites by scraping HTML elements and notifying users asynchronously by email. I originally used this to notify myself of announcements from my university e-learning website. If you want to use this yourself, you need to setup an email for this app to use for sending emails.

The web app uses Django for authentication and sending emails, Scrapy for web scraping, Celery for managing web scraping workers, and Redis for scheduling and queuing those workers.
