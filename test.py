from time import time as Time
import requests
import threading
import server
from client import Client

def start():
  # start and run server in separate thread.
  server.app.run(port=5000, reloader=False)

def check_if_server_ready(url, timeout=25):

  # check if server running and ready
  start_time = Time()
  while(timeout > (Time()-start_time)):
    try:
      response = requests.get(url)
      if response.status_code == 200:
        return True
    except requests.exceptions.RequestException as error:
      print(f"Error reaching server: {error}")
  return False


def test():
  # start server in separate thread
  thread_server = threading.Thread(target=start, daemon=True)
  thread_server.start()

  # time for server to start
  if check_if_server_ready(url = "http://localhost:5000"):
    try:
      # initialize client 
      client = Client(url = "http://localhost:5000")
      # wait for server's response 
      result = client.process_of_completion(timeout = 25)
      if result == False:
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


  
