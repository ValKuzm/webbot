--
-- File generated with SQLiteStudio v3.4.4 on �� ��� 24 13:35:51 2024
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: books
CREATE TABLE IF NOT EXISTS books (number NUMERIC PRIMARY KEY, "book name" TEXT NOT NULL, author TEXT NOT NULL, image BLOB NOT NULL, "file name" BLOB NOT NULL);
INSERT INTO books (number, "book name", author, image, "file name") VALUES (1, '����� �������', '������ ��������', '����� �������', '����� ������� ������ ��������');
INSERT INTO books (number, "book name", author, image, "file name") VALUES (2, '������ � ���������', '������ ��������', '������ � ���������', '������ � ��������� ������ ��������');
INSERT INTO books (number, "book name", author, image, "file name") VALUES (3, '���', '���� ��������� ��������', '���', '��� ���� ��������� ��������');
INSERT INTO books (number, "book name", author, image, "file name") VALUES (4, '������� ������', '��������� ��������� ������', '������� ������', '������� ������ ��������� ��������� ������');

-- Index: sqlite_autoindex_books_1
CREATE UNIQUE INDEX IF NOT EXISTS sqlite_autoindex_books_1 ON books (number COLLATE BINARY);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
