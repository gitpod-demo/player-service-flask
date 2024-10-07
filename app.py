from flask import Flask, jsonify

app = Flask(__name__)

# Sample data
players = [
{'id': 1, 'nameFirst': 'Intuit', 'nameLast': 'Is Life'},
{'id': 2, 'nameFirst': 'Eric', 'nameLast': 'Fa'},
{'id': 3, 'nameFirst': 'Alice', 'nameLast': 'Smith'},
]

# Get all players
@app.route('/v1/players', methods=['GET'])
def get_players():
	return jsonify(players)

# Get a specific player by ID
@app.route('/v1/players/<int:player_id>', methods=['GET'])
def get_player(player_id):
	player = [player for player in players if player['id'] == player_id]
	if player:
		return jsonify(player[0])
	else:
		return jsonify({'message': 'player not found'}), 404

if __name__ == '__main__':
	app.run(debug=True)