import urllib.request

from bs4 import BeautifulSoup
import asyncio
import aiohttp

URL = 'http://127.0.0.1:8000'


async def parse_catalogs(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.text(encoding='utf-8')
            name = url.split('/')[-1]
            with open(name, 'w', encoding='utf-8') as f:
                f.write(data)


if __name__ == '__main__':
    # получаем главную страницу
    with urllib.request.urlopen(URL) as response:
        main_html = response.read().decode('utf-8')
        if response.code != 200:
            raise Exception('Ошибка получения главной страницы!')
        print(main_html)
    
    # собираем все ссылки каталогов
    soup = BeautifulSoup(main_html, 'html.parser')
    link_tags = soup.find_all('a', class_='dropdown-item')
    catalog_links = [f'{URL}{link_tag["href"]}.html' for link_tag in link_tags]
    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait([parse_catalogs(url) for url in catalog_links]))
