from flask import Flask

app = Flask(__name__)

@app.route("/",methods = ["GET","POST"])
def home():
    return "Hii There"

if __name__=="__main__":
    app.run('0.0.0.0')