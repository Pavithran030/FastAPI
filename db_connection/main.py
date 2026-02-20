from fastapi import FastAPI

from models import Products

from dbconfig import session,engine# import the session form the dbconfig file

import dbmodel  # import the metadata of the db (class and the structures..)

dbmodel.Base.metadata.create_all(bind=engine)



app=FastAPI()



#GET 


# To display in the content inn the server side 

pros=[
    Products(id = 1 , name = "Smartphone" , price = 350 , description = "Latest 5G enabled device."),
    Products(id = 2 , name = "Headphones" , price = 80 , description = "Noise cancelling wireless headphones."),
    Products(id = 3 , name = "Monitor" , price = 220 , description = "24 inch Full HD LED display."),
    Products(id = 4 , name = "Keyboard" , price = 45 , description = "Mechanical RGB gaming keyboard."),
    Products(id = 5 , name = "Mouse" , price = 25 , description = "Ergonomic wireless mouse.")
]

@app.get("/pro")

def products():
    return pros  # print the specific id value


# id based routing 

pr=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

@app.get("/{i}")

def pro(i:int):
    return pr[i][i]




# POST (or) UPDATE

@app.post("/adding")

#       variable : type (it a product type and its a class)

def posting( proo : Products):
    pros.append(proo)



# PUT (or) UPDATE

@app.put("/update/{id}")

def updates(id : int, products:Products):

    for i in range(len(pros)):

        if(pros[i].id==id):
            pros[i]=products

            return "Details added Successfully.."
    return "Update fails"



# DELETE

@app.delete("/del/{id}")

def deletes(id :int):
    
    for i in range(len(pros)):
        if(pros[i].id==id):
            # del pros[i]
            pros.pop(id)
            return pros[i] 
    return "Deleted Successfully"



# DB Storage..

@app.get("/dbs")

def store():
    db=session()
    db.query()
    return 