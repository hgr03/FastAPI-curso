from typing import Union 
from fastapi import FastAPI

app = FastAPI()

#regresa un mensaje
@app.get('/')
async def read_root():
    return {"message": "Hello world"}

#Parametros por ruta /1000
@app.get('/item/{item_id}')
async def read_item(item_id:int , q:Union[str, None] = None):
    return {'item_id':item_id, 'q':q}


#parametros por consulta ?num_1=1&num_2=2
@app.get('/calculadora')
async def calculator(num_1:float, num_2:float):
    return {"suma": num_1+num_2}