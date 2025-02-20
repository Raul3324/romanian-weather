from urllib.request import urlopen
import json

url = "https://www.meteoromania.ro/wp-json/meteoapi/v2/starea-vremii"

# Datele arata in urmatorul mod:
# data este un dictionar cu cheile success, type, date, features
# ne intereseaza doar features si date
# features este o lista de 163 de orase indexate 0-162
# fiecare index reprezinta o lista care contine un singur dictionar cu cheile:
# type, geometry, properties
# ne intereseaza doar properties

def city_input(): # this function fetches the desired city from the user
	city = input("Enter desired city: ").upper()
	return city

city = city_input() # global variable needed for filter function

def load_data(url): # loads the dataset and keeps only what is needed
	url_opened = urlopen(url)
	data = json.load(url_opened)
	return data['features']

def find_city(tested): # function for filter
        # the program ignores the list and only looks at the single dictionary it contains
        if tested['properties']['nume'] == city:
                return True
        return False

def find_properties(features, city): # this function fetches the properties of the chosen city
	city_in_features = list(filter(find_city, features))
	properties = city_in_features[0]['properties']
	return properties

def output(properties): # and this function prints them nicely
	for key, value in properties.items():
		match key:
			case 'umezeala':
				print(f"{key}: {value}%")
			case 'zapada' | 'nebulozitate' | 'vant':
				print(f"{key}: {value}")
			case 'actualizat':
				date = value[0:10] + " " + value[-5:]
				print(f"{key}: {date}")
			case 'presiunetext':
				print(f"presiune: {value}")
			case 'tempe':
				print(f"temp: {value} C")

