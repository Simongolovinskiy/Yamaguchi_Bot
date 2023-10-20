import logging
import asyncio

from src.bot.main import run_bot


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(run_bot())
