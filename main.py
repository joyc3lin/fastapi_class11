from fastapi import FastAPI
from flask import Flask, request
import pandas as pd 

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello World"}

df = pd.read_csv('./data/diagnoses2019.csv')

app = Flask(__name__)

@app.route('/', methods=["GET"])
def home(): 
    return 'this is a API service for MN ICD code details'

@app.route('/preview', methods =['GET'])
def preview(): 
    top10rows = df.head(10)
    result = top10rows.to_json(orient="records")
    return result

@app.route('/icd/<value>', methods=['GET'])
def icdcode(value):
    print('value: ', value)
    filtered = df[df['principal_diagnosis_code'] == value]
    if len(filtered) <= 0:
        return 'There is nothing here'
    else: 
        return filtered.to_json(orient="records")


if __name__ == '__main__':
    app.run(debug=True)
