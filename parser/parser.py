import requests
from bs4 import BeautifulSoup as BS
import re
import time

url = "ссылка"
r = requests.get(url)

dictionary = ['Физическая культура и спорт', 'Информатика'] # словарь, для выбора только этих слов из большого текста если нужно! Иначе удаляем 20 и 21 строку и сам словарь на 9 строке.

def parser():
    if r.status_code == 200:
        html = BS(r.content, 'html.parser')

        try:
            print ('Примерное время загрузки данных 2 секунды!')
            time.sleep (2)
            for el in html.select("класс"): # пример .menu и далее .menu-glav || в итоге ".menu .glav"
                osnov = el.select('класс') # что нужно выводить, также класс, обычно он один. Например .text_a
                for word in dictionary:
                    output = re.findall(rf'\b{dictionary}\b', osnov[0].text, flags=re.IGNORECASE)
                    print (*output) # в случаи удаление строк, которые написаны выше, меняем на osnov[0].text
        except Exception as e: 
            print (f'Ошибка - {e}') 
    else:
        print (f'Что-то со страницей! Ошибка {r.status_code}')

if __name__ == '__main__':
    print ('Загрузка данных...')
    time.sleep(1)
    parser()
