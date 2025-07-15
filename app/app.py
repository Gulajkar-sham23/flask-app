import os
import bugsnag
from bugsnag.flask import handle_exceptions

app = Flask(__name__)

# Configure Bugsnag
bugsnag.configure(
    api_key=os.getenv("BUGSNAG_API_KEY", ""),  # Use environment variable
    project_root="/app"
)

# Attach Bugsnag to Flask's exception handler
handle_exceptions(app)


@app.route('/')
def home():
    return "Hello from Flask with DevOps Pipeline and Bugsnag Monitoring!"

@app.route('/error')
def error():
    # This will trigger a Bugsnag error notification
    raise Exception("This is a test exception for Bugsnag!")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv("PORT", 5000)))
