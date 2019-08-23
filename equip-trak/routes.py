from config import app
from controller_functions import root, checkoutPage, register, addUser, checkUser, nav, newEquip, addEquipment, equipments, equipmentDetails, users, userDetails, transaction, login, getEquip, equipOut, equipIn, logout

app.add_url_rule("/", view_func=root)
app.add_url_rule('/nav', view_func=nav)
app.add_url_rule('/checkout', view_func=checkoutPage)

app.add_url_rule("/addUser", view_func=addUser, methods=['POST'])
app.add_url_rule('/register', view_func=register)
app.add_url_rule('/login', view_func=login, methods=['POST'])
app.add_url_rule('/logout', view_func=logout)

app.add_url_rule('/username', view_func=checkUser, methods=['POST'])
app.add_url_rule('/users', view_func=users)
app.add_url_rule('/users/<userId>', view_func=userDetails)


app.add_url_rule('/equipments', view_func=equipments)
app.add_url_rule('/equipments/<myId>', view_func=equipmentDetails)
app.add_url_rule('/equipments/new', view_func=newEquip)
app.add_url_rule('/equipments/add', view_func=addEquipment, methods=['POST'])
app.add_url_rule('/getEquip', view_func=getEquip, methods=['POST'])
app.add_url_rule('/equipOut', view_func=equipOut, methods=['POST'])
app.add_url_rule('/equipIn', view_func=equipIn, methods=['POST'])

app.add_url_rule('/transaction/<myId>', view_func=transaction)
