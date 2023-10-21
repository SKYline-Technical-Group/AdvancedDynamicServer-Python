from model.PDU import PDUDisconnected, PDUPilotLogin,PDUTextmessage,PDUATCLogin

def data_judgment(tokens,raw_data,client_address):
    # ATC连接
    if "#AA" in tokens[0]:
        print("ATC连接")
        PDUATCLogin.atc_Login(tokens,client_address)
    if "#AP" in tokens[0]:
        print("飞行员连接")
        PDUPilotLogin.pilot_Login(tokens,client_address)
    if "#DA" in tokens[0]:
        PDUDisconnected.Userdisconnected(tokens)
    if "#TM" in tokens[0]:
        PDUTextmessage.Private_chat(tokens,raw_data)
