x = int(input())
y = int(input())
if x == y:
    print(-1)
elif x * (x - x % 2) // (y - x) != 0:
    print(x * (x - x % 2) // (y - x))
else:
    print(x)


    
import sqlite3

fileName = input()
connection = sqlite3.connect(fileName)
query = """
    select films.title from films, genres
    where films.genre = genres.id and (genres.title = "музыка" or genres.title = "анимация") and films.year >= 1997
"""
res = connection.cursor().execute(query).fetchall()
for row in res:
    print(row[0])


connection.close()