from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# JSON verilerini yükle
with open('countries.json', 'r') as file:
    jsonData = json.load(file)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city_name = request.form["city"]
        country_name = request.form["country"]
        year = request.form["year"]
        print(city_name)
        print(country_name)
        print(year)
        return render_template("index.html", analysisPage=True, cityName=city_name, year=year)
    return render_template("index.html", starterPage=True, jsonData=jsonData)

if __name__ == "__main__":
    app.run(port=3000)
