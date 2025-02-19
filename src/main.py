import uvicorn
from contextlib import asynccontextmanager
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from configs import config
from routers import weather
from infrastructure.middleware.trace_id import TraceIDMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    print("Starting Binge Backend...")
    yield
    # Clean up the ML models and release the resources
    print("Stopping Binge Backend...")


def create_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.add_middleware(TraceIDMiddleware)
    app.include_router(weather.router)

    return app

app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)