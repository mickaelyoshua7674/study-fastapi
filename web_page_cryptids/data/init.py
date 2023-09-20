from sqlite3 import connect
import os

_dbname = os.environ.get("CRYPTID_SQLITE_DB", "cryptid.db")
curs = connect(_dbname).cursor()