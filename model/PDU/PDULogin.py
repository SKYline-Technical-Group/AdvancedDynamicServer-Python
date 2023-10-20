from SQL import User
from ServerNetwork import network
from model.PDU import PDUTextmessage
import datetime
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
            "logon_time": datetime.UTC
        }
    network.atc_list[tokens[0][3:]] = atcdata
def UserLogin(tokens,client_address):
    print("判断连接")
    userid = tokens[3]
    password = tokens[4]
    level = tokens[5]
    callsign = tokens[0][3:]
    print("加入连接池")
    network.send_data("$DISERVER:CLIENT:VATSIM FSD V3.13\r\n",callsign)
    user_data = User.connect.query_user(userid)
    print("查询用户数据",user_data)
    if user_data != None:
        if password == user_data[1]:
            if int(level) <= int(user_data[2]):
                if "#AA" in tokens[0]:
                    network.Adduser_pool(callsign,client_address)
                    appendAtc(tokens)
                    PDUTextmessage.server_message("Welcome to SKYline Dynamic Flight Server Python edition version 0.1",callsign)
                if "#AP" in tokens[0]:
                    network.Adduser_pool(callsign, client_address)
                    PDUTextmessage.server_message("Welcome to SKYline Dynamic Flight Server Python edition version 0.1",callsign)
            else:
                network.Adduser_pool(callsign, client_address)
                PDUTextmessage.server_message("The rating is too high",callsign)
                network.Deluser_pool(callsign)
        else:
            network.Adduser_pool(callsign, client_address)
            PDUTextmessage.server_message("The account ID or password is incorrect", callsign)
            network.Deluser_pool(callsign)
    else:
        network.Adduser_pool(callsign, client_address)
        PDUTextmessage.server_message("The account ID or password is incorrect", callsign)
        network.Deluser_pool(callsign)
