from fastapi import FastAPI
import pandas as pd
import random

app = FastAPI()

@app.get("/")
async def root():
	return "KJAPI"

@app.get("/api/{quantity}")
async def generate(quantity: int):

	if quantity > 120:
		return f"{quantity} is a big number! Unfortunately there aren't that many KJ facts! Hint: there are 120 KJ facts."

	facts_list = list()
	rand_list = list(range(121))
	random.shuffle(rand_list)

	data = pd.read_csv("../data/kjfacts.csv")

	for i in range(quantity):
		facts_list.append(data["Fact"][rand_list[i]])

	return facts_list 
