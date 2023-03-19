from fastapi import FastAPI
from pydantic import BaseModel # Used to send information to our API
import pickle
import pandas as pd

from body.request import ScoringItem
from body.response import ResponseItem

app = FastAPI()

with open('./model/rfmodel.pkl','rb') as f:
    model = pickle.load(f)

@app.post('/',response_model=ResponseItem)
async def scoring_endpoint(item:ScoringItem): 
    df = pd.DataFrame([item.dict().values()],columns=item.dict().keys())
    res = model.predict(df)
    return ResponseItem(prediction = int(res))