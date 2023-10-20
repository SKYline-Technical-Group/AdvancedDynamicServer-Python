from model.PDU import PDUweather
def Requests(data):
    if "$AX" in data[0]:
        PDUweather.Metar(data)