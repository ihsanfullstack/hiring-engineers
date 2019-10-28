
import logging
import sys

# Get the Datadog agent’s ip address
# from datadog.dogstatsd import route
# hostname=route.get_default_route()
 
# Connect the APM to the agent
from ddtrace import tracer, patch_all
# tracer.configure(hostname=hostname)
 
# Activate the APM
patch_all()

from flask import Flask
# Have flask use stdout as the logger
main_logger = logging.getLogger()
main_logger.setLevel(logging.DEBUG)
c = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c.setFormatter(formatter)
main_logger.addHandler(c)

app = Flask(__name__)

@app.route('/')
def api_entry():
    return 'Entrypoint to the Application'

@app.route('/api/apm')
def apm_endpoint():
    return 'Getting APM Started'

@app.route('/api/trace')
def trace_endpoint():
    return 'Posting Traces'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5050')