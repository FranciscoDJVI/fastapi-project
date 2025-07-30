# API FastAPI con Autenticación JWT

API desarrollada con FastAPI que incluye autenticación JWT y conexión a MongoDB Atlas.

## Características

- ✅ Autenticación JWT
- ✅ Conexión a MongoDB Atlas
- ✅ CORS habilitado
- ✅ Endpoints de salud
- ✅ Documentación automática con Swagger

## Endpoints

- `GET /` - Endpoint raíz
- `GET /health` - Health check
- `POST /token` - Login y obtención de token
- `GET /users/me/` - Información del usuario actual
- `GET /users/me/items/` - Items del usuario actual
- `GET /docs` - Documentación Swagger (automática)

## Usuario de prueba

- **Username:** `johndoe`
- **Password:** `secret`

## Despliegue en Render

### 1. Preparar el repositorio
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/tuusuario/tu-repositorio.git
git push -u origin main
```

### 2. Crear cuenta en Render
1. Ve a https://render.com
2. Regístrate con GitHub
3. Conecta tu repositorio

### 3. Configurar el servicio
1. Clic en "New" → "Web Service"
2. Conecta tu repositorio de GitHub
3. Configuración:
   - **Name:** tu-api-fastapi
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn api:app --host 0.0.0.0 --port $PORT`

### 4. Variables de entorno (opcional)
En la sección "Environment":
- `SECRET_KEY`: Tu clave secreta
- `MONGODB_URL`: Tu URL de MongoDB Atlas
- `ALGORITHM`: HS256
- `ACCESS_TOKEN_EXPIRE_MINUTES`: 30

### 5. Desplegar
- Clic en "Create Web Service"
- Espera a que termine el build
- Tu API estará disponible en: `https://tu-api-fastapi.onrender.com`

## Otras opciones de despliegue gratuitas

### Railway
1. Ve a https://railway.app
2. Conecta GitHub
3. Deploy from repo
4. Variables de entorno en Settings

### Fly.io
1. Instala Fly CLI
2. `fly launch`
3. `fly deploy`

### Vercel (para APIs pequeñas)
1. Ve a https://vercel.com
2. Import project from GitHub
3. Configura como Python project

## Desarrollo local

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar servidor de desarrollo
uvicorn api:app --reload

# La API estará en http://localhost:8000
# Documentación en http://localhost:8000/docs
```

## Conexión a MongoDB

Para conectar tu MongoDB Atlas, agrega tu connection string en las variables de entorno:

```
MONGODB_URL=mongodb+srv://usuario:password@cluster.mongodb.net/basededatos?retryWrites=true&w=majority
```

## Seguridad

- Cambia la `SECRET_KEY` en producción
- Configura los orígenes CORS específicos en lugar de usar `*`
- Usa HTTPS en producción
- Configura rate limiting si es necesario
