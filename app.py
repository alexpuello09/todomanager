from flask import Flask 

todo_list = [{"title": "Create git repository"

}

]
app = Flask(__name__)

@app.get("/todos")
def get_todos():
    return todo_list,200
    