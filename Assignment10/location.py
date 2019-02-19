import googlemaps

gmaps = googlemaps.Client(key='')

geocode_result = gmaps.geocode('Indiana University Showalter Fountain')
print(geocode_result[0]["geometry"]["location"])

reverse_geocode_result = gmaps.reverse_geocode((39.165341, -86.523588))
print(reverse_geocode_result[0]["formatted_address"])


#geocode_result = gmaps.geocode('Indiana University Luddy Hall')
#print(geocode_result[0]["geometry"]["location"])
#reverse_geocode_result = gmaps.reverse_geocode((39.1727, -86.5233))
#print(reverse_geocode_result[0]["formatted_address"])
