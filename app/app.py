from flask import Flask
import json_logging, logging
import sys

app = Flask(__name__)
app.config['SECRET_KEY'] = 'stam'

json_logging.init_flask(enable_json=True)
json_logging.init_request_instrument(app)
logging.basicConfig(level=logging.DEBUG, stream=sys.stdout, format='%(asctime)s %(levelname)s %(message)s')

from views import views
app.register_blueprint(views, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=3000) #TODO: off in production