# Import modules
import scrapy
from scrapy.crawler import CrawlerProcess

# Define the spider
class MySpider(scrapy.Spider):
    name = "MySpider"
    
    def start_requests(self):
        urls = ["https://taxiliz.com/?lang=fr"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
            
    def parse(self, response):
        page_content = response.css('body').extract_first()
        yield {'content': page_content}

# Run the spider
process = CrawlerProcess()
process.crawl(MySpider)
process.start()

# Save the output to a file
with open("summary.txt", "w") as file:
    file.write(str(MySpider))

