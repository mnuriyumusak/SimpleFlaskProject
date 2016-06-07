from flask import Flask, request
import postAdapter
app = Flask(__name__)


@app.route('/post', methods=['GET', 'POST', 'PUT', 'DELETE'])
def post():
    if request.method == 'GET':
        return postAdapter.show_database()
    elif request.method == 'POST':
        n = request.args.get('n')
        a = request.args.get('a')
        c = request.args.get('c')
        p = request.args.get('p')
        postAdapter.add_student(n, a, c, p)
        return "Added!"
    elif request.method == 'PUT':
        n = request.args.get('n')
        a = request.args.get('a')
        c = request.args.get('c')
        p = request.args.get('p')
        postAdapter.update(n, a, c, p)
        return "Changed!"
    elif request.method == 'DELETE':
        n = request.args.get('n')
        postAdapter.delete_row(n)
        return "Deleted!"
    else:
        return "Undefined method!"


@app.route('/post/<string:id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def post_with_id(id):
    if request.method == 'GET':
        return postAdapter.show_this_row(id)
    elif request.method == 'PUT':
        n = request.args.get('n')
        a = request.args.get('a')
        c = request.args.get('c')
        p = request.args.get('p')
        postAdapter.update_this(id, n, a, c, p)
        return "Changed!"
    elif request.method == 'DELETE':
        n = request.args.get('n')
        postAdapter.delete_row_this(id)
        return "Deleted!"
    else:
        return "Undefined method!"


if __name__ == "__main__":
    app.run()

