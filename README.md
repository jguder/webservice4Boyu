webservice4Boyu
Web service and sample implementation for Boyu to integrate. Please note that all of what is described below is contained within this git's code and is available to you. The code in this git is exactly what I used to model the micro service in my video, so it should be 100% usable for you to copy into your own application, and it should all work.

How to programmatically request data:

index.html file:
This is my simplified version of your web page, modeled from the video you shared. For each book, I'm recommending you add a button with the book's title as the data that is sent upon pushing it via a POST request. Example: 

[button](./button.png)

In the script section of the same page, this translates to a POST request:

[script POST](./index_post_send_data.png)


This request is then handled in the app.py file, which contains two relevant routes: /send_data and send_to_server. The send_data file fields the POST request, packages up the book title and passes it to send_to_server to pass to my microservice. 

[send data](./app_py_send_data.png)


The send_to_server route establishes the socket connection with my server, passes the data, and then receives the data back as well.

[send to server](./send_to_server.png)

How to programmatically receive data:

After it returns the data to send_data (the retdata = sock.recv(4096) above is when it receives the data back from the web socket, and return retdata is the returning to send_date), send_data returns it via jsonify statement to the requesting html page (index.html in my example code). In this file, a modal manages the data and displays it via popup. The following is the modal code itself.

[modal code](./modal_code.png)

And this code is the modal sending and receiving data to populate.

[modal code to send and receive](./modal_send_receive.png)

Other points to be aware of:
I developed the modal (contrived pop-up looking display) with bootstrap, so there are some bootstrap elements to be aware of in this code. First ensure you include the bootstrap css in the page as I have. 
You can really just copy the code I've provided and just change the name of each book title per each button. The section with all the divs is the modal, and that is what's calling the bootstrap css, so it's very important you have included those. As I said, the javascript handles the data sending and receiving. 


app.py contains all my example code to add to your application to communicate with the server by sending requests and receiving data. 
I know you used flask. To use this code in your app.py, import Flask, render_template, request, and jsonify, as well as socket.

wiki-server.py
This is my micro service. I recommend running it in a virtual environment. After creating the virtual environment (virtualenv venv), install flask and the wikipedia-api. Then import wikipediaapi and socket (which is part of the python standard library). 
The file implements a socket server. Within this file, the only change you need to make is to insert your email address where indicated in the file. The email address is required by wikipediaapi so they can track how many accesses you make in a day. THIS IS REALLY THE ONLY CHANGE YOU NEED TO MAKE TO THIS FILE: ENTER YOUR EMAIL ADDRESS ON LINE 14. There is a limit of 1000 per day. If you are not running on localhost or if you prefer to use a different port, you would need to change those number in this file as well as in your app.py file of your flask application.

We can talk through all of these items, but I hope this readme helps.

UML Sequence diagram follows.

[UML diagram](./UML.png)


