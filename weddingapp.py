import os
from flask import Flask, render_template, request, redirect
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("DB_NAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)


@app.route('/')
def welcome_page():
    return render_template('welcomepage.html')

@app.route('/venue')
def venue_page():
    return render_template('venue.html')

@app.route('/rsvp')
def rsvp_page():
    return render_template('rsvp.html')
    
@app.route('/contact_us')
def contactus_page():
    return render_template('contactus.html')
    
@app.route('/how_to_get_there')
def howtogetthere_page():
    return render_template('howtogetthere.html')





@app.route('/add_guest')
def add_guest():
    return render_template('addguest.html')

    
@app.route('/do_add_guest', methods=["POST"])
def do_add_guest():
    guest_details = request.form.to_dict()
    mongo.db.guests.insert_one(guest_details)
    return redirect("/")    

@app.route('/add_table')
def add_table():
    return render_template('addtable.html')  

@app.route('/do_add_table', methods=["POST"])
def do_add_table():
    table_name = request.form.to_dict()
    mongo.db.tables.insert_one(table_name)
    return redirect("/")    

@app.route('/add_diet')
def add_diet():
    return render_template('adddiet.html')  

@app.route('/do_add_diet', methods=["POST"])
def do_add_diet():
    diet_name = request.form.to_dict()
    mongo.db.diets.insert_one(diet_name)
    return redirect("/")    



if __name__ == "__main__":
    app.run(host=os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT", 8080)), debug=True)