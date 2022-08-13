from fastapi import FastAPI
from fastapi.responses import PlainTextResponse, JSONResponse
from linecache import getline
from json import loads as jloads
import random

app=FastAPI()

@app.get("/kota-kabupaten", response_class=PlainTextResponse)
def kota():
    return getline("kota-kabupaten.txt",random.randint(1,472)).replace("\n","")

@app.get("/pertanyaan", response_class=JSONResponse)
def pertanyaan():
    return jloads(getline("list_pertanyaan.json", random.randint(1,17)).replace("\n",""))