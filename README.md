webservice4Boyu
Web service and sample implementation for Boyu to integrate. Please note that all of what is described below is contained within this git's code and is available to you. The code in this git is exactly what I used to model the micro service in my video, so it should be 100% usable for you to copy into your own application, and it should all work.

How to programmatically request data:

index.html file:
This is my simplified version of your web page, modeled from the video you shared. For each book, I'm recommending you add a button with the book's title as the data that is sent upon pushing it via a POST request. Example: 

     <p>Sample version of app for testing micro service.</p>
    <ul>
        <li>Little Women <button onclick="sendData('Little Women')">Summary</button></li>
        <li>The Little Prince <button onclick="sendData('The Little Prince')">Summary</button></li>
    </ul>

In the script section of the same page, this translates to a POST request:

    <script>
        function sendData(data) {
            fetch('/send_data', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ data: data })
            })

This request is then handled in the app.py file, which contains two relevant routes: /send_data and send_to_server. The send_data file fields the POST request, packages up the book title and passes it to send_to_server to pass to my microservice. 

@app.route('/send_data', methods=['POST'])
def send_data():
    data = request.get_json()
    if data and 'data' in data:
        book_title = data['data']
        retdata = send_to_server(book_title)
        return jsonify({'success': True, 'data': retdata})
    else:
        return jsonify({'success': False, 'error': 'No data provided.'})

The send_to_server route establishes the socket connection with my server, passes the data, and then receives the data back as well.

def send_to_server(data):
    HOST = "127.0.0.1"  # The server's hostname or IP address
    PORT = 65432  # The port used by the server

    # Establish a socket connection and send the data
    try:
        #SENDS DATA VIA OPEN SOCKET
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((HOST, PORT))
            sock.sendall(data.encode('utf-8'))
             #RECEIVES DATA BACK FROM WEB SERVICE AND RETURNS IT
            retdata = sock.recv(4096)   
            retdata = retdata.decode('utf-8')
            return retdata
    except Exception as e:
        print(f"Error sending data: {str(e)}").

How to programmatically receive data:

After it returns the data to send_data (the retdata = sock.recv(4096) above is when it receives the data back from the web socket, and return retdata is the returning to send_date), send_data returns it via jsonify statement to the requesting html page (index.html in my example code). In this file, a modal manages the data and displays it via popup.

<div class="modal" id="resultsModal" tabindex="-1" role="dialog">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">Results</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    <p id="modalContent"></p>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                </div>
            </div>
        </div>
    </div>

    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.1/dist/umd/popper.min.js" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" crossorigin="anonymous"></script>

    <script>
        function sendData(data) {
            fetch('/send_data', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ data: data })
            })
            .then(response => {
                if (response.ok) {
                    return response.json();
                } else {
                    console.error('Failed to send data.');
                }
            })
            .then(data => {
                // Check if data was successfully received
                if (data && data.success && data.data) {
                    // Populate the modal with the received data
                    document.getElementById('modalContent').textContent = data.data;
                    // Show the modal
                    $('#resultsModal').modal('show');
                } else {
                    console.error('Invalid data received.');
                }
            })
            .catch(error => {
                console.error('Error sending data:', error);
            });
        }
    </script>

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

