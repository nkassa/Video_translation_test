import time
import requests

class Client:
  def __init__(self, url, max_tries = 5 , poll_interval = 2, max_poll_interval = 10):
    self.url = url
    self.max_tries = max_tries
    self.poll_interval = poll_interval
    self.max_poll_interval = max_poll_interval
  

  def check_status(self):
    try:
      # send HTTP GET request to server 
      response = requests.get(f"{self.url}/status", timeout= 6)
      # check HTTP status code 
      response.raise_for_status()
      # return "completed" or "pending" or "error"
      return response.json().get("result")
    except requests.exceptions.RequestException as error:
      print(f"Contacting server error: {error}")
      return None

  def check_if_server_ready(self):
    # initial poll interval and counter for # of tries
    poll = self.poll_interval
    tries = 0
    # retry until max # of tries
    while self.max_tries > tries:
      # check status
      status = self.check_status()
      # if pending wait and try again 
      if status == "pending":
        print(f"Translation pending, retrying in {poll} sec")
        # wait for polling interval
        time.sleep(poll)
        # make sure polling interval doesnt exceed max tries
        # by dynamically increasing polling interval, 
        # we minimize unnecessary calls to server preventing excessive loading and delayed responses
        poll = poll * 2
        if poll > self.max_tries:
          poll = self.max_tries
      # if completed then translation complete
      elif status == "completed":
        print(f"Translation completed SUCCESSFULLY!")
        # indicate success
        return True
      # if error then something went wrong
      elif status == "error":
        print(f"Translation Error.")
        # indicate failure
        return False
      # increment counter of tries
      tries = tries + 1

    # return false if max tries is exceeded
    print("Translation could not be determined")
    return False