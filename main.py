from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import products, basic_auth_users, jwt_auth_users, users, users_db
from datetime import datetime, timezone

app = FastAPI(
    title="Mi API FastAPI Completa",
    description="API con múltiples routers, autenticación y conexión a MongoDB Atlas",
    version="1.0.0"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especifica los dominios permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(products.router)
app.include_router(users.router)
app.include_router(basic_auth_users.router)
app.include_router(users_db.router)
app.include_router(jwt_auth_users.router)

@app.get("/")
async def root():
    return {
        "message": "¡API FastAPI Completa funcionando correctamente!",
        "status": "online",
        "version": "1.0.0",
        "endpoints": {
            "docs": "/docs",
            "products": "/products",
            "users": "/users",
            "basic_auth": "/basicauth",
            "users_db": "/usersdb",
            "jwt_auth": "/jwtauth"
        }
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.now(timezone.utc)}
