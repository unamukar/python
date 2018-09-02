import dbSebas
def main():
    n='wisdompets/db.sqlite3'
    d=dbSebas.db(n)
    t2='adoptions_pet'
    for i in d.sql('PRAGMA table_info([{}])'.format(t2)):print('Table {}: {}'.format(t2,tuple(i)))
    for i in d.sql('SELECT * FROM {}'.format(t2)):print('Table {}: {}'.format(t2,dict(i)))
    d.close()
if __name__=='__main__':main()
