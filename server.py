import time
from flask import Flask, jsonify


app = Flask(__name__)

# start time of application
start_time = time.time()
# 8 sec configuration delay (time to finish job/task)
configuration_time = 8

# server name config
app.config['SERVER_NAME'] = 'localhost:5000'

# use GET requests 
@app.route('/status')
def get_status():
  # calculate time passed 
  time_passed = time.time() - start_time
  # create error threshold 
  complete_time_threshold = configuration_time
  error_time_threshold = complete_time_threshold + 4 

  # pending 
  if time_passed < complete_time_threshold:
    status = "pending"
  # completed 
  elif time_passed < error_time_threshold:
    status = "completed"
  # else error 
  else:
    status = "error"
  # return result
  return jsonify({"result": status})


if __name__ == '__main__':
    app.run()
