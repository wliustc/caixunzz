#-*-coding=utf-8-*-
import scrapy,codecs
from caixunzz.items import CaixunzzItem
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
    name="cnbeta"
    start_urls=["http://www.caixunzz.com/?post=611"]

    def parse(self, response):
        #self.log("A response received from %s" % response.url)
        print "A response recevived from %s " %response.url
        feedback=response.xpath('//a/@href').extract()

        print "*"*10

        for i in feedback:
            #yield scrapy.Request(i,callback=self.parse)
            if i != "#":
                print i
        print "*"*20
        print "End"