# crawler-rss-feed
Crawler for the rss feed [http://revistaautoesporte.globo.com/rss/ultimas/feed.xml](http://revistaautoesporte.globo.com/rss/ultimas/feed.xml).


# Install requirements

```
	$ pip install -r requirements.txt
```

# Usage


## Using the custom feed reader


```
	$ python crawler_rss_feed.py
{'feed': [{'item': {'link': 'http://revistaautoesporte.globo.com/Noticias/noticia/2017/03/ssangyong-antecipa-imagens-do-seu-jipao-de-luxo.html', 'content': [{'content': 'http://s2.glbimg.com/_9UjXU-aqsj89WB_78lm0sDje-Y=/620x413/e.glbimg.com/og/ed/f/original/2017/03/24/suvsssangyong.jpg', 'type': 'image'}, {'content': 'A SsangYong apresentou imagens iniciais do seu novo utilitário topo de linha, chamado pelo nome projeto de Y400. O carro será apresentado no Salão de Seul e terá linhas parecidas com as do conceito LIV-2, apresentado em setembro último no Salão de Paris. O carro será um substituto na prática para defasado Rexton, lembrando que desde o conceito LIV-1 de 2013 que a marca promete substituir o utilitário lançado originalmente no muito distante ano de 2001.', 'type': 'text'}, {'content': 'As vendas começarão ainda no primeiro semestre de 2017 e o SUV será vendido em outros mercados até o final deste ano. Contudo, a marca sul-coreana deixou de ter representação no Brasil faz quase dois anos, então o Y400 está mais do que distante daqui.', 'type': 'text'}, {'content': ['http://revistaautoesporte.globo.com/Noticias/noticia/2017/02/ssangyong-levara-conceito-de-sete-lugares-ao-salao-de-genebra.html', 'http://revistaautoesporte.globo.com/Noticias/noticia/2016/02/ssangyong-revela-siv-2-previa-de-novo-suv-grande.html', 'http://revistaautoesporte.globo.com/Noticias/noticia/2013/03/ssangyong-revela-imagens-do-conceito-liv-1.html'], 'type': 'links'}, {'content': 'Será um utilitário mesmo, sem trejeitos de crossover. Para começar, a tração é traseira com 4X4 temporária.\xa0 A estrutura utiliza 63% de aços de altaresistência, algo que ajudou também na diminuição de peso, segundo a SsangYong.', 'type': 'text'}, {'content': 'http://s2.glbimg.com/5OY422mqv-HQ5zwNsKpMh8fgHNI=/e.glbimg.com/og/ed/f/original/2017/03/24/painelssangyong.jpg', 'type': 'image'}, {'content': 'O porte é próximo do Chevrolet Trailblazer, são 4,85 metros de comprimento e 2,86 metros de distância entre-eixos, enquanto o GM tem 4,88 m e 2,84 m nas mesmas medidas. A SsangYong ainda não divulgou mais dados mecânicos, apenas afirmou que o Y400 contará com motores a diesel e gasolina de baixas emissões.', 'type': 'text'}], 'title': 'SsangYong antecipa imagens do seu jipão de luxo'}}, {'item':
```

Save items to json file 'autoesporte.json'
```
	$ python crawler_rss_feed.py -o autoesporte.json
```

## Using default scrapy library
Notice that the default scrapy library only returns items indepently, it does not aggregate them in a single json.

```
	$ scrapy crawl autoesporte
2017-03-24 16:22:09 [scrapy.core.engine] DEBUG: Crawled (200) <GET http://revistaautoesporte.globo.com/rss/ultimas/feed.xml> (referer: None)
2017-03-24 16:22:09 [scrapy.core.scraper] DEBUG: Scraped from <200 http://revistaautoesporte.globo.com/rss/ultimas/feed.xml>
{'link': 'http://revistaautoesporte.globo.com/Noticias/noticia/2017/03/ssangyong-antecipa-imagens-do-seu-jipao-de-luxo.html', 'title': 'SsangYong antecipa imagens do seu jipão de luxo', 'content': [{'type': 'image', 'content': 'http://s2.glbimg.com/_9UjXU-aqsj89WB_78lm0sDje-Y=/620x413/e.glbimg.com/og/ed/f/original/2017/03/24/suvsssangyong.jpg'}, {'type': 'text', 'content': 'A SsangYong apresentou imagens iniciais do seu novo utilitário topo de linha, chamado pelo nome projeto de Y400. O carro será apresentado no Salão de Seul e terá linhas parecidas com as do conceito LIV-2, apresentado em setembro último no Salão de Paris. O carro será um substituto na prática para defasado Rexton, lembrando que desde o conceito LIV-1 de 2013 que a marca promete substituir o utilitário lançado originalmente no muito distante ano de 2001.'}, {'type': 'text', 'content': 'As vendas começarão ainda no primeiro semestre de 2017 e o SUV será vendido em outros mercados até o final deste ano. Contudo, a marca sul-coreana deixou de ter representação no Brasil faz quase dois anos, então o Y400 está mais do que distante daqui.'}, {'type': 'links', 'content': ['http://revistaautoesporte.globo.com/Noticias/noticia/2017/02/ssangyong-levara-conceito-de-sete-lugares-ao-salao-de-genebra.html', 'http://revistaautoesporte.globo.com/Noticias/noticia/2016/02/ssangyong-revela-siv-2-previa-de-novo-suv-grande.html', 'http://revistaautoesporte.globo.com/Noticias/noticia/2013/03/ssangyong-revela-imagens-do-conceito-liv-1.html']}, {'type': 'text', 'content': 'Será um utilitário mesmo, sem trejeitos de crossover. Para começar, a tração é traseira com 4X4 temporária.\xa0 A estrutura utiliza 63% de aços de altaresistência, algo que ajudou também na diminuição de peso, segundo a SsangYong.'}, {'type': 'image', 'content': 'http://s2.glbimg.com/5OY422mqv-HQ5zwNsKpMh8fgHNI=/e.glbimg.com/og/ed/f/original/2017/03/24/painelssangyong.jpg'}, {'type': 'text', 'content': 'O porte é próximo do Chevrolet Trailblazer, são 4,85 metros de comprimento e 2,86 metros de distância entre-eixos, enquanto o GM tem 4,88 m e 2,84 m nas mesmas medidas. A SsangYong ainda não divulgou mais dados mecânicos, apenas afirmou que o Y400 contará com motores a diesel e gasolina de baixas emissões.'}]}
```

Save items to json file 'autoesporte.json'
```
	$ scrapy crawl autoesporte -o autoesporte.json
```


# API
Start server:

```
	$ python autoesporte_api.py
```

Requesting json feed:
```
	$ curl -u user1:pass1 http://127.0.0.1:5000/autoesporte/feed
{
  "feed": [
    {
      "item": {
        "content": [
          {
            "content": "N\u00e3o conseguiu acompanhar todas as not\u00edcias do mundo dos carros durante a semana? Tudo bem, separamos as mais legais para voc\u00ea ler no final de semana. Assista no v\u00eddeo acima o bate-papo que acontece todas as semanas sobre as not\u00edcias dos \u00faltimos dias.", 
            "type": "text"
          },
```

```
	$ curl -u user1:wrongpass http://127.0.0.1:5000/autoesporte/feed 
{
  "error": "Unauthorized access"
}

```




# Testing

Test crawler
```
	$ python -m crawler.tests
...........
----------------------------------------------------------------------
Ran 11 tests in 0.067s

OK
```

Test autoesporte crawler
```
	$ python -m crawler.tests.autoesporte
...........
----------------------------------------------------------------------
Ran 11 tests in 0.067s

OK
```

Verbose test
```
	$ python -m unittest -v crawler.tests

test_chalenge_example (crawler.tests.autoesporte.AutoEsporteSpiderTest) ... ok
test_content (crawler.tests.autoesporte.AutoEsporteSpiderTest) ... ok
test_empty_content (crawler.tests.autoesporte.AutoEsporteSpiderTest) ... ok
test_empty_link (crawler.tests.autoesporte.AutoEsporteSpiderTest) ... ok
test_empty_title (crawler.tests.autoesporte.AutoEsporteSpiderTest) ... ok
test_image (crawler.tests.autoesporte.AutoEsporteSpiderTest) ... ok
test_link (crawler.tests.autoesporte.AutoEsporteSpiderTest) ... ok
test_links (crawler.tests.autoesporte.AutoEsporteSpiderTest) ... ok
test_multiple_items (crawler.tests.autoesporte.AutoEsporteSpiderTest) ... ok
test_text (crawler.tests.autoesporte.AutoEsporteSpiderTest) ... ok
test_title (crawler.tests.autoesporte.AutoEsporteSpiderTest) ... ok

----------------------------------------------------------------------
Ran 11 tests in 0.077s

OK
```



# Comments

The core of the crawler was implemented in the file [crawler/spiders/autoesporte.py](crawler/spiders/autoesporte.py)  extending the XMLFeedSpider class from Scrapy.

The libraries [Scrapy](https://scrapy.org/) and [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)  were used to parse the responses.

The tests where implemented in the file [crawler/tests/autoesporte.py](crawler/tests/autoesporte.py) using 	the default unit testing framework from Python [unittest](https://docs.python.org/3/library/unittest.html).

The package Flask was used to setup the webservice and the authentication was made with the Flask-HTTPAuth extension.