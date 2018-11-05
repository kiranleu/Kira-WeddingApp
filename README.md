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


### Existing Features
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
        

* Feature 6
        When the user clisk on the Photos section, All the picures uploaded will be shown in a full size slider feature.

### Feautures to be implemented

* Feature 1

        A feature that will allow the user to upload more than one image at the same time.
        
        

## Technologies Used

To construct this app I have used:
* Python
* Pymongo
* Flask
* MongoDB
* Materialize
* Google Fonts
* Flask Mail
* Hover.css 


## Testing

#### Links

All the links included in the website have been tested and they are all working.

### Effects

Hover effects on icons, links and cards have been tested and they all have a hover effect working as expected. 

* Responsive The website have been tested in different viewports and it is responsve.

### Data Base

Since we are using MongoDB i had tested that the data is been storage in the expected collection
and this is working.

* Infomation Added by the host: Has been tested and passed.
* Information added by the guest: Has been tested and is working.

### Testing Email Sending feature

The feature has been tested and it is sending the email correctly with the correct link.

The link the user receives on the email has been tested and is working.

### Testing Images features

I had try to upload and image from a mobile phone and laptop and it had worked successfully.

The Images are being kept in the data base correctly.

The images that have been uploaded on the data base are shown in the Photos section. This has been tested and has passed it successful.


## Deployment

I deployed this app using Heroku ang GitHub.

Here is the link to the app:

[https://kira-wedding-app.herokuapp.com/]

## Credits

### Content

All the content from the Website is based on the clients Wedding. Some of the information, 
has been took from the actual venue website.

I also had used Google maps to embed it on the how to get there section.

Pictures and images used in the Website are been download from different google searches.






        





