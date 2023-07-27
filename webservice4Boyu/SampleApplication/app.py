from flask import Flask, render_template, request, jsonify
import socket

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_data', methods=['POST'])
def send_data():
    data = request.get_json()
    if data and 'data' in data:
        book_title = data['data']
        retdata = send_to_server(book_title)
        return jsonify({'success': True, 'data': retdata})
    else:
        return jsonify({'success': False, 'error': 'No data provided.'})

def send_to_server(data):
    HOST = "127.0.0.1"  # The server's hostname or IP address
    PORT = 65432  # The port used by the server

    # Establish a socket connection and send the data
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((HOST, PORT))
            sock.sendall(data.encode('utf-8'))
            retdata = sock.recv(4096)
            retdata = retdata.decode('utf-8')
            return retdata
    except Exception as e:
        print(f"Error sending data: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
