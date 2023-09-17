from flask import Flask, request

todo_list = [{
    "title": "Create git repository"
}
]
app = Flask(__name__)

@app.get("/todos")
def get_todos():
    return todo_list,200


@app.post("/todos")
def create_todo():
    data = request.get_json()
    new_todo = {"title": data["title"]}
    todo_list.append(new_todo)
    return new_todo, 201
    