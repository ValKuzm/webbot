--
-- File generated with SQLiteStudio v3.4.4 on Вс мар 24 13:35:51 2024
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: books
CREATE TABLE IF NOT EXISTS books (number NUMERIC PRIMARY KEY, "book name" TEXT NOT NULL, author TEXT NOT NULL, image BLOB NOT NULL, "file name" BLOB NOT NULL);
INSERT INTO books (number, "book name", author, image, "file name") VALUES (1, 'Белая гвардия', 'Михаил Булгаков', 'белая гвардия', 'Белая гвардия Михаил Булгаков');
INSERT INTO books (number, "book name", author, image, "file name") VALUES (2, 'Мастер и Маргарита', 'Михаил Булгаков', 'Мастер и Маргарита', 'Мастер и Маргарита Михаил Булгаков');
INSERT INTO books (number, "book name", author, image, "file name") VALUES (3, 'Ася', 'Иван Сергеевич Тургенев', 'Ася', 'Ася Иван Сергеевич Тургенев');
INSERT INTO books (number, "book name", author, image, "file name") VALUES (4, 'Евгений Онегин', 'Александр Сергеевич Пушкин', 'Евгений Онегин', 'Евгений Онегин Александр Сергеевич Пушкин');

-- Index: sqlite_autoindex_books_1
CREATE UNIQUE INDEX IF NOT EXISTS sqlite_autoindex_books_1 ON books (number COLLATE BINARY);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
