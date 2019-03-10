import os
from flask import Flask, render_template, request, redirect
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from base64 import b64encode
from flask_mail import Mail
from flask_mail import Message
import base64



app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("DB_NAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")


app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=587
app.config['MAIL_USE_TLS']=True
app.config['MAIL_USERNAME']=os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD']=os.environ.get('EMAIL_PASS')

mail = Mail(app)
mongo = PyMongo(app)


# initial route
@app.route('/')
def welcome_page():
    return render_template('welcomepage.html')

# Route to venue section
@app.route('/venue')
def venue_page():
    return render_template('venue.html')

# Route to rsvp section with the unique id of the guest
@app.route('/rsvp/<guest_id>')
def rsvp_page(guest_id):
    if ObjectId.is_valid(guest_id):
        
        guest = mongo.db.guests.find_one({'_id': ObjectId(guest_id)})
        if guest is None:
            return redirect('/')
        table = mongo.db.tables.find()
        diet = mongo.db.diets.find()
        return render_template('confirmed.html', guest=guest, table=table, diet=diet)
    return redirect("/")
    
# This is the route that add the confirmed guests to the data base. 
# After it will redirect the client to the main url/
@app.route('/do_add_confirmed_guests')
def do_add_confirmed_guests():
    confirmed_guests= request.form.to_dict()
    mongo.db.confirmed_guests.insert_one(confirmed_guests)
    return redirect("/")    
    
#This route is to the contact_us page   
@app.route('/contact_us')
def contactus_page():
    return render_template('contactus.html')

#This route is to the How to get there page 
@app.route('/how_to_get_there')
def howtogetthere_page():
    return render_template('howtogetthere.html')
    
    
#This route is to the upload photos page     
@app.route('/upload_photos')
def uploadphotos_page():
       return render_template('uploadimages.html')

# This is the route when we upload the photos into the Data Base,
# once is done it will redirect the client to the main page, "/"
@app.route('/do_upload_photos',methods=["POST"])
def do_upload_photos():
       image = request.files['image']
       image_string = base64.b64encode(image.read()).decode("utf-8")
       form_values = request.form.to_dict()
       form_values["image"] = "data:image/png;base64," + image_string
      
       
       mongo.db.images.insert_one(form_values)
       
       return redirect('/')

# this route allow the user to view the uploaded photos   
@app.route('/view_photos_uploaded')
def view_photos_uploaded_page():
    images = mongo.db.images.find()
    return render_template('viewphotosuploaded.html', images=images)
        

# This route redirects the guests confirmed to the main url, home page.
@app.route('/confirmed_guests')
def confirmed_guests():
    return redirect('/') 
    
    
@app.route('/add_guest')
def add_guest():
    return render_template('addguest.html')

# During this route the added guests will be posted in the MLab that they are confirmed to attend
# An email is sent to the guest too
@app.route('/do_add_guest', methods=["POST"])
def do_add_guest():
    guest_details = request.form.to_dict()
    _id = mongo.db.guests.insert(guest_details)
    print(_id)
    msg = Message("RSVP to the wedding",
    sender="kiraandbillwedding@gmail.com",
    recipients=[guest_details["email"]])
    msg.body="http://kira-wedding-app-kiranleu.c9users.io:8080/rsvp/"+str(_id)
    mail.send(msg)
    
    return redirect("/")    

# Route to add table
@app.route('/add_table')
def add_table():
    return render_template('addtable.html')  
    
# Route table is added to Mlab 
@app.route('/do_add_table', methods=["POST"])
def do_add_table():
    table_name = request.form.to_dict()
    mongo.db.tables.insert_one(table_name)
   
    return redirect("/")   
    
# Route to add diet
@app.route('/add_diet')
def add_diet():
    return render_template('adddiet.html')  

# When the new diet is been added to the DataBase
@app.route('/do_add_diet', methods=["POST"])
def do_add_diet():
    diet_name = request.form.to_dict()
    mongo.db.diets.insert_one(diet_name)
    return redirect("/")    



if __name__ == "__main__":
    app.run(host=os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT", 8080)), debug=True)