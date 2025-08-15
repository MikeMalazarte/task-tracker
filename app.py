from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Temporary "database" in memory
tasks = []

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    task_name = request.form.get("task")
    if task_name:
        tasks.append({"name": task_name, "status": "Not Done"})
    return redirect("/")

@app.route("/delete/<int:task_id>")
def delete(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)