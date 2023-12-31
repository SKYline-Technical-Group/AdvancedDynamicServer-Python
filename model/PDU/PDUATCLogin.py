from ServerNetwork import network
from model.PDU import PDUTextmessage
import datetime
from SQL import User

def Check_for_duplicate_callsigns(callsign):
    if callsign in network.newclients:
        return False
    else:
        return True
def appendAtc(tokens):
    atcdata ={
            "cid": tokens[3],
            "name": tokens[2],
            "callsign": tokens[0][3:],
            "frequency": "199.998",
            "facility": 0,
            "rating": tokens[5],
            "server": "SKYline Technical Server",
            "visual_range": 50,
        #输出这种类型的时间2023-10-21 16:26:51
            "logon_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "latitude": tokens[9],
            "longitude":tokens[10]
        }
    network.atc_list[tokens[0][3:]] = atcdata




def atc_Login(tokens,client_address):
    network.Native_send_data("$DISERVER:CLIENT:VATSIM FSD V3.13\r\n", client_address)
    userid = tokens[3]
    password = tokens[4]
    level = tokens[5]
    callsign = tokens[0][3:]
    if Check_for_duplicate_callsigns(callsign):
        network.Adduser_pool(callsign, client_address)
        print("没有重复呼号")
        user_data = User.connect.query_user(userid)
        if user_data != None:
            if password == user_data[1]:
                if int(level) <= int(user_data[2]):
                    AtcLogin(tokens,client_address)
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
        print("有重复呼号")
        PDUTextmessage.err_server_message("CallsignInUse", client_address, callsign)
        network.Disconnect_Native_pools(client_address)
def AtcLogin(tokens,client_address):
    callsign = tokens[0][3:]
    appendAtc(tokens)
    PDUTextmessage.server_message("Welcome to SKYline Dynamic Flight Server Python edition version 0.1", callsign)
    network.send_data(f'''$CRSERVER:{callsign}:ATC:Y:{callsign}
$CRSERVER:{callsign}:CAPS:ATCINFO=1:ICAOEQ=1:FASTPOS=1
$CRSERVER:{callsign}:IP:{client_address[0]}
''',callsign)