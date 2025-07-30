from pymongo import MongoClient as MongoClient

# Conexion a la base de datos en local.
# db_client = MongoClient().local

# conexion a la base de datos en Mongodb atlas.
db_client = MongoClient(
    "mongodb+srv://test:test@cluster0.ictpwvh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0").test