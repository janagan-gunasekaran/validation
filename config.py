import os

DIRPATH = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__))))


FILEMAP = [
    (f"{DIRPATH}\src\data.json", f"{DIRPATH}\contracts\personData\\base.json")
]