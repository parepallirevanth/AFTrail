
from typing import Optional

from fastapi import FastAPI
import os

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}/{q}")
def read_item(item_id: int, q: Optional[str] = None):
   open('U_%s.py' % q, 'w').write("k") # create a new file with userid
   os.system("cp temp.txt U_* ")             # copy dag content in it
   os.system("sed -i \"s/VAR/NewDag/g\" U_*")
   os.system("cp U_* dags/")		     # copy user dag to dags folder
   return {"item_id": item_id, "q": q}

#open('U_%s.py' % item_id, 'w').write("k")
#os.system("cp tuto.py U_* ")
#os.system("sed 's/\"U_/\"U_/g' U_*")

