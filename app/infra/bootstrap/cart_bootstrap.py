from propan import RabbitBroker
from propan.fastapi import RabbitRouter
from pydantic import BaseModel

import redis as cache_client
from sqlalchemy.orm import sessionmaker
from app.infra import stripe
from app.cart import uow
from app.cart.uow import SqlAlchemyUnitOfWork
from app.infra.database import get_async_session as get_session
from app.infra import redis
from app.freight import freight_gateway as freight
from app.user import gateway as user_gateway
from typing import Any
from app.infra.worker import task_message_bus


class Command(BaseModel):
    """Command to use in the application."""

    db: sessionmaker
    uow: uow.AbstractUnitOfWork
    cache: redis.MemoryClient | cache_client.Redis
    message: RabbitRouter
    freight: freight.AbstractFreight
    user: Any
    payment: Any

    class Config:
        """Pydantic configs."""

        arbitrary_types_allowed = True


async def bootstrap(  # noqa: PLR0913
    db: sessionmaker = get_session(),
    uow: uow.AbstractUnitOfWork = None,
    cache: redis.AbstractCache = redis.RedisCache(),
    message: RabbitRouter = task_message_bus,
    freight: freight.AbstractFreight = freight.MemoryFreight(),
    user=user_gateway,
    payment: Any = stripe,  # noqa: ANN401
) -> Command:
    """Create a command function to use in the application."""
    if uow is None:
        uow = SqlAlchemyUnitOfWork()

    _cache = cache.client()
    _user = user

    return Command(
        db=db,
        uow=uow,
        cache=_cache,
        message=message,
        freight=freight,
        user=_user,
        payment=payment,
    )