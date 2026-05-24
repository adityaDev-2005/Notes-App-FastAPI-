from pydantic import BaseModel

class Note(BaseModel):

    title: str
    content: str
    pinned: Optional[bool] = False


# this file includes the things that are given as input
