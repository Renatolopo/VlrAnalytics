# %%
import requests
from bs4 import BeautifulSoup

# %%
r = requests.get('https://www.vlr.gg/stats')
soup = BeautifulSoup(r.content, 'html.parser')
table = soup.find_all('tr')
table
# %%
def get_info(player):
    """Retorna as informações dos players"""
    # nome dos players
    name = player.find('div', attrs={'class':'text-of'}).text
    # agentes que os players jogam
    agents = player.find('td', attrs={'class':'mod-agents'}).div.find_all('img')
    # quantidade de rounds jogados
    rdn = player.find('td', attrs={'class':'mod-rnd'}).text
    # pontuação media de combate
    acs = player.find('td', attrs={'class':'mod-color-sq mod-acs'}).text
    


# %%
for player in table:
    try:
        imgs = player.find('td', attrs={'class':'mod-color-sq mod-acs'}).text
        print(imgs)
        print('**')
    except:
        print('null')