import scrapy


class NicolsspiderSpider(scrapy.Spider):
    name = "nicolsSpider"

    custom_settings = {
        'FEED_URI': 'nicols_Data.csv',
        'FEED_FORMAT': 'csv'
    }

    cookies = {
        'PHPSESSID': 'krnpi95fkqnobtht97egcv6vj3',
        'PrestaShop-8aec7a5722627e6b2ad96140ea4d655d': 'def502009f4fa9378ff20c8c7153d7e29dbc9adfd54cc164c6edf7c6d18a60c9805effede39f7d0cf3685b1594942148b7760f8cce504f71d7d7d7384a20891368c5740d64bbf079c10ffc2f93ccf66a5ffcaba62aa8d7f9a6911da40094e463ca9644ab2db703a33bbbc3c35c1e1c0b012f0e38cd4b88316388c6ecaa576c193b79f10052904ab967cc10f10468d05df3c0ab8642e5f643240aa08cd39229c347c0e6c47489a0d2092435dacfe87da13450070d7fda11aa24b080af37a6e32fbc9576dce1c7b6c964d6dfcd134a5e91525af573ac95ead2d6ae30c90620f792405aa2dcfbcd4a8fbd77ffaa2ff5e0a6e3ff866acc8662ee3b504845b385c5accac1c1ee5e5119fccdccdf2dce7a2dbb021bb0feb79998d9d60e2cb7833817287d23fb82facb39615f00b74000560f',
        '_gcl_au': '1.1.10390569.1713381805',
        '_ga': 'GA1.1.396208300.1713381809',
        '_clck': 'ymhafp%7C2%7Cfl0%7C0%7C1568',
        'cf_clearance': 'Gi8_y9w2zkiVktKk2_lcKCfE_NUx2jgp0LF3Gl9kws8-1713381857-1.0.1.1-hN7GzYxL.j6KWcp09ZwsCWM9VeDFo6dMrTvF5SWwtKld0QU0oeODK3.BrfWpaW_Glw0edHg82kzrxiIl_ksHYA',
        '__stripe_mid': 'f889d6c1-5a40-4767-9093-13af5a5519308bd99e',
        '__stripe_sid': 'c66f8a13-2a7e-465d-8b7f-36af025d570082e28c',
        '_fbp': 'fb.1.1713381881167.1311298085',
        'cookiesplus': '%7B%22C_P_DISPLAY_MODAL%22%3Afalse%2C%22cookiesplus-finality-3%22%3A%22on%22%2C%22cookiesplus-finality-4%22%3A%22on%22%2C%22consent_date%22%3A%222024-04-17%2021%3A24%22%2C%22consent_hash%22%3A%224c475d251b8267148c18a64202f90fe3-31fb5c87%22%7D',
        '_clsk': '1g0szb2%7C1713382368447%7C5%7C1%7Cm.clarity.ms%2Fcollect',
        '_ga_KF7FBSMZWH': 'GS1.1.1713381809.1.1.1713382373.46.0.0',
        '_uetsid': '1927c2f0fcf011eeb7c21ffefefdb30e',
        '_uetvid': '1927f040fcf011ee9d3cf3603895491c',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        # 'cookie': 'PHPSESSID=krnpi95fkqnobtht97egcv6vj3; PrestaShop-8aec7a5722627e6b2ad96140ea4d655d=def502009f4fa9378ff20c8c7153d7e29dbc9adfd54cc164c6edf7c6d18a60c9805effede39f7d0cf3685b1594942148b7760f8cce504f71d7d7d7384a20891368c5740d64bbf079c10ffc2f93ccf66a5ffcaba62aa8d7f9a6911da40094e463ca9644ab2db703a33bbbc3c35c1e1c0b012f0e38cd4b88316388c6ecaa576c193b79f10052904ab967cc10f10468d05df3c0ab8642e5f643240aa08cd39229c347c0e6c47489a0d2092435dacfe87da13450070d7fda11aa24b080af37a6e32fbc9576dce1c7b6c964d6dfcd134a5e91525af573ac95ead2d6ae30c90620f792405aa2dcfbcd4a8fbd77ffaa2ff5e0a6e3ff866acc8662ee3b504845b385c5accac1c1ee5e5119fccdccdf2dce7a2dbb021bb0feb79998d9d60e2cb7833817287d23fb82facb39615f00b74000560f; _gcl_au=1.1.10390569.1713381805; _ga=GA1.1.396208300.1713381809; _clck=ymhafp%7C2%7Cfl0%7C0%7C1568; cf_clearance=Gi8_y9w2zkiVktKk2_lcKCfE_NUx2jgp0LF3Gl9kws8-1713381857-1.0.1.1-hN7GzYxL.j6KWcp09ZwsCWM9VeDFo6dMrTvF5SWwtKld0QU0oeODK3.BrfWpaW_Glw0edHg82kzrxiIl_ksHYA; __stripe_mid=f889d6c1-5a40-4767-9093-13af5a5519308bd99e; __stripe_sid=c66f8a13-2a7e-465d-8b7f-36af025d570082e28c; _fbp=fb.1.1713381881167.1311298085; cookiesplus=%7B%22C_P_DISPLAY_MODAL%22%3Afalse%2C%22cookiesplus-finality-3%22%3A%22on%22%2C%22cookiesplus-finality-4%22%3A%22on%22%2C%22consent_date%22%3A%222024-04-17%2021%3A24%22%2C%22consent_hash%22%3A%224c475d251b8267148c18a64202f90fe3-31fb5c87%22%7D; _clsk=1g0szb2%7C1713382368447%7C5%7C1%7Cm.clarity.ms%2Fcollect; _ga_KF7FBSMZWH=GS1.1.1713381809.1.1.1713382373.46.0.0; _uetsid=1927c2f0fcf011eeb7c21ffefefdb30e; _uetvid=1927f040fcf011ee9d3cf3603895491c',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    }

    def start_requests(self):
        for i in range(1, 20):
            yield scrapy.Request(f'https://www.nicols.es/es/anillos-de-compromiso-pedida-49?page={i}', callback=self.parse)

    def parse(self, response):
        all_urls = response.css('.h3.product-title a::attr(href)').getall()
        for url in all_urls:
            yield scrapy.Request(url,callback=self.detail_page)

    def detail_page(self, response):
        description = response.css("#tab-content ::text").getall()
        title = response.css('.product_name strong::text').get('')
        ref_no = response.css('.product-reference span::text').getall()
        if ref_no:
            ref_no = ref_no[-1]
        price = response.css('.current-price span::text').get('')
        image_url = response.css('#zoom_product::attr(src)').get('')
        if description:
            description = ' '.join([value.strip() for value in description if value])
        names = response.css('.data-table .data-sheet dt')
        values = response.css('.data-table .data-sheet dd')
        product_detail = []

        for name, value in zip(names, values):
            _name = ''
            _value = ''
            if name:
                name = name.css('::text').getall()
                if name:
                    _name = ' '.join(name)

            if value:
                value = value.css('::text').getall()
                if value:
                    _value = ' '.join(value)
            product_detail.append(f"{_name}:{_value}")

        if product_detail:
            product_detail = ','.join(product_detail)
        else:
            product_detail = ''

        yield {
            'Image Url': image_url,
            'Title': title,
            'Reference No': ref_no,
            'Price': price,
            'Description': description,
            'Product Detail': product_detail,
            'Url': response.url
        }