import uvicorn
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

# Creamos una conexión a la bd
engine = create_engine('postgresql://postgres:postgres@localhost:5432/public')

# Creamos una sesión para interactuar con la bd
Session = sessionmaker(bind=engine)
session = Session()

# esquema de la tabla 
metadata = MetaData()
products = Table('products', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('name', String),
                 Column('description', String))

# Definimos un modelo para crear un nuevo producto
class Product(BaseModel):
    name: str
    description: str

@app.get("/hello_ud")
def hello_ud():
    return "Welcome to UD!"

# ruta para obtener todos los productos
@app.get("/products")
def get_products():
    query = products.select()
    result = session.execute(query)
    products = result.fetchall()
    return products

# ruta para crear un nuevo producto
@app.post("/products")
def create_product(product: Product):
    query = products.insert().values(name=product.name, description=product.description)
    session.execute(query)
    session.commit()
    return {"message": "Product created successfully"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)