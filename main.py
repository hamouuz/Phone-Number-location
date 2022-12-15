import phonenumbers
from test import number
import folium 

# donne la localisation (pays)
from phonenumbers import geocoder
ch_number = phonenumbers.parse(number, "CH")
localisation = geocoder.description_for_number(ch_number, "fr")
print(localisation)

#donne l'operateur 
from phonenumbers import carrier
service_number = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_number, "fr"))

#trouver la localisation
from opencage.geocoder import OpenCageGeocode
clef = 'a89281cfa18d4448bd49007455d8367b'
coord = OpenCageGeocode(clef)
requete = str(localisation)
reponse = coord.geocode(requete)
lat = reponse[0]["geometry"]["lat"]
lng = reponse[0]["geometry"]["lng"]
print(lat, lng)

#creation de map
monMap = folium.Map(location=[lat, lng], zoom_start=12 )
folium.Marker([lat, lng], popup=localisation).add_to(monMap)
monMap.save("map.html")

