from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)
tasks = []

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Todo App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
        }
        input {
            padding: 8px;
            width: 250px;
        }
        button {
            padding: 8px 12px;
        }
        li {
            margin: 10px 0;
        }
        a {
            color: red;
            text-decoration: none;
            margin-left: 10px;
        }
    </style>
</head>
<body>
    <h1>My Todo List</h1>
    <form method="POST" action="/add">
        <input type="text" name="task" placeholder="Enter a task" required>
        <button type="submit">Add Task</button>
    </form>
    <ul>
        {% for task in tasks %}
            <li>
                {{ task }}
                <a href="/delete/{{ loop.index0 }}">Delete</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html, tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    task = request.form["task"]
    tasks.append(task)
    return redirect("/")

@app.route("/delete/<int:index>")
def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)