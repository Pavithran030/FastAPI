from pydantic import BaseModel

class Products(BaseModel):
    id:int
    name:str
    price:float
    description:str


# use this below code is  pydantic is not used.


# class Products():
#     id:int
#     name:str
#     price:float
#     description:str

#     def __init__(self,id : int ,name : str ,price : float ,description : str):
#         self.id=id
#         self.name=name
#         self.price=price
#         self.description=description

