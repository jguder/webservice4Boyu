# webservice4Boyu
Web service and sample implementation for Boyu to integrate.

wiki-server.py
I recommend running my service in a virtual environment. After creating the virtual environment (virtualenv venv), install flask and the wikipedia-api. Then import wikipediaapi and socket (which is part of the python standard library). 
The file implements a socket server. Within this file, the only change you need to make is to change my email address to yours. The email address is required by wikipediaapi so they can track how many accesses you make in a day. There is a limit of 1000 per day. If you are not running on localhost or if you prefer to use a different port, you would need to change those number in this file as well as in your app.py file of your flask application.

app.py
This is my example code to add to your application to communicate with the server by sending requests and receiving data. 
Install flask if you haven't already, then import Flask, render_template, request, and jsonify, as well as socket.
In this file, there are really only two routes I am suggesting you add. Send_data receives the POST request from your html page's buttons and sends that query to the function send_to_server. Send_to_server manages the socket connection, sends the data to the server, and receives the summary in response, which it provides back to send_data, which sends it to the modal on the html page.

index.html
This is my simplified version of your web page, per the video you shared. I developed the modal (contrived pop-up looking display) with bootstrap, so there are some bootstrap elements to be aware of in this code. First ensure you include the bootstrap css in the page as I have. For each book, I'm recommending you add a button with the book's title as the data that is send upon push via a POST request. This is what will be sent to my server. You can really just copy the code I've provided and just change the name of each book title per each button. The section with all the divs is the modal, and that is what's calling the bootstrap css, so it's very important you have included those. You'll then see some javascript as well, which handles the data sending and receiving. 

We can talk through all of these items, but I hope this readme helps

UML Diagrams follow.
