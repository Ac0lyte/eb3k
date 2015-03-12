# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

# Snippet imported from snippets.scrapy.org (which no longer works)
# and later found on http://snipplr.com/
# author: redtricycle
# date  : Nov 21, 2011


from twisted.enterprise import adbapi
import datetime
import MySQLdb.cursors

from scrapy.conf import settings
from scrapy import log

# Loads the page link and spiders that pulling out the image and link.
class eb3kPagePipeline(object):
    def process_item(self, item, spider):
        item['url'] = item['url'].rstrip('/')
        return item


# Inserts the item into the MySQL DB
class eb3kMySQLPipeline(object):

    def __init__(self):
        self.dbpool = adbapi.ConnectionPool( 'MySQLdb', host=settings['MYSQL_HOST'], db=settings['MYSQL_DB'],
                user=settings['MYSQL_USER'], passwd=settings['MYSQL_PASS'], cursorclass=MySQLdb.cursors.DictCursor,
                charset='utf8', use_unicode=True)
        log.msg("Did we connect to the DB? In theory YES!", level=log.DEBUG)
 
    def process_item(self, item, spider):
        # run db query in thread pool
        log.msg("Attempting to add an item to the DB", level=log.DEBUG)
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        query.addErrback(self.handle_error)
 
        return item
 
    def _conditional_insert(self, tx, item):
        # create record if doesn't exist. 
        # all this block run on it's own thread
        log.msg("Checking for item in db: ", level=log.DEBUG)
        tx.execute("select * from items where title = %s", (item['title'][0], ))
        result = tx.fetchone()
        if result:
            log.msg("Item already stored in db:", level=log.DEBUG)
        else:
            log.msg("Storing item in db: ", level=log.DEBUG)
            tx.execute(\
                "insert into items (url, title, link, thumb, page, image, date) "
                "values (%s, %s, %s, %s, %s, %s, %s)",
                (item['url'], 
                 item['title'][0], 
                 item['link'][0], 
                 item['thumb'][0], 
                 item['page'][0], 
                 item['image'][0],
                 datetime.datetime.now() )
            )
            log.msg("Item stored in db:", level=log.DEBUG)
 
    def handle_error(self, e):
        log.err(e)
 

