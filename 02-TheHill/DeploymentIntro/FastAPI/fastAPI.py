from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    salary : int
    bonus : int
    taxes : int

@app.get('/')
def read_root():
    return {"Hello": "World"}


@app.get("/mult/")
def add(mult : int):
    return {'res' : mult * 2}


@app.post("/salary")
def salary(item: Item):
    if not isinstance(item.salary, int) or not isinstance(item.bonus, int) or not isinstance(item.taxes, int):
        print('coucou')
        raise HTTPException(status_code=400, detail={"error": "expected numbers, got strings."})
    return {"result": item.salary + item.bonus - item.taxes}
   


@app.post("/salaryy")
def salary(item: Item):
    if not isinstance(item.salary, int) or not isinstance(item.bonus, int) or not isinstance(item.taxes, int):
        return {"error": "expected numbers, got strings."}
    return {"result": item.salary + item.bonus - item.taxes}


dic = {
    1 : {
        1 : "a",
        2 : "b"
    }
}

@app.get('/page/{id}')
def message(id : int):
    return {'res' : dic[id][1]}

