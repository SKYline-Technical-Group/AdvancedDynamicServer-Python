from model.PDU import PDULogin

def data_judgment(tokens,client_address):
    # ATC连接
    if "#AA" in tokens[0]:
        print("ATC连接")
        PDULogin.UserLogin(tokens,client_address)
