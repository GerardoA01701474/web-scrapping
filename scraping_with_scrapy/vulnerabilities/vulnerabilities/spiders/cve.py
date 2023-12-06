import scrapy
import os 
from os.path import dirname, join
import csv, json


current_dir = dirname(__file__)
url = join(current_dir, 'source-EXPLOIT-DB.html')

class CveSpider(scrapy.Spider):
    name = "cve"
    allowed_domains = ["cve.mitre.org"]
    #start_urls = ["https://cve.mitre.org/data/refs/refmap/source-EXPLOIT-DB.html"] #from web
    start_urls = [f"file://{url}"] #from local

    def parse(self, response):
        for child in response.xpath('//table'):
            if len(child.xpath('tr'))>100:
                table = child
                break
        count = 0
        data = {}
        #csv_file = open('vulnerabilities.csv', 'w')
        json_file = open('vulnerabilities.json', 'w')
        #writer = csv.writer(csv_file)
        #writer.writerow(['exploit id', 'cve id'])

        for row in response.xpath('//tr'):
            try:
                explot_id = row.xpath('td//text()')[0].extract()
                cve_id = row.xpath('td//text()')[2].extract()
                data[explot_id] = cve_id 
                #writer.writerow(explot_id, cve_id)
                count += 1
            except IndexError:
                pass
        #csv_file.close()
        json.dump(json_file)
        json_file.close()