from fastapi import FastAPI
from routes.user import user
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title= "API-Users",
    description = "API creada con FASTAPI & ANACONDA(PythonDev)",
    version ="0.1",
    openapi_tags=[{
        "name": "user",
        "description": "routes" 
    }]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user)

