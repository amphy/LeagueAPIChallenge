#!/usr/bin/env python

from flask import render_template, request, redirect, url_for
from LeagueAPIChallenge import app
from flaskext.mysql import MySQL
from ConfigParser import SafeConfigParser
from query import Query
import json

c = ""
result = []

mysql = MySQL()
parser = SafeConfigParser()
try:
  parser.read('/var/www/LeagueAPIChallenge/LeagueAPIChallenge/config.ini')
  print parser.sections()
  app.config['MYSQL_DATABASE_USER'] = parser.get('database', 'username')
  app.config['MYSQL_DATABASE_PASSWORD'] = parser.get('database', 'password')
  app.config['MYSQL_DATABASE_DB'] = parser.get('database', 'name')
  app.config['MYSQL_DATABASE_HOST'] = parser.get('database', 'host')
  apikey = parser.get('league_api', 'apikey')
  mysql.init_app(app)
except:
  print "ERROR WITH DATABASE CALL"

cursor = mysql.connect().cursor()
cursor.execute('SELECT match_id from urf')
entries = cursor.fetchone()
print entries

url = "https://global.api.pvp.net/api/lol/static-data/{0}/v1.2/champion?locale=en_US&api_key={1}"
q = Query("na", url, apikey, [])
try:
  html = q.fetchData()
  data = json.loads(html)
  for k, v in data["data"].items():
    result.append(str(v["name"]))
except:
  print "There was an error"

@app.route('/LeagueAPIChallenge/')
def mainpage():
  return render_template('homepage.html', champ_list = result)

@app.route('/LeagueAPIChallenge/champion/', methods = ['GET', 'POST'])
def champion():

  try:
    c = request.data
  except:
    c = "Aatrox"

  img_prefix = 'http://ddragon.leagueoflegends.com/cdn/5.2.1/img/item/'
  img1 = img_prefix + '3153.png'
  img2 = img_prefix + '3181.png'
  img3 = img_prefix + '3047.png'
  img4 = img_prefix + '3142.png'
  img5 = img_prefix + '3074.png'
  img6 = img_prefix + '3184.png'
  return render_template('champion.html', champion_name = c, url_img1 = img1, url_img2 = img2, 
  url_img3 = img3, url_img4 = img4, url_img5 = img5, url_img6 = img6, champ_list = result)
