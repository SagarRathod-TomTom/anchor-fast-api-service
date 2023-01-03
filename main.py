from typing import Any
from fastapi import FastAPI
import json

index = 0
anchor_store = {}
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Anchor Backend Sharing Service"}


@app.post("/api/anchors/key")
async def save_anchor(anchorKey: Any, location: Any):
    global index, anchor_store
    index = index + 1
    print(f'Saving anchor at index: {index} = {anchorKey}')
    anchor_store[index] = (anchorKey, location)
    return index


@app.get("/api/anchors/last")
async def get_anchor():
    global index, anchor_store
    print(f'Getting last anchor:{anchor_store[index]}')
    return anchor_store[index][0]


@app.get("/api/anchors/{anchor_number}")
async def get_anchor_with_anchor_id(anchor_number: int):
    global anchor_store
    print(f'Getting anchor with id {anchor_number}:{anchor_store[anchor_number]}')
    return anchor_store[anchor_number][0]


@app.get("/api/allanchors")
async def get_all_anchors():
    global anchor_store
    print('Anchor Store:', anchor_store)
    return json.dumps(anchor_store)


@app.get("/api/clearanchors")
async def clean_anchors():
    global index, anchor_store
    anchor_store = dict()
    index = 0
    print("Cleared All anchors")
