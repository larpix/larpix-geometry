import json
io_groups = [1, 2]
io_channels = [i for i in range(33)]
chip_ids = [i for i in range(11, 112)]


net = {'network' : {}}
for io_group in io_groups:
	net['network'][io_group] = {}
	for io_channel in io_channels:
		net['network'][io_group][io_channel] = {}
		nodes = [ {"chip_id" : 'ext' }]
		for chip in chip_ids:
			nodes.append({'chip_id': chip})
		net['network'][io_group][io_channel]['nodes']=nodes


jsonString = json.dumps(net, indent=4)
jsonFile = open('agnostic-hydra.json', "w")
jsonFile.write(jsonString)
jsonFile.close()





