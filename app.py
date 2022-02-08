
from methods import downloadFile
from flask import Flask

URL = 'https://www.instagram.com/p/CZnWeMDporv/?utm_source=ig_web_copy_link'

app = Flask(__name__)

@app.route("/")
def main():
    return '<p>Flask app - Instagram download</p>'

@app.route("/images")
def image():
    downloadFile(URL)
    return '<p>Flask app - Instagram image download</p>'

