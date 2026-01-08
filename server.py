from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/jobb")
def jobb():
    q = request.args.get("q", "")
    params = {"q": q, "limit": 5, "sort": "pubdate-desc"}
    r = requests.get("https://jobsearch.api.jobtechdev.se/search", params=params)
    data = r.json()
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

