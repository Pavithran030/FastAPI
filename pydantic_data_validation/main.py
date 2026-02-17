from fastapi import FastAPI

from models import Products

app=FastAPI()

@app.get("/")
def test():
    return "Testing prompt"


# use this below code is  pydantic is not used.

# pros=[
#     Products(10,"Lap",200,"Hello Backend i am Learning..")
# ]

pros=[
    Products(id = 11 , name = "Smartphone" , price = 350 , description = "Latest 5G enabled device."),
    Products(id = 12 , name = "Headphones" , price = 80 , description = "Noise cancelling wireless headphones."),
    Products(id = 13 , name = "Monitor" , price = 220 , description = "24 inch Full HD LED display."),
    Products(id = 14 , name = "Keyboard" , price = 45 , description = "Mechanical RGB gaming keyboard."),
    Products(id = 15 , name = "Mouse" , price = 25 , description = "Ergonomic wireless mouse.")
]

@app.get("/pro")
def products():
    return pros