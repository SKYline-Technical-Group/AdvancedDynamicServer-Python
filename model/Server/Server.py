from model.Server import Aircraft_update, ATC_update,Requests,clients_or_messages


def command(tokens,client_address):
    if "$" in tokens[0]:
        Requests.Requests(tokens)
    if "#" in tokens[0]:
        clients_or_messages.data_judgment(tokens,client_address)
    if "@" in tokens[0]:
        Aircraft_update.Aircraft_update(tokens)
    if "%" in tokens[0]:
        ATC_update.atc_pposition(tokens)




