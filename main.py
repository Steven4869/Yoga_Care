from flask import Flask, render_template
import pymysql
pymysql.install_as_MySQLdb()
from flask_mysqldb import MySQL
import yaml



app = Flask(__name__)

db = yaml.full_load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
mysql = MySQL(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/positions")
def positions():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM data")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('positions.html', userDetails=userDetails)
@app.route("/videos")
def videos():
    cur = mysql.connection.cursor()
    VideoLink = cur.execute("SELECT * FROM video")
    if VideoLink>0:
        videoValues = cur.fetchall()
    return render_template('videos.html', videoValues=videoValues)

if (__name__ == '__main__'):
    app.run(debug=True)
