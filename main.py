from dotenv import load_dotenv
load_dotenv()

import os
import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://www.dolarhoy.com/'
TOKEN = os.getenv('TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
TELEGRAM_API_SEND_MSG = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

items = [
    'cotizaciondolaroficial',
    'cotizaciondolarblue',
]

def main(event={}, context={}):

    for item in items:
        url = BASE_URL + item
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')

        titulo = soup.select_one('title').get_text()
        #compra = soup.select_one('div[class="col-md-6 compra"]').get_text()
        #venta = soup.select_one('div[class="col-md-6 venta"]').get_text()
        #update = soup.select_one('span[class="update"]').get_text()

        data = {
            'chat_id': CHAT_ID,
            'text': f'Hola! Los precios promedio del mercado son:\n *\nÚltima actualización: ]({url})\n',
            'parse_mode': 'Markdown'
        }
        r = requests.post(TELEGRAM_API_SEND_MSG, data=data)

if __name__== '__main__':
    main()


