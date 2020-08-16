from pydantic import BaseModel


class PatreonResponse:

    def __init__(self, username, status, mail):
        self.username = username
        self.mail = mail
        self.status = status


class PatreonModel(BaseModel):
    user_name: str
    mail: str
    status: str
