#!/usr/bin/env python

from flask import render_template
from LeagueAPIChallenge import app
from flaskext.mysql import MySQL
from ConfigParser import SafeConfigParser

mysql = MySQL()
parser = SafeConfigParser()
try:
  parser.read('/var/www/LeagueAPIChallenge/LeagueAPIChallenge/config.ini')
  print parser.sections()
  app.config['MYSQL_DATABASE_USER'] = parser.get('database', 'username')
  app.config['MYSQL_DATABASE_PASSWORD'] = parser.get('database', 'password')
  app.config['MYSQL_DATABASE_DB'] = parser.get('database', 'name')
  app.config['MYSQL_DATABASE_HOST'] = parser.get('database', 'host')
  mysql.init_app(app)
except:
  print "ERROR WITH DATABASE CALL"

cursor = mysql.connect().cursor()
cursor.execute('SELECT match_id from urf')
entries = cursor.fetchone()
print entries

@app.route('/LeagueAPIChallenge/')
def mainpage():
  return render_template('template.html', name = 'Heather')

@app.route('/LeagueAPIChallenge/champion/')
def hello():
  img_prefix = 'http://ddragon.leagueoflegends.com/cdn/5.2.1/img/item/'
  img1 = img_prefix + '3153.png'
  img2 = img_prefix + '3181.png'
  img3 = img_prefix + '3047.png'
  img4 = img_prefix + '3142.png'
  img5 = img_prefix + '3074.png'
  img6 = img_prefix + '3184.png'
  return render_template('champion.html', champion_name = 'Aatrox', url_img1 = img1, url_img2 = img2, 
  url_img3 = img3, url_img4 = img4, url_img5 = img5, url_img6 = img6)

