from sqlite3 import connect, IntegrityError
import os

_dbname = os.environ.get("CRYPTID_SQLITE_DB", "cryptid.db")
curs = connect(_dbname, check_same_thread=False).cursor()