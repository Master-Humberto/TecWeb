import sqlite3
from dataclasses import dataclass

@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''

class Database:
    def __init__(self, dbname):
        self.conn = sqlite3.connect(f'{dbname}' + '.db')
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS note ( id INTEGER PRIMARY KEY, title TEXT , content TEXT NOT NULL);")
        

    def add(self, note = Note):
        self.cur.execute(f"INSERT INTO note ('title','content') VALUES (?,?);",(note.title, note.content))
        self.conn.commit()

    def get_all(self):
        cursor = self.conn.execute("SELECT id, title, content FROM note")
        notes = []
        for linha in cursor:
            id = linha[0]
            title = linha[1]
            content = linha[2] 
            notes.append(Note(id=id, title=title, content=content))
           
        return notes

    def update(self, note = Note):
        self.cur.execute(f"UPDATE note SET title = ?, content = ? WHERE id = ?;",(note.title, note.content, note.id))
        self.conn.commit()

    def delete(self, id):
        self.cur.execute(f"DELETE FROM note WHERE id = ?;",(str(id)))
        self.conn.commit()
        

