import requests

def cnn():
    x = requests.get(url='https://production.dataviz.cnn.io/index/fearandgreed/graphdata', headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'})
    return x.json()['fear_and_greed']['score']

