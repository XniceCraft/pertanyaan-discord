#pylint: disable=line-too-long
from linecache import getline
from json import loads as jloads
from random import randint
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from subprocess import run

jumlah_pertanyaan=int(run("wc -l daftar-pertanyaan.json".split(), capture_output=True).stdout.decode().split()[0])
jumlah_kota_kabupaten=int(run("wc -l kota-kabupaten.txt".split(), capture_output=True).stdout.decode().split()[0])

app=FastAPI()
@app.get("/", response_class=JSONResponse)
async def root() -> dict:
    '''Mereturn status'''
    return {"status":"berhasil"}

def _return_kota(pilih_acak: str) -> dict:
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

@app.get("/kota-kabupaten", response_class=JSONResponse)
async def kota(generate: int=None) -> dict:
    '''Memilih Kota/Kabupaten secara acak'''
    if generate is not None:
        list_number=set()
        while True:
            list_number.add(randint(1,jumlah_kota_kabupaten))
            if len(list_number) == generate:
                break
        return [_return_kota(getline("kota-kabupaten.txt",list_number.pop()).replace("\n","")) for _ in range(generate)]
    if generate is None:
        pilih_acak=getline("kota-kabupaten.txt",randint(1,jumlah_kota_kabupaten)).replace("\n","")
        return _return_kota(pilih_acak)

@app.get("/pertanyaan", response_class=JSONResponse)
async def pertanyaan(generate: int=None) -> dict:
    '''Mereturn pertanyaan secara acak'''
    if generate is not None:
        if generate > jumlah_pertanyaan:
            return {"error":f"permintaan melebihi {jumlah_pertanyaan}"}
        list_number=set()
        while True:
            list_number.add(randint(1,jumlah_pertanyaan))
            if len(list_number) == generate:
                break
        return [jloads(getline("daftar-pertanyaan.json", list_number.pop()).replace("\n","")) for _ in range(generate)]
    elif generate is None:
        return jloads(getline("daftar-pertanyaan.json", randint(1,jumlah_pertanyaan)).replace("\n",""))
