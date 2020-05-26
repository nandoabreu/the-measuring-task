#! /usr/bin/env python3
# -*- coding: utf-8 -*-

""" Run server app an accept GET requests through http
    Routes/handlers:
        /: redirects to /list
        /list: lists data from DB (must import from csv first)
        /log: lists logs stored in DB
"""

# Import libraries
import os, sys
import logging
from flask import Flask
from flask import redirect, url_for
from flask import render_template
import sqlite3
from sqlite3 import Error
from data import config as cfg

# Start script logging
logging.basicConfig(level=logging.INFO)
log = logging.getLogger()
log.info("{} called {}".format(__name__, os.path.basename(__file__)))


# Instanciate Flask
app = Flask(__name__)

# Response to http GET /list
@app.route('/list')
def list():
    try:
        conn = sqlite3.connect(cfg.sqlite3_db_file)
        cursor = conn.cursor()
    except Error as e:
        log.critical("SQLite3 on {} error: {}".format(cfg.sqlite3_db_file, e))
        return 2

    query = "INSERT INTO log (info) VALUES ('Data requested')"
    cursor.execute(query)
    conn.commit()

    query = "SELECT * FROM task_data"
    cursor.execute(query)
    data = cursor.fetchall()

    conn.close()
    return render_template("list.html", data=data)

# Response to http GET /log
@app.route('/log')
def log():
    try:
        conn = sqlite3.connect(cfg.sqlite3_db_file)
        cursor = conn.cursor()
    except Error as e:
        log.critical("SQLite3 on {} error: {}".format(cfg.sqlite3_db_file, e))
        return 2

    query = "SELECT * FROM log ORDER BY sequencial DESC"
    cursor.execute(query)
    data = cursor.fetchall()

    conn.close()
    return render_template("log.html", data=data)

# Response to http GET /
@app.route("/")
def index():
    return redirect(url_for("list"))


if __name__ in ("__main__"):
    me = os.path.basename(__file__)
    where = os.getcwd().split("/")[-1]
    if where != "task":
        try:
            os.chdir("task/")
        except:
            log.critical("Please run 'python task/{0} [PORT]' from project root or 'python {0} [PORT]' from inside 'task/'.".format(me))
            sys.exit(1)

    port = 8080
    try:
        int(sys.argv[1]) + 0
        port = int(sys.argv[1])
    except:
        pass

    app.run(host="0.0.0.0", port=port)

