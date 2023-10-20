import requests
from ServerNetwork import network
def Metar(tokens):
    icao = tokens[-1]
    print(icao)
    callsign = tokens[0][3:]
    url = f"https://metar.vatsim.net/metar.php?id={icao}"
    metar = requests.get(url=url).text
    network.send_data(f"$ARserver:{callsign}:METAR:{metar}\r\n",callsign)
