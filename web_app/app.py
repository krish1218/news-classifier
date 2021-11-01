import numpy as np
#import data
from utils import predict_model
from flask import Flask,render_template,request

app=Flask(__name__)
#model=pickle.load(open('newsclassifier_model.pkl','rb'))

@app.route('/')
def home():
    return render_template("index.html")


@app.route("/prediction",methods=["POST","GET"])
def predict():
    news_summary=request.form["summary_text"]
    print(news_summary)
    #param = request.get_json()
    #print(param['text'])
    result=predict_model(news_summary)
    return render_template("index.html",output=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"))#map port to 5000