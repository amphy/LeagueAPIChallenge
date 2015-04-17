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

#app.config['MYSQL_DATABASE_USER'] = parser.get('database', 'username')
#app.config['MYSQL_DATABASE_PASSWORD'] = parser.get('database', 'password')
#app.config['MYSQL_DATABASE_DB'] = parser.get('database', 'name')
#app.config['MYSQUL_DATABASE_HOST'] = parser.get('database', 'host')
#mysql.init_app(app)

cursor = mysql.connect().cursor()
cursor.execute('SELECT match_id from urf')
entries = cursor.fetchone()
print entries

@app.route('/LeagueAPIChallenge/')
def mainpage():
  return render_template('template.html', name = 'Heather')

@app.route('/LeagueAPIChallenge/template/')
def hello():
  return render_template('template.html', name = 'name')

