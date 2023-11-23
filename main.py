from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Sample data to simulate a database
books = [
    {'id': 1, 'title': 'Book 1', 'author': 'Author 1'},
    {'id': 2, 'title': 'Book 2', 'author': 'Author 2'},
    # Add more books here
]

# Routes for CRUD operations on books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({'books': books})

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify({'book': book})
    return jsonify({'message': 'Book not found'}), 404

@app.route('/books', methods=['POST'])
def create_book():
    new_book = request.get_json()
    if not new_book or 'title' not in new_book or 'author' not in new_book:
        abort(400)  # Bad request if title or author is missing
    new_book['id'] = len(books) + 1
    books.append(new_book)
    return jsonify({'message': 'Book created successfully', 'book': new_book}), 201

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if not book:
        return jsonify({'message': 'Book not found'}), 404
    book_data = request.get_json()
    if not book_data:
        abort(400)  # Bad request if no data provided
    book.update(book_data)
    return jsonify({'message': 'Book updated successfully', 'book': book})

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    initial_length = len(books)
    books = [book for book in books if book['id'] != book_id]
    if initial_length != len(books):
        return jsonify({'message': 'Book deleted successfully'}), 200
    return jsonify({'message': 'Book not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)

   

