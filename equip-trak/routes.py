from config import app
from controller_functions import root, register, addUser, checkUser, nav, newEquip, addEquipment

app.add_url_rule("/", view_func=root)
app.add_url_rule("/addUser", view_func=addUser, methods=['POST'])
app.add_url_rule('/register', view_func=register)
app.add_url_rule('/username', view_func=checkUser, methods=['POST'])
app.add_url_rule('/nav', view_func=nav)
app.add_url_rule('/newEquipment', view_func=newEquip)
app.add_url_rule('/addEquipment', view_func=addEquipment, methods=['POST'])

# app.add_url_rule("/addDojo", view_func=addDojo, methods=["POST"])
# app.add_url_rule("/addNinja", view_func=addNinja, methods=["POST"])
