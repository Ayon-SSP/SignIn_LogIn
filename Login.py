# from crypt import methods
import psycopg2
from flask import Flask, render_template, request
import Content.Configuration as config

conn = psycopg2.connect(
    host = config.hostname,
    dbname = config.database,
    user = config.username,
    password = config.pwd,
    port = config.port_id
)
cur = conn.cursor()
insert_script = '''
    INSERT INTO UserData (id,password) VALUES (%s,%s)
'''

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def getvalue():
    name = request.form['name']
    pwd = request.form['pwd']
    
    insert_value = (name,pwd)
    cur.execute(insert_script,insert_value)
    conn.commit()
        
    
    
    # insert_value = (name,pwd)
    # insert_value = ('AYON','passpass')
    # try:
    # cur = db.conn.cursor()
    # cur.execute(db.insert_script,insert_value)
    # cur.close()
    # db.conn.close()
    
    return render_template('pass.html', n=name, p=pwd)

if __name__== '__main__':
    app.run(debug=True)