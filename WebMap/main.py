from API_Request import getStation
from flask import Flask, render_template, request, redirect, json
from API_Request import getCarTrayectGeom, adress_to_coordinates
from Point import Point
from journeyAdria import findJourney

app = Flask(__name__)


@app.route("/map", methods=["POST"])
def calculTrajecte():
    if request.method == "POST":
        if (not request.form["origin"] or not request.form["destination"]):
            return redirect("/",code=2)
        else:
        
            try:
                origin=adress_to_coordinates(request.form['origin'])
                destination=adress_to_coordinates(request.form['destination'])
            except:
                return redirect("/", code=2)
            megalista = findJourney(origin, destination)
            listaCoords = megalista[0]
            tiempototal = megalista[1]
            listaCoords[1][0], listaCoords[1][1] = listaCoords[1][1], listaCoords[1][0]
            listaCoords[4][0], listaCoords[4][1] = listaCoords[4][1], listaCoords[4][0]


            return render_template("map.html", dataStruct=[adress_to_coordinates(request.form['origin']), adress_to_coordinates(request.form['destination']), listaCoords, request.form['origin'], request.form['destination']])
    else:
        return redirect("/", code=1)


@app.route("/")
def index_init():
    return render_template("index.html")
'''
def carTrayectWeb(A,B):
    jsonTraject = getCarTrayectGeom(A,B)
    return render_template("index.html", jsonTraject_geom=jsonTraject)
'''



if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8009, debug=True)


