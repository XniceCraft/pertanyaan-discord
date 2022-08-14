#pylint: disable=line-too-long
from linecache import getline
from json import loads as jloads
from random import randint
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app=FastAPI()
@app.get("/", response_class=JSONResponse)
def root() -> dict:
    '''Mereturn status'''
    return {"status":"berhasil"}

@app.get("/kota-kabupaten", response_class=JSONResponse)
def kota() -> dict:
    '''Memilih Kota/Kabupaten secara acak'''
    pilih_acak=getline("kota-kabupaten.txt",randint(1,472)).replace("\n","")
    tersensor=""
    pilih_acak_huruf=[randint(0,len(pilih_acak)-1) for _ in range(int(len(pilih_acak)*randint(1,30)/100))]

    apakah_spasi=False
    for nomor_iterasi, isi in enumerate(pilih_acak):
        if nomor_iterasi > 1 and isi != " " and not apakah_spasi and nomor_iterasi not in pilih_acak_huruf:
            tersensor+="ˍ "
        else:
            if isi == " ":
                apakah_spasi=True
            elif apakah_spasi:
                apakah_spasi=False
            tersensor+=f"{isi} "
    return {"hasil": pilih_acak, "tersensor": tersensor}

@app.get("/pertanyaan", response_class=JSONResponse)
def pertanyaan() -> dict:
    '''Mereturn pertanyaan secara acak'''
    return jloads(getline("daftar-pertanyaan.json", randint(1,51)).replace("\n",""))
