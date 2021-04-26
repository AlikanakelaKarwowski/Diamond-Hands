from model import *

def makeModel(ticker):
	return MyModel(90, ticker, epochs=25)

#DJI
AMZN = makeModel("AMZN")
TSLA = makeModel("TSLA")
NASDAQ = makeModel("^IXIC")
DJI = makeModel("^DJI")
AAPL= makeModel("AAPL")
MSFT = makeModel("MSFT")
NIO = makeModel("NIO")
NVDA = makeModel("NVDA")
FB = makeModel("FB")
TWTR = makeModel("TWTR")
WMT= makeModel("WMT")
SP500 = makeModel("^GSPC")
GME = makeModel("GME")

