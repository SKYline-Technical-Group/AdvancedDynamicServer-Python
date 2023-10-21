from model.PDU import PDUweather,PDUUserinfo,PDUFlightplan
def Requests(tokens,raw_data):
    if "$AX" in tokens[0]:
        PDUweather.Metar(tokens)
    if "$CQ" in tokens[0]:
        PDUUserinfo.Get_information(tokens,raw_data)
    if "$CR" in tokens[0]:
        PDUUserinfo.Recover_information(tokens,raw_data)
    if "$FP" in tokens[0]:
        PDUFlightplan.flight_plan(tokens,raw_data)
