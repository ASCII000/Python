import sqlite3

con = sqlite3.connect("_sqlite3/db_example.db")

cur = con.cursor()
cur.execute(
    """
    CREATE TABLE IF NOT EXISTS movies (
    titulo TEXT PRIMARY KEY NOT NULL,
    avaliacao INTEGER NOT NULL,
    ano INTEGER)
    """
)
try:
    cur.execute(
        """
        INSERT INTO movies (titulo, avaliacao, ano) VALUES
        ('BATMAN', 4, 2012),
        ('BARBIE', 5, 2023)
        """
    )
except:
    cur.execute(
        """
        UPDATE movies
        SET avaliacao = 5
        WHERE titulo = 'BATMAN'
        """
    )

con.commit()

res = cur.execute("SELECT * FROM movies ORDER BY ano DESC")

print(res.fetchall())
