
from dotenv import load_dotenv

load_dotenv(override=True)

from fastapi import FastAPI

from api.routers.journal_router import router as journal_router

import logging
import sys
logging.basicConfig(level=logging.INFO)
consoleHandler = logging.StreamHandler(sys.stdout)
logger = logging.getLogger(__name__)

app = FastAPI(title="Journal API", description="A simple journal API for tracking daily work, struggles, and intentions")
app.include_router(journal_router)

@app.on_event("startup")
async def startup_log():
    logger.info("App started")
