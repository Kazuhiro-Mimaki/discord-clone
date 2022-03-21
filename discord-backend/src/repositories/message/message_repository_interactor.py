from src.models.user import UserModel
from .message_repository_interface import IMessageRepository
from src.repositories.db import MESSAGE, session


class MessageRepository(IMessageRepository):
    def get_list(self):
        return session.query(MESSAGE).all()

    def create(self, content: str) -> int:
        db_message = MESSAGE(content=content)
        session.add(db_message)
        session.commit()
        return db_message.id
