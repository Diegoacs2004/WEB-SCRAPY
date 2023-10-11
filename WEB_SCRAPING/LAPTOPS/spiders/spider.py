import scrapy
from scrapy.exceptions import CloseSpider
from scrapy.spiders import Spider, Rule
from scrapy.linkextractors import LinkExtractor
from LAPTOPS.items import ProyectoScrapyItem

class LaptopSpider(scrapy.Spider):
    name = 'laptop'
    item_count = 0 #Para no escrapear cantidad e products, como un filtro.
    allowed_domain =['https://www.loginstore.com/'] #Permitir toda la info dentro del dominio
    start_urls = ['https://www.loginstore.com/computacion/laptops/laptops'] #Donde va a empezar a hacer el scrapy, se puede agregar mas urls agregando una coma

    rules = (
        Rule(LinkExtractor(allow =(), restrict_xpaths=('//li[@class = "item"]/a'))),
        Rule(LinkExtractor(allow =(), restrict_xpaths=('//h2[@class="ui-search-item__title"]')),
                            callback = 'parse.item', follow = False),
    )
    def parse_item(self, response): # Encargado de extraer los datos de la página web
        ml_item = LaptopSpider() # Instancia del Spider
        
        #info de producto, extracción de Datos Utilizando XPath:
        #ml_item['titulo'] = response.xpath('...').extract_first().strip()
        #ml_item, diccionario, se almacena en los campos
        ml_item['titulo'] = response.xpath('normalize-space(//*[@id="product_addtocart_form"]/div[3]/div[1]/h1)').extract()
        ml_item['codigo'] = response.xpath('normalize-space(//*[@id="product_addtocart_form"]/div[3]/div[1]/p[1]').extract()
        ml_item['descripcion'] = response.xpath('normalize-space(//*[@id="product_addtocart_form"]/div[3]/div[2]/div').extract()
        ml_item['precio'] = response.xpath('normalize-space(//*[@id="product_addtocart_form"]/div[3]/div[3]/div)').extract()
        ml_item['stock'] = response.xpath('normalize-space(//*[@id="product_addtocart_form"]/div[3]/div[5]/span)').extract()
        ml_item['plazo'] = response.xpath('normalize-space(//*[@id="product_addtocart_form"]/div[3]/strong').extract()
        self.item_count += 1
        if self.item_count> 20:
            raise CloseSpider('item_exceeded')
        yield ml_item
