webservice4Boyu
Web service and sample implementation for Boyu to integrate. Please note that all of what is described below is contained within this git's code and is available to you. The code in this git is exactly what I used to model the micro service in my video, so it should be 100% usable for you to copy into your own application, and it should all work.

How to programmatically request data:

index.html file:
This is my simplified version of your web page, modeled from the video you shared. For each book, I'm recommending you add a button with the book's title as the data that is sent upon pushing it via a POST request. Example: 

<img width="841" alt="Screenshot 2023-07-28 at 4 18 37 PM" src="https://github.com/jguder/webservice4Boyu/assets/59512278/b90bfe03-b668-4635-b4ca-1f31162af971">

In the script section of the same page, this translates to a POST request:

<img width="493" alt="Screenshot 2023-07-28 at 4 19 13 PM" src="https://github.com/jguder/webservice4Boyu/assets/59512278/74cca468-99cc-41b6-8290-c14b68562486">


This request is then handled in the app.py file, which contains two relevant routes: /send_data and send_to_server. The send_data file fields the POST request, packages up the book title and passes it to send_to_server to pass to my microservice. 

<img width="723" alt="Screenshot 2023-07-28 at 4 19 28 PM" src="https://github.com/jguder/webservice4Boyu/assets/59512278/c7514a65-03c3-41f6-a799-e9cf7066e83e">


The send_to_server route establishes the socket connection with my server, passes the data, and then receives the data back as well.

<img width="647" alt="Screenshot 2023-07-28 at 4 19 54 PM" src="https://github.com/jguder/webservice4Boyu/assets/59512278/3f4f682b-31fe-41be-a02b-cc7062c61a6f">

How to programmatically receive data:

After it returns the data to send_data (the retdata = sock.recv(4096) above is when it receives the data back from the web socket, and return retdata is the returning to send_date), send_data returns it via jsonify statement to the requesting html page (index.html in my example code). In this file, a modal manages the data and displays it via popup. The following is the modal code itself.

<img width="1043" alt="Screenshot 2023-07-28 at 5 21 40 PM" src="https://github.com/jguder/webservice4Boyu/assets/59512278/10159055-68d1-48a8-b22d-78e14a0dea29">

And this code is the modal sending and receiving data to populate.

<img width="705" alt="Screenshot 2023-07-28 at 5 21 51 PM" src="https://github.com/jguder/webservice4Boyu/assets/59512278/289abe00-3a91-42d7-a340-eea963b9744e">

Other points to be aware of:
I developed the modal (contrived pop-up looking display) with bootstrap, so there are some bootstrap elements to be aware of in this code. First ensure you include the bootstrap css in the page as I have. 
You can really just copy the code I've provided and just change the name of each book title per each button. The section with all the divs is the modal, and that is what's calling the bootstrap css, so it's very important you have included those. As I said, the javascript handles the data sending and receiving. 


app.py contains all my example code to add to your application to communicate with the server by sending requests and receiving data. 
I know you used flask. To use this code in your app.py, import Flask, render_template, request, and jsonify, as well as socket.

wiki-server.py
This is my micro service. I recommend running it in a virtual environment. After creating the virtual environment (virtualenv venv), install flask and the wikipedia-api. Then import wikipediaapi and socket (which is part of the python standard library). 
The file implements a socket server. Within this file, the only change you need to make is to insert your email address where indicated in the file. The email address is required by wikipediaapi so they can track how many accesses you make in a day. There is a limit of 1000 per day. If you are not running on localhost or if you prefer to use a different port, you would need to change those number in this file as well as in your app.py file of your flask application.

We can talk through all of these items, but I hope this readme helps.

UML Sequence diagram follows.
![image](https://github.com/jguder/webservice4Boyu/assets/59512278/01d54899-cfa2-4bd7-8d06-8dcf3f011b4e)# 

