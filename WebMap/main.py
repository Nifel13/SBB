from API_Request import getStation
from flask import Flask, render_template, request, redirect
from API_Request import getCarTrayectGeom, adress_to_coordinates
from Point import Point

app = Flask(__name__)



@app.route("/map", methods=["POST"])
def calculTrajecte():
    if request.method == "POST":
        if (not request.form["origin"] or not request.form["destination"]):
            return redirect("/",code=2)
        else:
        
            try:
                origin=Point(adress_to_coordinates(request.form['origin']))
                destination=Point(adress_to_coordinates(request.form['destination']))
            except:
                return redirect("/", code=2)
            jsonTraject = getCarTrayectGeom(origin, destination)
            return render_template("map.html", dataStruct=[adress_to_coordinates(request.form['origin']), adress_to_coordinates(request.form['destination']), jsonTraject, request.form['origin'], request.form['destination']])
    else:
        return redirect("/", code=1)


@app.route("/")
def index_init():
    return render_template("index.html", bitch_var="Yes BITCHHH")
'''
def carTrayectWeb(A,B):
    jsonTraject = getCarTrayectGeom(A,B)
    return render_template("index.html", jsonTraject_geom=jsonTraject)
'''



if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8083, debug=True)


