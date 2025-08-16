import datetime
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

default_tasks = [
    {"name": "Brush your teeth", "status": "Not Done"},
    {"name": "Wash your face", "status": "Not Done"},
    {"name": "Read a book", "status": "Not Done"},
    {"name": "Fix your bed", "status": "Not Done"},
    {"name": "Eat breakfast", "status": "Not Done"},
    {"name": "Study coding", "status": "Not Done"},
    {"name": "Create a reels", "status": "Not Done"},
    {"name": "Exercise", "status": "Not Done"},
    {"name": "Play a game", "status": "Not Done"}
]

tasks = default_tasks.copy()

last_reset_date = datetime.date.today()


@app.before_request
def reset_daily():
    global tasks, last_reset_date
    today = datetime.date.today()

    if today != last_reset_date:
        # New day → reset tasks
        tasks = default_tasks.copy()
        last_reset_date = today

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    task_name = request.form.get("task")
    if task_name:
        tasks.append({"name": task_name, "status": "Not Done"})
    return redirect("/")

@app.route("/done/<int:task_id>")
def done(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]["status"] = "Done"
    return redirect("/")

@app.route("/delete/<int:task_id>")
def delete(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)