import scrapy


class SrealitySpider(scrapy.Spider):
    name = "sreality"

    def start_requests(self):
        urls = [
            'https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&page=1&per_page=5',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        for flat in response.json().get('_embedded').get('estates'):
            yield{
                    'title': flat.get('name'),
                    'image_url': flat.get('_links').get('images')[0].get('href'),
                }
