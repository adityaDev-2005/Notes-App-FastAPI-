# use this to check if ur app connected to the database you made
# from database import engine
# print(engine.url)


# endpoints: 
#/notes
#/notes/id
#/notes/title

from fastapi import Depends, FastAPI
from models import Note
from fastapi.middleware.cors import CORSMiddleware
from database import engine, session
import database_models
from sqlalchemy.orm import Session

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

database_models.Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    return "Welcome to the Notes APP."


notes = [
    Note(
        title="FastAPI important points",
        content=
            "1. FastAPI is a backend framework to create using pyton.\n"
            "2. It can be used to integrate the ml models which can be made easy for deployment."
            
    ),

    Note(
        title="Research Paper",
        content=
            '1. The paper is "Attention is all you need"\n'
            "2. It deals with how the transformers are made and how attention is a very crucial feature."
            
    )
]

def get_db():

    db = session()
    try:
        yield db
    finally:
        db.close()



def init_db():
    db = session()

    count = db.query(database_models.Note).count()

    if count == 0:
        for note in notes:
            db.add(
                database_models.Note(
                    **note.model_dump()
                )
            )
        db.commit()
    db.close()

init_db()


@app.get("/notes")
def get_all_notes(
    db: Session = Depends(get_db)
):
    
    return db.query(
        database_models.Note
    ).all()


@app.get("/notes/{id}")
def get_note_by_id(
    id:int,
    db: Session = Depends(get_db)
):
    
    note = db.query(
        database_models.Note
    ).filter(
        database_models.Note.id == id
    ).first()

    if note:
        return note
    
    return {"message":"Notes not found"}

@app.post("/notes")
def add_note(
    note:Note,
    db: Session = Depends(get_db)
):
    
    new_note = database_models.Note(
        **note.model_dump()
    )

    db.add(new_note)

    db.commit()

    db.refresh(new_note)

    return new_note

@app.delete("/notes/{id}")
def delete_note(
    id: int,
    db: Session = Depends(get_db)
):

    db_note = db.query(
        database_models.Note
    ).filter(
        database_models.Note.id == id
    ).first()

    if db_note:

        db.delete(db_note)

        db.commit()

        return{
            "message":"Note deleted successfully"
        }
    

    return{
        "message":"Note not found"
    }