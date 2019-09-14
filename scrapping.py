# -*- coding: utf-8 -*-
import scrapy


class ReviewSpider(scrapy.Spider):   
    # Spider name
    name = 'amazon_reviews'
     
    # Domain names to scrape
    allowed_domains = ['amazon.in']
     
    # Base URL for the reviews
    myBaseUrl = "https://www.amazon.in/Forever-Living-Aloe-Vera-Gel/product-reviews/B00IEFJSQK/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber="
    start_urls=[]
    
    # Creating list of urls to be scraped by appending page number a the end of base url
    for i in range(1,43):
        start_urls.append(myBaseUrl+str(i))
    
    # Defining a Scrapy parser
    def parse(self, response):
            data = response.css('#cm_cr-review_list')
             
            # Collecting product star ratings
            star_rating = data.css('.review-rating')
             
            #Collecting review header
            header = data.css('.review-title')
            
            # Collecting user reviews
            comments = data.css('.review-text')
            count = 0
             
            # Combining the results
            for review in star_rating:
                yield{'Rating': ''.join(''.join(review.xpath('.//text()').extract()).replace('out of 5 stars','')),
                      'Title':''.join(header[count].xpath(".//text()").extract()),
                      'Comment': ''.join(comments[count].xpath(".//text()").extract())
                     }
                count=count+1
