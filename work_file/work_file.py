import os

f = open("../text.txt")
conn = f.read()
f.close()
print(conn)

try:  # лучший вариант открытие файла
    with open("text1.txt") as k:
        conn = k.read()
except FileNotFoundError:
    conn = "NOT FOUND"

print(conn)

try:  # если файл не найден, то создается новый и перезаписывает туда данные
    with open("../text2.txt", "w") as tw:
        tw.write("sweet dreams")
except FileExistsError:
    print("help")

try:  # если файл не найден, то создается новый  и записывает данные в конец
    with open("text3.txt", "a") as tw:
        tw.write("sweet dreams")
        print("s", file=tw)
except FileExistsError:
    print("help")

# удаление файла
path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "text3.txt")
os.remove(path)
