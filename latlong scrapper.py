import requests
from bs4 import BeautifulSoup
import pandas as pd
import warnings
import time
warnings.filterwarnings('ignore')
# Base URL for Google Search
BASE_URL = "https://www.google.com/search?q="
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}


def get_data(sector):
    search_term = f"{sector} hyderabad latitude and longitude"
    response = requests.get(BASE_URL + search_term, headers=HEADERS)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        coordinates_div = soup.find("div", class_="Z0LcW t2b5Cf")
        if coordinates_div:
            return coordinates_div.text

df = pd.DataFrame(columns=["Sector", "Coordinates"])
i = 10
areas  =['Charminar', 'Golconda Fort', 'Hussain Sagar Lake',
       'Ramoji Film City', 'Nehru Zoological Park', 'Lumbini Park',
       'Salar Jung Museum', 'Birla Mandir', 'Qutb Shahi Tombs',
       'Chowmahalla Palace', 'Birla Planetarium', 'Public Gardens',
       'Laad Bazaar', 'Shilparamam', 'Hyderabad Central University',
       'Osmania University', 'Durgam Cheruvu', 'KBR National Park',
       'NTR Gardens', 'HITEC City (Cyberabad)', 'Ravindra Bharathi',
       'Secunderabad Railway Station', 'Nampally Railway Station',
       'Kachiguda Railway Station', 'Rajiv Gandhi International Airport',
       'Miyapur Metro Station', 'Ameerpet Metro Station',
       'Mahatma Gandhi Bus Station (MGBS)', 'Jubilee Bus Station (JBS)',
       'Madhapur Police Station', 'Sultan Bazar Police Station',
       'Airport Police Station', 'Assembly Metro Station',
       'Begumpet Metro Station', 'Bharat Nagar Metro Station',
       'Chaitanyapuri Metro Station', 'Chikkadpally Metro Station',
       'Dilsukhnagar Metro Station',
       'Dr. B. R. Ambedkar Balanagar Metro Station',
       'Durgam Cheruvu Metro Station', 'Erragadda Metro Station',
       'ESI Hospital Metro Station', 'Gandhi Bhavan Metro Station',
       'Gandhi Hospital Metro Station', 'Habsiguda Metro Station',
       'Hitec City Metro Station', 'Irrum Manzil Metro Station',
       'JBS Parade Ground Metro Station', 'JNTU College Metro Station',
       'Jubilee Hills Check Post Metro Station',
       'Khairatabad Metro Station', 'KPHB Colony Metro Station',
       'Kukatpally Metro Station', 'LB Nagar Metro Station',
       'Lakdi-ka-pul Metro Station', 'Madhapur Metro Station',
       'Malakpet Metro Station', 'Mettuguda Metro Station',
       'MG Bus Station Metro Station', 'Moosapet Metro Station',
       'Musarambagh Metro Station', 'Musheerabad Metro Station',
       'Nagole Metro Station', 'Nampally Metro Station',
       'Narayanaguda Metro Station', 'New Market Metro Station',
       'NGRI Metro Station', 'Osmania Medical College Metro Station',
       'Parade Ground Metro Station', 'Paradise Metro Station',
       'Peddamma Gudi Metro Station', 'Prakash Nagar Metro Station',
       'Punjagutta Metro Station', 'Raidurg Metro Station',
       'Rasoolpura Metro Station',
       'Road No. 5 Jubilee Hills Metro Station',
       'RTC X Roads Metro Station', 'S.R. Nagar Metro Station',
       'Secunderabad East Metro Station',
       'Secunderabad West Metro Station', 'Stadium Metro Station',
       'Sultan Bazaar Metro Station', 'Tarnaka Metro Station',
       'Taruni Madhura Nagar Metro Station', 'Uppal Metro Station',
       'Victoria Memorial Metro Station', 'Yusufguda Metro Station']
for sector in areas:
    if i % 50 ==0:
        time.sleep(10)
    coordinates = get_data(sector)
    df = df.append({"Sector": f"Sector {sector}", "Coordinates": coordinates}, ignore_index=True)
    print(sector,'---' , coordinates)


df.to_csv("hyderbad_places_latlong.csv", index=False)