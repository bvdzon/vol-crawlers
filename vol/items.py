# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    text = scrapy.Field()
    labels = scrapy.Field()
    city = scrapy.Field()
    region = scrapy.Field()
    country = scrapy.Field()
    sites = scrapy.Field()
    organisation = scrapy.Field()
    organisation_id = scrapy.Field()
    organisation_url = scrapy.Field()
    site_name = scrapy.Field()
    site_url = scrapy.Field()
    api_url = scrapy.Field()


class OrganisationItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    description = scrapy.Field()
    city = scrapy.Field()
    region = scrapy.Field()
    country = scrapy.Field()


class SiteItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
