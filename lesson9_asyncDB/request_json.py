import asyncio
from dataclasses import dataclass
from aiohttp import ClientSession
from loguru import logger


@dataclass
class Service:
    name: str
    url: str


SERVICES = [
    Service("users", "https://jsonplaceholder.typicode.com/users"),
    Service("posts", "https://jsonplaceholder.typicode.com/posts"),
]


async def fetch(session: ClientSession, url: str) -> dict:
    """
    :param session:
    :param url:
    :return:
    """
    async with session.get(url) as response:
        return await response.json()


async def fetch_json_list(service: Service):
    """
    :param service:
    :return:
    """
    async with ClientSession() as session:
        result = await fetch(session, service.url)

    logger.info("Got {} results for {}, result {}", len(result), service.name, result)
    return result


async def make_requests():
    done, pending = await asyncio.wait(
        [fetch_json_list(s) for s in SERVICES],
        timeout=5,
        return_when=asyncio.ALL_COMPLETED,
    )
    return [t.result() for t in done]

