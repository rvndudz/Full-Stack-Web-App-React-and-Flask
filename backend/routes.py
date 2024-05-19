from app import app, db
from flask import request, jsonify
from models import Friend

# For get all friends
@app.route('/api/friends', methods=['GET'])
def get_friends():
    friends = Friend.query.all()
    friends_json = [friend.to_json() for friend in friends]
    return jsonify(friends_json)

# For create a friend
@app.route('/api/friends', methods=['POST'])
def create_friend():
    try:
        data = request.json

        required_fields = ['name', 'role', 'gender']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing field: {field}"}), 400
        
        name = data.get('name')
        role = data.get('role')
        description = data.get('description')
        gender = data.get('gender')

        # fetch avatar from avatar-placeholder request
        if gender == 'male':
            image_url = f'https://avatar.iran.liara.run/public/boy?username={name}'
        else:
            image_url = f'https://avatar.iran.liara.run/public/girl?username={name}'

        new_friend = Friend(name=name, role=role, description=description, gender=gender, image_url=image_url)

        db.session.add(new_friend)
        db.session.commit()

        return jsonify(new_friend.to_json), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# delete a friend
@app.route('/api/friends/<int:id>', methods=['DELETE'])
def delete_friend(id):
    try:
        friend = Friend.query.get(id)
        if friend is None:
            return jsonify({"error": "Friend not found"}), 404
        
        db.session.delete(friend)
        db.session.commit()

        return jsonify({"msg":"It's working DELETE Request"}), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    

# update a friend
@app.route('/api/friends/<int:id>', methods=['PATCH'])
def update_friend(id):
    try:
        friend = Friend.query.get(id)
        if friend is None:
            return jsonify({"error": "Friend not found"}), 404

        data = request.json

        friend.name = data.get('name', friend.name)
        friend.role = data.get('role', friend.role)
        friend.description = data.get('description', friend.description)
        friend.gender = data.get('gender', friend.gender)

        db.session.commit()
        return jsonify(friend.to_json()), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500