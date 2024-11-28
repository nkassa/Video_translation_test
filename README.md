# Video_translation_test

Prerequisites:

  Install requests library: 
    pip install requests

  Install flask library:
    pip install flask

Overview:
  Client class interacts with server API and checks status of task. The client library has these features:
    - Error Handling
    - Exponential Backoff: exponentially increases waiting time between retries until it reaches max waiting time to reduce unnecessay load on the server
    - Retries: checks status at different intervals and automatically retries if task is pending

Client:
  - Initialization (__init__):
    - initialize client with necessary parameters 
  - Check Status (check_status):
    - send GET request to server endpoint to get current status
    - return "pending" or "completed" or "error"
  - Check Server Readiness (check_if_server_ready)
    - repeatedly checks status and waits for task to be completed
    - use exponential backoff to change interval 
    - retries up to max tries
    - return successful or failure

Server:
  - simulate status returning "pending" or "completed" or "error" based on time passed


HOW to run:

Start the Server: 
  - open terminal and run server script to simulate task status
    
    "python server.py"

Run the test:
  - In another terminal, run test script to test client and server (make sure server is not running in other terminal)
  
    "python test.py"

Expected Output:
  - if executed sucessfully, you should see the following logs:
  
    "127.0.0.1 - - [28/Nov/2024 14:30:38] "GET /status HTTP/1.1" 200 -
    Server ready
    127.0.0.1 - - [28/Nov/2024 14:30:38] "GET /status HTTP/1.1" 200 -
    Translation completed SUCCESSFULLY!
    Test result: SUCCESS
    Ending server..."
