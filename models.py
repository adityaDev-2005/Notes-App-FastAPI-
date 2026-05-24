from pydantic import BaseModel

class Note(BaseModel):

    title: str
    content: str


# this file includes the things that are given as input