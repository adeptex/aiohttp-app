import sqlite3


def sql(query, *args):
    db = sqlite3.connect('app/db/database.sqlite3')
    cursor = db.cursor()
    
    if len(args):
        ret = cursor.execute(query, args)
    else:
        ret = cursor.execute(query)
    
    ret = ret.fetchall()
    
    db.commit()
    db.close()
    return ret