import pickle
import pandas as pd
import json
from sklearn.preprocessing import MultiLabelBinarizer

def predict_model(docs_news):
    f = open("topic_list.txt","r")
    fl=f.read()
    tlist = list(fl.splitlines())
    
    multilable1 = MultiLabelBinarizer()
    y = multilable1.fit_transform([tlist])
    
    model=pickle.load(open('newsclf_model.pkl','rb'))
    
    loaded_vectorizer = pickle.load(open('tfidvectorizer.pkl', 'rb'))
    

    xt = loaded_vectorizer.transform([docs_news])


    predval = multilable1.inverse_transform(model.predict(xt))


    if len(predval[0]) < 1:
        return 'Unable to predict Sry!!'
    else:
        return predval[0][0]

    

#print(predict_model("The World Health Organization (WHO) announced 26 proposed members to an advisory committee aimed to steer studies into the origin of the COVID-19 pandemic and other pathogens of epidemic potential"))

    