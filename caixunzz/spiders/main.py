#-*-coding=utf-8-*-
import scrapy,codecs
from caixunzz.items import CaixunzzItem,CnbetaItem
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
class Caixun(scrapy.Spider):

    name="caixunzz"
    allowed_domains=["caixunzz.com"]
    start_urls=['http://www.caixunzz.com']

    def parse(self, response):
        #print response.body
        #just make sure it works
        #title=response.xpath('//title/text()').extract()
        #print "below is title"
        #print title[0]
        print "#"*10
        print "start to scrapy"
        print "#"*10

        data=response.xpath('//h2')
        date=response.xpath('//p[contains(@class,"date")]/text()').extract()
        link=response.xpath('//h2/a[2]/@href').extract()
        print link
        '''
        for i in link:
            print i
        '''
        #below has issue, not working , why so  ??

        #date=response.css('.date')
        date_list=[]

        for j in date:
            #item=CaixunzzItem()
            #item['date']=j.strip()
            if j.strip()!='':
                date_list.append(j.strip())
            #print j.strip()

            #print j.xpath('//text()').extract()
        #print data


        data_list=[]
        count=0
        for i in data.xpath('a/text()'):

            if count%2!=0:
                #item['date']=i.extract()
                #print i.extract()
                #print i.strip()
                data_list.append(i.extract())

            count=count+1

            #print type(i)
            #print i.extract()
            #print i.xpath('a/text()').extract()

        items=[]

        f=codecs.open("news.txt",'w','utf-8')


        #for (i,j) in (date_list,data_list):
        for i in range(len(data_list)):
            item=CaixunzzItem()
            item['date']=date_list[i]
            item['data']=data_list[i]
            item['link']=link[i]
            print item['date'],item['data'],item['link']
            f.write(item['date']+'\t')
            f.write(item['data']+'\t')
            f.write(item['link']+'\t')

            f.write('\n')
            items.append(item)
        '''
            for j in i:
                print j
        '''
        print "len of data %d and date %d and link %d" %(len(data_list),len(date_list),len(link))
        print "#"*10
        print "end to scrapy"
        print "#"*10
        '''
        for a in data_list:
            print a
        for b in date_list:
            print b
        '''
        f.close()
        #return items


class TestSpider(scrapy.Spider):
    #For testing purpose
    name="qq"
    start_urls=["http://www.qq.com"]

    def parse(self, response):
        #self.log("A response received from %s" % response.url)
        print "A response recevived from %s " %response.url
        feedback=response.xpath('//a/@href').extract()

        print "*"*10
        print "how much href %d" %len(feedback)
        for i in feedback:
            #yield scrapy.Request(i,callback=self.parse)
            if i != "#":
                print i
                yield scrapy.Request(i,callback=self.parse)
        print "*"*20
        print "End"

class CnbetaSpider(CrawlSpider):

    '''
    this can run properly
    '''
    name='cnbeta'
    allowed_domains=['cnbeta.com']
    start_urls=['http://www.cnbeta.com']
    rules = (Rule(SgmlLinkExtractor(allow=('/articles/.*\.htm')),callback='parse_page',follow=True),
             )
    #Rule(LinkExtractor(allow=('/articles/\d+\.htm',)),callback='parse',follow=True)

    def parse_page(self,response):
        item=CnbetaItem()
        print "Current Date: %s" %d
        item['title']=response.xpath('//title/text()').extract()
        item['url']=response.url
        print "*"*10
        print item['title']
        print item['url']
        return item