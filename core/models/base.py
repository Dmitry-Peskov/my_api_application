import datetime
import uuid
from sqlalchemy import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr
from sqlalchemy.types import DateTime


class BaseModel(DeclarativeBase):
    __abstract__ = True

    @declared_attr
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID,
        primary_key=True,
        unique=True,
        index=True,
        default=uuid.uuid4,
        comment="Идентификатор записи"
    )
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=func.now(),
        comment="Дата и время создания записи"
    )

    def __repr__(cls) -> str:
        return f"{cls.__name__} ({cls.id=})"
