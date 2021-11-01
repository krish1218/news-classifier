
import pandas as pd
import numpy as np
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.model_selection import train_test_split

from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC

from sklearn.multiclass import OneVsRestClassifier

from ReadFromMongodb import read_mongo


dataset = read_mongo()
#df = pd.read_csv('news_articles.csv')
df=dataset.toPandas()

df['topic'] =  df['topic'].str.upper()

df["topic"].fillna(".", inplace = True)

df.loc[(df.topic == '.'),'topic']='OTHERS'

df["summary"].fillna("a", inplace = True)

df["title"].fillna("a", inplace = True)

lst1 = df['topic'].tolist()

def extractElements(lst):
    res = []
    for el in lst:
        sub = el.split(', ')
        res.append(sub)
      
    return(res)
lst2 = extractElements(lst1)

df['topic_list'] = pd.DataFrame({'topic':lst2})

y = df['topic_list']

multilabel = MultiLabelBinarizer()

y = multilabel.fit_transform(df['topic_list'])

#pd.DataFrame(y, columns=multilabel.classes_)

# lets say you have -> l,e,t,s, ,

df['news_summary'] = df['title']+df['summary']

tfidf = TfidfVectorizer(analyzer='word', max_features=10000, ngram_range=(1,3), stop_words='english')
X = tfidf.fit_transform(df['news_summary'])

# tfidf.vocabulary_

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)



"""# Build Model"""

sgd = SGDClassifier()
lr = LogisticRegression(solver='lbfgs')
svc = LinearSVC()

for classifier in [LinearSVC(C=1.5, penalty = 'l1', dual=False)]:
  clf = OneVsRestClassifier(classifier)
  clf.fit(X_train, y_train)
  y_pred = clf.predict(X_test)
  #print_score(y_pred, classifier)

for classifier in [sgd, lr, svc]:
  clf = OneVsRestClassifier(classifier)
  clf.fit(X_train, y_train)
  y_pred = clf.predict(X_test)
  #print_score(y_pred, classifier)

"""## Model Test with Real Data"""

text= "Chelsea beat Southampton in a shootout in the fourth round of the Carabao Cup at Stamford Bridge on Tuesday night after the game ended in a 1-1 draw in regular time.Kai Havertz scored right before half-time to put Chelsea in front as the teams went to the dressing room for the break.- ESPN+ viewers' guide: LaLiga, Bundesliga, MLS, FA Cup, more Che Adams struck back for the visitors early in the second half to level the score, but neither team could find the winner as the match headed to a shootout.Reece James scored the decisive goal from the spot to book Chelsea's passage to the fifth round with their opponent yet to be determined ahead of the rest of the fourth round games on Wednesday."

x = [ text]

xt = tfidf.transform(x)

clf.predict(xt)

multilabel.inverse_transform(clf.predict(xt))

text = "The Supreme Court  appointed a committee of experts to inquire into the alleged use of Israeli spyware Pegasus for surveillance of Indian citizens.A bench comprising Chief Justice N V Ramana and Justices Surya Kant and Hima Kohli said the three-member committee will be headed by former top court judge RV Raveendran.Citing national security, the Centre had refused to file a detailed affidavit in the matter. The pleas are related to reports of alleged snooping by government agencies on eminent citizens, politicians and scribes by using Israeli firm NSO's spyware Pegasus."

xt = tfidf.transform([text])

clf.predict(xt)

multilabel.inverse_transform(clf.predict(xt))

text1 = "Dune director Denis Villeneuve has expressed his great admiration of Christopher Nolan's most recent film, Tenet. After helming Arrival, Blade Runner: 2049 and now Dune (which released earlier this week), Villeneuve is himself no stranger to large-scale sci-fi films. Recently, Nolan gave Dune his high praise, saying the film was "'compelling at every turn" and "an incredible piece of work.'"Nolan's Tenet was released in August of 2020, after it had been delayed three times by the COVID pandemic. It was the first major Hollywood film to open in theatres after lockdowns were lifted, but restrictions were still in place in many countries. Starring John David Washington, Robert Pattinson, Elizabeth Debicki and Kenneth Branagh, Tenet's action-packed but highly complex narrative earned the film mixed reviews from both critics and audiences. Warner Bros. later announced that it would be re-releasing Tenet in select New York theatres to celebrate their doors re-opening after remaining closed for several difficult months. On March 1, Tenet was simultaneously released on HBO Max, causing bad blood between Nolan and the streaming service."

xt = tfidf.transform([text1])

clf.predict(xt)

multilabel.inverse_transform(clf.predict(xt))

predval=multilabel.inverse_transform(clf.predict(xt))
type(predval[0][0])

with open('newsclf_model.pkl','wb') as f:
    pickle.dump(clf,f)

vec_file = 'tfidvectorizer.pkl'
pickle.dump(tfidf, open(vec_file, 'wb'))


