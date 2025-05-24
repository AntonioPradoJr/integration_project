import sqlite3
from datetime import datetime

def save_price(crypto, coin, price):
    conn = sqlite3.connect('integration_project_crypto.db')
    cursor = conn.cursor()

    date_time = datetime.now().isoformat(timespec='seconds')
    cursor.execute('''
        INSERT INTO prices(crypto, coin, price, date_time)
        VALUES (?,?,?,?)
    ''',(crypto,coin,price,date_time))

    conn.commit()
    conn.close()