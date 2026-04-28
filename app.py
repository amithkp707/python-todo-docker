from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)
<<<<<<< HEAD

tasks = []

HTML = """
=======
tasks = []

html = """
>>>>>>> fdeca04b3a2cf6c3a40cae3873047b6aba337eac
<!DOCTYPE html>
<html>
<head>
    <title>Todo App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
        }
<<<<<<< HEAD
        h1 {
            color: #333;
        }
        form {
            margin-bottom: 20px;
        }
        input[type="text"] {
=======
        input {
>>>>>>> fdeca04b3a2cf6c3a40cae3873047b6aba337eac
            padding: 8px;
            width: 250px;
        }
        button {
            padding: 8px 12px;
<<<<<<< HEAD
            margin-left: 5px;
        }
        li {
            margin-bottom: 10px;
        }
        .done {
            text-decoration: line-through;
            color: gray;
        }
        a {
            margin-left: 10px;
            text-decoration: none;
            color: red;
=======
        }
        li {
            margin: 10px 0;
        }
        a {
            color: red;
            text-decoration: none;
            margin-left: 10px;
>>>>>>> fdeca04b3a2cf6c3a40cae3873047b6aba337eac
        }
    </style>
</head>
<body>
    <h1>My Todo List</h1>
<<<<<<< HEAD

=======
>>>>>>> fdeca04b3a2cf6c3a40cae3873047b6aba337eac
    <form method="POST" action="/add">
        <input type="text" name="task" placeholder="Enter a task" required>
        <button type="submit">Add Task</button>
    </form>
<<<<<<< HEAD

    <ul>
        {% for task in tasks %}
            <li>
                <span class="{% if task.done %}done{% endif %}">{{ task.name }}</span>
=======
    <ul>
        {% for task in tasks %}
            <li>
                {{ task }}
>>>>>>> fdeca04b3a2cf6c3a40cae3873047b6aba337eac
                <a href="/delete/{{ loop.index0 }}">Delete</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
"""

@app.route("/")
def home():
<<<<<<< HEAD
    return render_template_string(HTML, tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    task_name = request.form.get("task")
    if task_name:
        tasks.append({"name": task_name, "done": False})
    return redirect("/")

@app.route("/delete/<int:task_id>")
def delete(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
=======
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
>>>>>>> fdeca04b3a2cf6c3a40cae3873047b6aba337eac
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)