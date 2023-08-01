import os
import glob
import pandas as pd
from statistics import mean
list_of_files = glob.glob('D:/Sem-5/LAB/Software Engineering/Project/Data-server/*.csv')
latest_file = max(list_of_files, key=os.path.getctime)
df=pd.read_csv(latest_file)

from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis")
Label=[]
Score=[]
for i, j in zip(df['Text'], df['Summary']):
  p=sentiment_pipeline((i+j)[:512])[0]
  Label.append(p.get('label'))
  Score.append(p.get('score'))
df['SentimentLabel']=Label
df['SentimentScore']=Score
p=0
n=0
for i in df["SentimentLabel"]:
    if i=='POSITIVE':
        p+=1
    else:
        n+=1
mean= "Positive" if p > n else "Negative"

from flask import Flask
  
# Initializing flask app
app = Flask(__name__)
  
  
# Route for seeing a data
@app.route('/dataSen')
def get_time():
  
    # Returning an api for showing in  reactjs
    return {
        'Positive':p,
        "Negative":n,
        "Mean": mean
        }
# Running app
if __name__ == '_main_':
    app.run()
    # host='127.0.0.1', port=9000, debug=True