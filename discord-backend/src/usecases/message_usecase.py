from src.repositories.message import MessageRepository, IMessageRepository


class MessageUseCase():
    def __init__(self, message_repository: IMessageRepository) -> None:
      self.message_repository = message_repository

    def create(self, req):
      try:
        msg_id = self.message_repository.create(content=req['content'])
        msg_list = self.message_repository.get_list()
        return  msg_list
      except Exception as e:
        print(e)

msg_usecase = MessageUseCase(message_repository=MessageRepository())