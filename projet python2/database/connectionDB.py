# import pymysql
# def createTables():
#     try:
#         cnt = pymysql.connect(host="localhost", port="3306", user="root", password="")
#         cntCursor = cnt.cursor()
#         queries =['CREATE DATABASE IF NOT EXISTS GES_BIBLIO', 
#                   'USE GES_BIBLIO', 
#                   'CREATE TABLE IF NOT EXISTS users (idu int primary key, nom varchar(20), password varchar(20) not null, email varchar(10) not null)',
#                   'CREATE TABLE IF NOT EXISTS livre (idL int primary key, titre varchar(10), annee year, auteur varchar(10), image BLOB)',
#                   'CREATE TABLE IF NOT EXISTS li_us (idL int, idu int, qte varchar(10), PRIMARY KEY (idL,idu), FOREIGN KEY (idL) REFERENCES livre(idL), FOREIGN KEY (idu) REFERENCES users(idu))',
#                   "INSERT INTO users (idu, nom, password, email) VALUES (1, 'Alice', '123456', 'alice@gmail.com');",
#                   "INSERT INTO users (idu, nom, password, email) VALUES (2, 'lara', 'lara123', 'lara@gmail.com');",
#                   "INSERT INTO users (idu, nom, password, email) VALUES (3, 'aziza', 'az1ma', 'aziza@gmail.com');",
#                   "INSERT INTO users (idu, nom, password, email) VALUES (4, 'asmae', 'soso123', 'asmae@gmail.com');"]
        
#         for q in queries:
#             cntCursor.execute(q)
#     except Exception as e:
          #   pass
import mysql.connector
# db = mysql.connector.connect(
#    host = "localhost",
#    user = "root",
#    password = ""
#  )
# cur = db.cursor()

# cur.execute("CREATE DATABASE GES_BIBLIO")
 
# cur = db.cursor()

# cur.execute("SHOW DATABASES")
# for x in cur:
#  print(x)
#connexion au base de données
db = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "",
  database = "GES_BIBLIO"
)
cur = db.cursor()
cur.execute(#'CREATE TABLE IF NOT EXISTS users (idu INT primary key, nom VARCHAR(20), password VARCHAR(20) not null, email VARCHAR(10) not null)',)
    #  'CREATE TABLE IF NOT EXISTS livre (idL INT primary key, titre VARCHAR(10), year DATE, auteur VARCHAR(10), image BLOB)',)
    #  'CREATE TABLE IF NOT EXISTS li_us (idL INT, idu INT, qte VARCHAR(10), PRIMARY KEY (idL,idu), FOREIGN KEY (idL) REFERENCES livre(idL), FOREIGN KEY (idu) REFERENCES users(idu))')
     'CREATE TABLE IF NOT EXISTS admin ( idA int   primary key AI, FOREIGN KEY (idu) references users (idu))')
for table in cur:
  print(table)