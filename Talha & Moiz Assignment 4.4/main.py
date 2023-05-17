import json
import logging
import os

from flask import Flask, render_template, request
from logging import StreamHandler

 
app = Flask(__name__)
app.debug = os.environ.get("DEBUG") == "1" 


root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)
stream_handler = StreamHandler()
root_logger.addHandler(stream_handler)


TODO_FILE_NAME = "/app/todo_data/todo.json"  

if os.path.exists(TODO_FILE_NAME):
    with open(TODO_FILE_NAME) as f:
        TODO_ITEMS = json.load(f)
else:
    TODO_ITEMS = []


@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        content = request.form["content"]
        TODO_ITEMS.append(content)
        
        save_todo_items()

    return render_template("index.html", todo_items=TODO_ITEMS)


def save_todo_items():
    with open(TODO_FILE_NAME, "w") as f:
        json.dump(TODO_ITEMS, f)


if app.debug:
    app.logger.setLevel(logging.DEBUG)
    app.logger.debug("Debug mode is enabled.")
else:
    app.logger.debug("Debug mode is disabled.")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
