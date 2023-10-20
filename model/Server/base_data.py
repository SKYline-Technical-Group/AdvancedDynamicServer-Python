from model.Server import Server
def split_data(data,client_address):
    #处理粘包
    datalist = data.split("\r\n")
    datalist.pop(-1)
    for i in datalist:
        try:
            New_data_format = i.split(":")
            print(New_data_format)
            Server.command(New_data_format,client_address)
        except:
            pass


