from flask import Flask, render_template, request
from connections.designerDAO import DesignerDAO

from routes.designer_routes import designer_routes

app = Flask(__name__)

app.register_blueprint(designer_routes)


# region designer


# @app.route('/designer', methods=['PUT'])
# def updateDesigner():
#     id = request.args.get('id')
#     name = request.args.get('name')
#     d = DesignerDAO()
#     r = d.update_on_db(id, name)
#     return r


# @app.route('/designer', methods=['POST'])
# def insertDesigner():
#     d = DesignerDAO()
#     name = request.args.get('name')
#     r = d.insert_on_db(name)
#     return r


# @app.route('/designer', methods=['GET'])
# def getDesigner():
#     id = request.args.get('id')
#     d = DesignerDAO()
#     r = d.select_from_db(id)
#     if(r == "error"):
#         return "failed", 500

#     else:
#         return r


# @app.route('/designer', methods=['DELETE'])
# def deleteDesigner():
#     id = request.args.get('id')
#     d = DesignerDAO()
#     r = d.remove_from_db(id)
#     if(r == "success"):
#         return r
#     else:
#         return "failed", 500


# @app.route('/designers', methods=['GET'])
# def getAllDesigners():

#     d = DesignerDAO()
#     r = d.select_all_from_db()
#     print(r)

#     if(r == "error"):
#         return "failed", 500
#     else:
#         return r
# endregion

# region categoria

# endregion


if __name__ == '__main__':
    app.run(debug=True)
