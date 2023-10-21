
from SQL import User
from ServerNetwork import network
from model.PDU import PDUTextmessage
import datetime
def Check_for_duplicate_callsigns(callsign):
    if callsign in network.newclients:
        return False
    else:
        return True
def appendPilot(tokens):
    pilot_data = {"cid": tokens[2],
    "callsign": tokens[0][3:],
    "realname": tokens[-1],
    "visual_range": 40,
                  }
    network.pilot_list[tokens[0][3:]] = pilot_data
def pilot_Login(tokens,client_address):
    userid = tokens[2]
    password = tokens[3]
    level = tokens[5]
    callsign = tokens[0][3:]
    if Check_for_duplicate_callsigns(callsign):
        network.Adduser_pool(callsign, client_address)
        user_data = User.connect.query_user(userid)
        if user_data != None:
            if password == user_data[1]:
                if int(level) <= int(user_data[2]):
                    if "#AP" in tokens[0]:
                        appendPilot(tokens)
                        # network.Native_send_data("$DISERVER:CLIENT:VATSIM FSD V3.13\r\n", client_address)
                        PDUTextmessage.server_message("Welcome to SKYline Dynamic Flight Server Python edition version 0.1",callsign)
                else:
                    PDUTextmessage.server_message("The rating is too high",callsign)
                    network.Disconnect_pool(callsign)

            else:
                PDUTextmessage.server_message("The account ID or password is incorrect", callsign)
                network.Disconnect_pool(callsign)
        else:
            PDUTextmessage.server_message("The account ID or password is incorrect", callsign)
            network.Disconnect_pool(callsign)
    else:
        PDUTextmessage.err_server_message("CallsignInUse", client_address, callsign)
        network.Disconnect_Native_pools(client_address)
# def AtcLogin(tokens,client_address):
#     callsign = tokens[0][3:]
#     appendAtc(tokens)
#     PDUTextmessage.server_message("Welcome to SKYline Dynamic Flight Server Python edition version 0.1", callsign)
#     network.send_data(f'''$CRSERVER:{callsign}:ATC:Y:{callsign}
# $CRSERVER:{callsign}:CAPS:ATCINFO=1:ICAOEQ=1:FASTPOS=1
# $CRSERVER:{callsign}:IP:{client_address[0]}
# ''',callsign)