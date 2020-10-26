import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText().strip()


def get_pig_address(fact):
    data = {'input_text': fact}
    pig = requests.post('https://hidden-journey-62459.herokuapp.com'
                        '/piglatinize/',
                        data=data)
    return pig.url


@app.route('/')
def home():
    fact = get_fact()
    address = get_pig_address(fact)
    return address


if __name__ == "__main__":
    # fact = get_fact()
    # get_pig_address(fact)
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

