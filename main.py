import urllib2
import re
import time
import datetime

from ConfigParser import SafeConfigParser

class Query:
	def __init__(self, server, beginDate, apiKey):
    parser = SafeConfigParser()
    parser.read('config.ini')
    self.server = server
		self.beginDate = beginDate
		self.apiKey = parser.get('league_api', 'apikey')
		self.url = self.generateUrl()
	
	def generateUrl(self):
		baseUrl = "https://na.api.pvp.net/api/lol/{server}/v4.1/game/ids?beginDate={beginDate}&api_key={apiKey}"
		url = baseUrl.format(server = self.server, beginDate = self.beginDate, apiKey = self.apiKey)
		return url
	
	def fetchData(self):
		response = None
		try:
			response = urllib2.urlopen(self.url)
		except:
			return []
		html = response.read()
		formattedHtml = html.replace("[", "").replace("]", "")
		dataList = formattedHtml.split(",")
		response.close()
		return dataList

def getURFGameData():
	startDate = 1427846400
	endDate = 1429056000
	devKey = ""
	outFile = open("urf-game-data", "wb")
	for date in range(startDate, endDate, 300):
		time.sleep(1)
		q = Query("na", date, devKey)
		data = q.fetchData()
		outStr = str(date) + "\t" + "\t".join(data) + "\n"
		outFile.write(outStr)
		print date, datetime.datetime.fromtimestamp(date).strftime('%Y-%m-%d %H:%M:%S'), len(data)
	outFile.close()
	
if __name__ == "__main__":
	pass
