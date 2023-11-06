from flask import Flask
from census.logger import logging
from census.exception import CustomException
import os,sys

app = Flask(__name__)

@app.route("/",methods = ["GET","POST"])
def home():
    logging.info('Hello')
    return "Hii There"

if __name__=="__main__":
    app.run('0.0.0.0')