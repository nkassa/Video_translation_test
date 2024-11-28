import time
import requests
import threading
import server
from client import Client

def start():
  # start and run server in separate thread.
  server.app.run(port=5001, debug=False)

def check_if_server_ready(url, timeout=30):

  # check if server running and ready
  start_time = time.time()
  while(timeout > (time.time()-start_time)):
    try:
      response = requests.get(url + "/status")
      if response.status_code == 200:
        print("Server ready")
        return True
    except requests.exceptions.RequestException as error:
      print(f"Error reaching server: {error}")
      # avoid excessive requests
      time.sleep(1)
  return False


def test():
  # start server in separate thread
  thread = threading.Thread(target=start, daemon=True)
  thread.start()

  # give time for server to start
  time.sleep(6)

  # time for server to start
  if check_if_server_ready(url = "http://localhost:5001", timeout=20):
    try:
      # initialize client 
      client = Client(url = "http://localhost:5001")
      # wait for server's response 
      success = client.check_if_server_ready()
      if not success:
        print("Test result: FAIL")
      else:
        print("Test result: SUCCESS")
    except requests.exceptions.RequestException as request_error:
      print(f"Interaction failed: {request_error}")
    except Exception as unexpected_error:
      print(f"Unexpected Error: {unexpected_error}")
  else:
    print("Server did not start")

  # server will end automatically when threat ends 
  print("Ending server...")

if __name__ == "__main__":
  test()


  
