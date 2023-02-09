//init db with user and notes collection. add test user with 2 notes
db.users.insert({ "name": "test", "email": "test@gamil.com", "password": "123456" })
let user = db.users.findOne({"name": "test"})
let id = user._id.toString()
db.notes.insert({ "text": "first test note", "user_id": id })
db.notes.insert({ "text": "second test note", "user_id": id })