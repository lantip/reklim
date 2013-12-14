from flask import Flask, request, jsonify
from roygbiv import *
#import json

app = Flask(__name__)

@app.route('/')
def reklim():
	source = request.args.get('url','')
	forma  = request.args.get('format','')
	if source:
		t    = Roygbiv(source)
		rgbs = t.get_palette_rgb()
		hexs = t.get_palette_hex()
		data = {}
		data["rgb"] = rgbs
		data["hex"] = hexs
		if forma == "rgb":
			return jsonify(rgb=rgbs)
		elif forma == "hex":
			return jsonify(hex=hexs)
		else:
			return jsonify(rgb=rgbs, hex=hexs)
	else:
		data = {"url": "" }
		return jsonify(data)

if __name__ == "__main__":
	app.run(host='geni.lantip.net', port=9000)
