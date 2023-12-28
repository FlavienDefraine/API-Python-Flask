import json
from flask import Flask, jsonify, request
app = Flask(__name__)

#Flavien DEFRAINE 3D Audiovisuel

@app.route('/')
def index():
    return jsonify({'message': 'home API avec les chiens'})

dog_list = {
    1 : {
        "id" : 0,
        "race" : "race0",
        "img" : "imgpath0"
    },
    2 : {
        "id" : 1,
        "race" : "race1",
        "img" : "imgpath1"
    },
}

#definition du endpoint
@app.route('/api/dogs', methods=["GET", "POST"])
def handle_books():
  if request.method == "GET":
    return jsonify( {'res': dog_list} )
  else:
    sent_data = request.json
    dog_array = list(dog_list.items())
    new_id = len(dog_array) + 1
    new_dog =   {
            "id": new_id,
            "race": request.json['race'] ,
            "img": request.json['img'],
        }
    dog_list[ int(new_id) ] = new_dog
    return {'New dog appeared : ': sent_data}, 201

#definition du endpoint
@app.route('/api/dogs/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def dogs(id):
    if request.method == 'GET':
        return jsonify({"resultat": dog_list.get(id)}), 200
    
    elif  request.method == 'PUT':
        new_race = request.json.get('race')
        new_img = request.json.get('img')

        if new_race:
          dog_list[int(id)].update({"race": new_race})
        if new_img:
          dog_list[int(id)].update({"img": new_img})

        return { "New dog appeared :') :": dog_list[int(id)] }, 202
    elif  request.method == 'DELETE':
        dog_list.pop(int(id))
        return { "resultat": f"Dog, id: {id} deleted :'( " }, 202

app.debug = True
app.run()