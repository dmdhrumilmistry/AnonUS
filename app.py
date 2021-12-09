from flask import Flask, request, jsonify, redirect

import json
import string
import random
import os


app = Flask(__name__)
app.config['ENV'] = 'deployment'
shortened_links = dict()
json_shortened_links = None
base_url = "http://127.0.0.1:8000/" 
file_name = "shortened_links.json"

if os.path.exists(file_name):
    with open(file_name, 'r') as f:
        print("[*] Loading shortened links from saved file.")
        data = f.read()
        shortened_links = json.loads(data)

def generate_unique_link(link):
    pool = string.ascii_letters + string.digits
    short_url = ''.join(random.sample(pool, 6))
    if short_url in shortened_links:
        generate_unique_link(link)

    return short_url


@app.route('/', methods=["GET", "POST"])
def home():
    return jsonify({"Simple Anonymous URL Shortner":"Written by Dhrumil Mistry"})


@app.route('/new_link', methods=["POST"])
def generate_link():
    global base_url
    global shortened_links
    if request.method == "POST":
        try:
            link = request.json["link"]
            shortened_url = base_url + generate_unique_link(link)
            shortened_links[shortened_url] = link
            json_shortened_links = json.dumps(shortened_links, indent=3)
            with open(file_name, "w") as f:
                f.write(json_shortened_links)
            return jsonify({"shortened_url":shortened_url}), 200
        except Exception as e:
            print('[X] Exception :',e)
            return jsonify({'Error':'Invalid Data'}), 400

    return jsonify({'Error':'Invalid Request'}), 400


@app.route('/<short_link_code>', methods=["GET"])
def redirect_user(short_link_code):
    global shortened_links
    url = base_url + short_link_code
    if url in shortened_links:
        redirect_url = shortened_links[url]
        return redirect(redirect_url,301)
    return jsonify({"URL":"NOT FOUND"}), 404