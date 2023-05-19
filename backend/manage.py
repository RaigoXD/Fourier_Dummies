"""python main file to run the microservice
"""

from fastapi import FastAPI

# middleware
from fastapi.middleware.cors import CORSMiddleware

# routes
from backend.routes.index import function_controller
# from app.routes.index import likes

def get_application() -> FastAPI:
    tags_metadata = [
        {
            "name": "Fourier Dommies",
            "description": "Backend Service Fourier Dommies",
        }
    ]

    application = FastAPI(
        title="Dommies",
        version="1.0.0",
        description="Resful API",
        openapi_tags=tags_metadata,
    )

    application.include_router(function_controller, prefix="/api/utils")
    # application.include_router(likes, prefix="/crud_likes")

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return application


app = get_application()
