#! /usr/bin/env python3
# -*- coding: utf-8 -*-

""" Prepare database structure and transfer data task_data.csv
    _I will replace previously existing structure an data will be lost!_

    Command:
        $ python sqlite3_prepare_and_transfer_data.py
"""

# Import libraries
import os, sys
import logging
import sqlite3
from sqlite3 import Error
import csv_to_sqlite
from data import config as cfg

# Start script logging
logging.basicConfig(level=logging.INFO)
log = logging.getLogger()
#log.info("{} called {}".format(__name__, os.path.basename(__file__)))


# Transfer data from CSV to database
def transfer_data(since, to):
    log.info("Transfering data to {}...".format(cfg.sqlite3_db_file))

    options = csv_to_sqlite.CsvOptions(typing_style="full", drop_tables=False)
    csv_to_sqlite.write_csv([cfg.csv_data_file], cfg.sqlite3_db_file, options)

# Structure database and create log table
def create_logspace(into):
    log.info("Preparing SQLite3 Structure in {}...".format(into))

    try:
        conn = sqlite3.connect(into)
        cursor = conn.cursor()
    except Error as e:
        log.critical("SQLite3 on {} error: {}".format(into, e))
        return 2

    query = "CREATE TABLE log (\
        [sequencial] INTEGER PRIMARY KEY AUTOINCREMENT, \
        [moment] TIMESTAMP DEFAULT (datetime('now', 'localtime')), \
        [info] BLOB)"
    cursor.execute(query)

    query = "INSERT INTO log ([info]) VALUES ('Database initialized')"
    cursor.execute(query)

    conn.commit()
    conn.close()


if __name__ in ("__main__"):
    me = os.path.basename(__file__)
    where = os.getcwd().split("/")[-1]
    if where != "task":
        try:
            os.chdir("task/")
        except:
            log.critical("Please run 'python task/{0}' from project root or 'python {0}' from inside 'task/'.".format(me))
            sys.exit(1)

    try:
        os.remove(cfg.sqlite3_db_file)
    except:
        pass

    create_logspace(into=cfg.sqlite3_db_file)
    transfer_data(since=[cfg.csv_data_file], to=cfg.sqlite3_db_file)

