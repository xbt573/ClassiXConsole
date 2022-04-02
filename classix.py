#!/usr/bin/env python3

from requests_html import HTMLSession
import sys

session = HTMLSession()

servers = {
    "ttt": '46.174.55.192:27016',
    "murder": '46.174.55.192:27015',
    "prophunt": '46.174.55.192:27018',
    "minigames": '46.174.55.192:27017'
}

xpaths = {
    "players": '//*[@id="HTML_num_players"]',
    "map": '//*[@id="HTML_curr_map"]',
    "average": '//*[@id="HTML_avg_players"]',
    "serveraddress": '/html/body/div[2]/div[7]/div[1]/div[2]/text()[2]',
    "manager": '/html/body/div[2]/div[7]/div[1]/div[2]/a[3]'
}

def getstat(server: str) -> str:
    r = session.get(f'https://www.gametracker.com/server_info/{server}')
    output = ""
    
    output += "Players: " + r.html.xpath(xpaths["players"])[0].text + "\n"
    output += "Map: " + r.html.xpath(xpaths["map"])[0].text + "\n"
    if ("-v" in sys.argv):
        output += "Average (past month): " + r.html.xpath(xpaths["average"])[0].text + "\n"
        output += "Address: " + server + "\n"

    return output


    



def main():
    if (sys.argv[1] not in servers):
        print("Wrong server name")
        sys.exit(0)

    print(getstat(servers[sys.argv[1]]))

if __name__ == '__main__':
    main()