from bs4 import BeautifulSoup
from flask import Flask,jsonify
import requests


def get_currency(input_curr,output_curr):
    url=f'https://www.x-rates.com/calculator/?from={input_curr}&to={output_curr}&amount=1'
    content=requests.get(url).text
    soup=BeautifulSoup(content,'html.parser')
    rate=soup.find("span",class_="ccOutputRslt").get_text()
    rate=float(rate[:-4])
    return rate


app=Flask(__name__)

@app.route('/')
def home():
    return '<h1>Currency Rate API</h1> <p>Example URL: /api/v1/usd-eur</p>'

@app.route('/api/v1/<in_cur>-<out_cur>')
def api(in_cur,out_cur):
    rate=get_currency(in_cur,out_cur)
    result_dictionary={'input':in_cur,'output':out_cur,'rate':rate}
    return jsonify(result_dictionary)

app.run()