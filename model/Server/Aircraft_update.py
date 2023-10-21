from model.PDU import PDUPilotPosition

def Aircraft_update(tokens,raw_data):
    PDUPilotPosition.Broadcast_location_Pilot(tokens,raw_data)