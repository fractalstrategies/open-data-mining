
import os
import sys
import requests

os.system('cls')

def main():

	greeting()
	config = get_config()
	datasets = get_datasets()
	dataset = validate_input('datasets', 1)
	print_config(config)

	request = make_request(config)


	response = get_request(request)
	print_status_code(response)
	print_headers(response)
	print_content(response)


def validate_input(input_type, position):
	try:
		i = sys.argv[1]
	except:
		i = ''
	while i is None or i == '':
		i = input('Please enter a dataset: ')

def write_to_file():
	with open('output/testing.out','w') as outfile:
		outfile.write('Jello world')

def print_content(response):
	print response.content

def print_headers(response):
	print response.headers

def print_status_code(response):
	print response.status_code

def get_request(request):
	return requests.get(request)

def make_request(config):
	request = ''
	request += config['root_url'] + get_dataset('crime') + '.' + config['output_type'] + '?'
	if config['limit'] != 0:
		request += '$limit=' + str(config['limit'])
	return request

def print_config(config):
	for c in config:
		print 'INFO: Config ' + c + ': ' + str(config[c])

def get_datasets():
	return {
		'public_employees': 'xzkq-xp2w',
		'crimes': 'ijzp-q8t2',
		'crimes2': '5cd6-ry5g',
		'building_permits': 'ydr8-5enu',
		'rental_housing': 's6ha-ppgi',
		'business_licenses': 'uupf-x98q',
		'food_inspections': '4ijn-s7e5',
		'street_names': 'i6bp-fvbx',
		'building_violations': '22u3-xenr',
		'police_stations': 'z8bn-74gv',
		'crimes_map': 'dfnk-7re6',
		'city_land': 'aksk-kvfp',
		'pot_holes': '7as2-ds3y',
		'public_transport': '97wa-y6ff',
		'problem_landlord': 'dip3-ud6z',
		'towed_vehicles': 'ygr5-vcbg',
		'payments': 's4vu-giwb',
		'street_lights': '3aav-uy2v',
		'red_light_violations': 'spqx-js37'
	}

def get_config():
	return {
		'root_url': 'https://data.cityofchicago.org/resource/',
		# 'dataset': 'alternative-fuel-locations',
		'dataset': '',
		'output_type': 'json',
		'limit': 1,
		'city': 'Chicago',
		'output_dir': 'output'
	}

def greeting():
	print 'INFO: ' + ' '.join(sys.argv)
	print 'INFO: Running Chicago Data Analysis'

if __name__ == '__main__':
	main()