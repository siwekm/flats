import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.signalmanager import dispatcher
from scrapy import signals
from srealityScrapper.srealityScrapper.spiders.sreality import SrealitySpider
from DBManager.DBManager import DBManager


def add_flat(signal, sender, item, response, spider):
    flatsDB.insert_flat(item)


def scrap():
    dispatcher.connect(add_flat, signal=scrapy.signals.item_scraped)
    process = CrawlerProcess()
    process.crawl(SrealitySpider)
    process.start()


if __name__ == '__main__':
    flatsDB = DBManager()
    flatsDB.create_table()
    scrap()
    flatsDB.close()
