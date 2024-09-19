__all__ = ["db"]

from settings import config
from asyncio import current_task
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    async_scoped_session,
    AsyncSession
)


class DataBase:

    def __init__(self):
        self.engine = create_async_engine(
            url=config.db.dsn,
            echo=config.db.echo
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=config.db.autoflush,
            expire_on_commit=config.db.expire_on_commit
        )

    def get_scoped_session(self):
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task
        )
        return session

    async def session_dependency(self) -> AsyncSession:
        session = self.get_scoped_session()
        yield session
        await session.close()


db = DataBase()
