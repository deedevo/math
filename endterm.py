import requests
import loging
from bs4 import BeautifulSoup

loging.basicConfig(level=loging.DEBUG)
logger = logging.getLogger('wb')


class Client:

    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            'Accept-Language': 'ru'}

    def load_page(self, page: int = None):
        url = 'https://www.wildberries.ru/catalog/muzhchinam/odezhda/dzhempery-i-kardigany'
        res = self.session.get(url=url)
        res.raise_for_status()
        return res.text

    def parse_page(self, text: str):
        soup = BeautifulSoup(text, 'lxml')
        container = soup.select('div.dtlist.i-dtList.j-card-item')
        for block in container:
            self.parse_block(block=block)

    def parse_block(self, block):
        logger.info(block)
        logger.info('=' * 100)

    def run(self):
        text = self.load_page
        self.parse_page(text=text)


if __name__ == '__main__':
    parser = Client()
    parse.run()