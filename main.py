"""The main server starting script"""

import os
from gemini_service import gemini_service
from flask import Flask, send_file

app = Flask(__name__)

@app.route("/gemini")
def gemini():
    return gemini_service.get_response("Explain how AI works in less than 20 words")

@app.route("/")
def index():
    return send_file('src/index.html')

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()
