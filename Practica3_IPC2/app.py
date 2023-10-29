from flask import Flask, request, jsonify

app = Flask(__name__)

movies = []

# Endpoint para agregar una película
@app.route('/api/new-movie', methods=['POST'])
def add_movie():
    data = request.get_json()
    movie_id = data.get('movieId')
    name = data.get('name')
    genre = data.get('genre')

    if not movie_id or not name or not genre:
        return jsonify({"message": "Faltan datos obligatorios"}), 400

    movies.append({"movieId": movie_id, "name": name, "genre": genre})

    return jsonify({"message": "Película agregada con éxito"})

@app.route('/api/all-movies-by-genre/<genre>', methods=['GET'])
def get_movies_by_genre(genre):
    filtered_movies = [movie for movie in movies if movie['genre'] == genre]
    return jsonify(filtered_movies)

@app.route('/api/update-movie', methods=['PUT'])
def update_movie():
    data = request.get_json()
    #next() retorna el primer elemento que cumpla con la condición, aprendido de la documentación
    movie = next((movie for movie in movies if movie['movieId'] == data['movieId']), None)
    if movie:
        movie['name'] = data['name']
        movie['genre'] = data['genre']
        return jsonify({'message': 'La película fue actualizada con éxito'})
    else:
        return jsonify({'message': 'La película no se encontró'})

if __name__ == '__main__':
    app.run()
