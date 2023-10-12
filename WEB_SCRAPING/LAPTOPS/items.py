# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProyectoScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    #info de producto, dato específico que planeas extraer de la página web.
    titulo = scrapy.Field()
    precio = scrapy.Field()
    plazo = scrapy.Field()
    stock= scrapy.Field()
    descripcion= scrapy.Field()
    codigo= scrapy.Field()
