from flask import Flask, render_template
import pymysql
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
try :
    db = pymysql.connect(
        host = 'databasemysql5.mysql.database.azure.com',
        user = 'damar',
        password = 'ariandi*123#',
        db = 'data5',
        ssl = {'ca' :os.getenv("SSL")}
    )
    print('berhasil konek ke database')
    print(os.getenv('DB_NAME'))
except Exception as err:
    print(f'gagal konek ke database, error: {err}')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about/')
def about():
    cur = db.cursor()
    cur.execute('SELECT * from nama')
    data=cur.fetchall()
    print(data)
    return render_template('about.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
