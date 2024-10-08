import ollama
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

# Talk to Ollama test route
@app.route('/chat/ollama', methods=['GET'])
def chat_model():
	stream = ollama.chat(
    	model='tinyllama',
    	messages=[{'role': 'user', 'content': 'Why is the sky blue?'}],
    	stream=True,
	)
	for chunk in stream:
  		print(chunk['message']['content'], end='', flush=True)
	return "TEST"

if __name__ == '__main__':
	app.run(debug=True)