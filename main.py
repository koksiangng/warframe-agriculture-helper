import requests
import PySimpleGUI as psg
import pandas as pd
from bs4 import BeautifulSoup

link = "https://n8k6e2y6.ssl.hwcdn.net/repos/hnfvc0o3jnfvc873njb03enrf56.html"
name = "Warframe Agriculture Helper"
soup = BeautifulSoup(requests.get(link).text, "lxml")

last_update_date = soup.find('p')
last_update_date.b.decompose()
print("Last update: {0}".format(last_update_date.text.strip()))

print('========================')

all_tables = soup.find_all('table')
#print(all_tables)
df = pd.read_html(str(all_tables[0]))[0]
df.to_csv(r'missions.csv')
df = pd.read_html(str(all_tables[1]))[0]
df.to_csv(r'relics.csv')
df = pd.read_html(str(all_tables[2]))[0]
df.to_csv(r'keys.csv')

#sg.Window(title="Hello World", layout=[[]], margins=(100, 50)).read()
WindowLayout = [[psg.Combo(["test", "potato"], size = (50, 20))], [psg.Text("Hello from PySimpleGUI")], [psg.Button("OK")]]
psg.Window(title=name, layout=WindowLayout, margins=(300, 200)).read()


#Could be disected more.
# df = pd.read_html(str(all_tables[3]))[0]
# df.to_csv(r'C:\Users\Sigge\Documents\Programmingprojects\Warframe-agriculture-helper\dynamic_location.csv')

# df = pd.read_html(str(all_tables[4]))[0]
# df.to_csv(r'C:\Users\Sigge\Documents\Programmingprojects\Warframe-agriculture-helper\sorties.csv')
# df = pd.read_html(str(all_tables[5]))[0]
# df.to_csv(r'C:\Users\Sigge\Documents\Programmingprojects\Warframe-agriculture-helper\cetus_bounties.csv')
# df = pd.read_html(str(all_tables[6]))[0]
# df.to_csv(r'C:\Users\Sigge\Documents\Programmingprojects\Warframe-agriculture-helper\orb_vallis_bounties.csv')
# df = pd.read_html(str(all_tables[6]))[0]
# df.to_csv(r'C:\Users\Sigge\Documents\Programmingprojects\Warframe-agriculture-helper\cambion_drift_bounties.csv')
# df = pd.read_html(str(all_tables[7]))[0]
# df.to_csv(r'C:\Users\Sigge\Documents\Programmingprojects\Warframe-agriculture-helper\zariman_drift_bounties.csv')
# df = pd.read_html(str(all_tables[8]))[0]
# df.to_csv(r'C:\Users\Sigge\Documents\Programmingprojects\Warframe-agriculture-helper\mod_drop_by_source.csv')
# df = pd.read_html(str(all_tables[9]))[0]
# df.to_csv(r'C:\Users\Sigge\Documents\Programmingprojects\Warframe-agriculture-helper\mod_drop_by_mods.csv')
# df = pd.read_html(str(all_tables[10]))[0]
# df.to_csv(r'C:\Users\Sigge\Documents\Programmingprojects\Warframe-agriculture-helper\bp-or-parts_by_source.csv')
# df = pd.read_html(str(all_tables[11]))[0]
# df.to_csv(r'C:\Users\Sigge\Documents\Programmingprojects\Warframe-agriculture-helper\bp-or-parts_by_item.csv')
# df = pd.read_html(str(all_tables[12]))[0]
# df.to_csv(r'C:\Users\Sigge\Documents\Programmingprojects\Warframe-agriculture-helper\resource_drops_by_source.csv')
# df = pd.read_html(str(all_tables[13]))[0]
# df.to_csv(r'C:\Users\Sigge\Documents\Programmingprojects\Warframe-agriculture-helper\additional_item_drops_by_source.csv')

# print(len(all_tables))