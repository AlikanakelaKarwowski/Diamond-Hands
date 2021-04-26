from model import *
plt.ion()
def makeModel(ticker):
	return MyModel(90, ticker, epochs=2, n_steps=50)

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

