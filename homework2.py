#!/usr/bin/python

import sqlite3
from flask import Flask,render_template

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

class create_table:
    def __init__(self,name):
        self.name = name
    def create_database(self):
        conn = sqlite3.connect(self.name)
        c = conn.cursor()
        c.execute('''CREATE TABLE MOCK
                (ID INT PRIMARY KEY NOT NULL,
                UUID CHAR(32) NOT NULL,
                NAME CHAR NOT NULL,
                MODLEPATH TEXT NOT NULL,
                RANK REAL NOT NULL,
                STATUS CHAR NOT NULL,
                CONFIG TEXT NOT NULL,
                COMMITER CHAR NOT NULL,
                COMMIT_TIME DATETIME NOT NULL,
                LAST_PROOCESSED_TIME DATETIME NOT NULL
                );''')
        conn.commit()
        conn.close()
    def insert_data(self):
        conn = sqlite3.connect(self.name)
        c = conn.cursor()
        c.execute(
            "INSERT INTO MOCK (ID,UUID,NAME,MODLEPATH,RANK,STATUS,CONFIG,COMMITER,COMMIT_TIME,LAST_PROOCESSED_TIME)\
            VALUES (1,'ABCDEFGHIJKLMNOPQRSTUVWXYZaaaaaa','test','/test',
            0.258,'ok','normal','yyq','2017-11-17 13:41:24',
            2017-11-17 13:41:24')");
        conn.commit()
        conn.close()

@app.route('/')
def index():
    l = []
    with open("./mock.data") as f:
        for line in f:
            a = line.split("\t")
            l.append({
                      "id":int(a[0]),
                      "uuid":a[1],
                      "name":a[2],
                      "config":a[3],
                      "model_path":a[4],
                      "rank":a[5],
                      "status":a[7],
                      "commiter":a[8],
                      "commit_time":a[9],
                      "last_processed_time":a[10]})
    return render_template('index.html',tasks=l)

if __name__ == "__main__":
    app.run(port=8000)

