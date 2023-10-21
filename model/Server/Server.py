from model.Server import Aircraft_update, ATC_update,Requests,clients_or_messages


def command(tokens,raw_data,client_address):
    if "$" in tokens[0]:
        Requests.Requests(tokens,raw_data)
    if "#" in tokens[0]:
        clients_or_messages.data_judgment(tokens,raw_data,client_address)
    if "@" in tokens[0]:
        Aircraft_update.Aircraft_update(tokens,raw_data)
    if "%" in tokens[0]:
        ATC_update.atc_pposition(tokens,raw_data)




