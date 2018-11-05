# Kira-Wedding-App

It is an App that helps the client to organize and invite their guests, upload photos and view the photos uploaded
from a wedding party and ceremony.

This App also keepsrecord of that organization as all the data introduce in the App
will be storage in MongoDB.

## UX 
### Who is it for?

The potencial user of this application will be people who are planing theirwedding.

It is directed to people with basic knowledge on technology as the App is been kept simple and as clear as possible.
The customer is looking for using this app mostly on their desktop but it can be easily be use on their mobile device.
The customer in this case is looking for organise their wedding event as well as keep a memory from it.
The design is adaptable for any viewport too as you can see on the mockups I have atteched in the project.

### Structure and Design

All the design process was developed to create a full positive user experience.

The structure of the whole Website is:

1. Host focused:
        Home.  In this page the host can add their guests as well as the name of the tables and the diet requirements
               for each guest.
2. Guests focused:
        Venue. The guests will find the information they need about the venue where the event is taking place.

        How to get there.  This part of the app where guests can get direction of how to get to the venue.
                           In here i have added and embed google map that will hel the guest to use a live map.
                           
        Contact Us.  This section was createdto facilitate any of the host details that the guest might required in case they
                     need to contact the host.
                     
3. Guests and Host:

        Upload Images. This section was created so guest and host  can upload their images from the day.
        
        Photos.  In case any guests or hosts would like to see the images other people have uploaded.
        
##  Features

    In the home page we will find three buttons: Add Guest, Add diet and Add table.

    
* Feature 1
        The Add Guest button
        It takes the host into a form and this has to be fill in with the name, last name and email of the guest. Once
        the host presses the add guest submit button. The details of the guests will be kept in the data base, in the collection 
        Guest.
        At the same time the added guest will receive and email with a link.
        when the guest opens the link, he/she will opn a form where the guest name and with details to fill in:
        What table he would like to sit down and their diet requirements.

        Once the guest fills the form and hits the button I confim i will be there, the guest and their automatically will be 
        storage in the collection confirmed guests.
        
        In this way the host can go and check in the data of the collectin guests and the host will get all the detail straight 
        away with the extra details already filled in by the guest.
        
   
* Feature 2
        In the venue page i have added an image of the venue that when you click on it you can make it large.

* Feature 3
        In the how to get there section is a map from Google maps that allows the guests or users of the app to use the mapping service
        with interactive zooming and panning, the directions form the aiport to the venue, location details, etc.

* Feature 4
        When the client clicks on the  phone icon added in contact us section, this button automatically will try to open 
        any app already install in the device to try to make the phone call.

* Feature 5
        The button Image in the upload photo section allows the user to choose what file would like to upload to the app.
        Currently the user only can upload one image at the time. It's is a feature i am workin on at theminute.

* Feature 6
        When the user clisk on the Photos section, All the picures uploaded will be shown in a full size slider feature.

        
## Technologies Used

To construct this app I have used:
* Python
* Pymongo
* Flask
* MongoDB
* Materialize
* 

## Testing


## Deployment

I deployed this app using Heroku.


        





