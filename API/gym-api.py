import flask
import DatabaseConnection

Gym_API = flask.Flask(__name__)
Gym_API.config["DEBUG"] = True


@Gym_API.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

Gym_API.run()

if __name__ == '__main__':
    db = DatabaseConnection
    
    