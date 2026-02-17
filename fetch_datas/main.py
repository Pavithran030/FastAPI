from fastapi import FastAPI

from models import Products

app=FastAPI()

@app.get("/")
def test():
    return "Testing prompt"


# use this below code if pydantic is not used.

# pros=[
#     Products(10,"Lap",200,"Hello Backend i am Learning..")
# ]

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





# POST 

@app.post("/adding")

#       variable : type (it a product type and its a class)

def posting( proo : Products):
    pros.append(proo)
    