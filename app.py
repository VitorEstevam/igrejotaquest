from flask import Flask, render_template, request
from connections.designerDAO import DesignerDAO

app = Flask(__name__)

# region designer


@app.route('/designer/<int:id>/<string:name>', methods=['PUT'])
def updateDesigner(id, name):
    d = DesignerDAO()
    r = d.update_on_db(id, name)
    if(r == "success"):
        return r
    else:
        return "failed", 500


@app.route('/designer/<string:name>', methods=['POST'])
def insertDesigner(name):
    d = DesignerDAO()
    r = d.insert_on_db(name)
    if(r == "success"):
        return r
    else:
        return "failed", 500


@app.route('/designer/<int:id>', methods=['GET'])
def getDesigner(id):
    d = DesignerDAO()
    r = d.select_from_db(id)
    if(r == "error"):
        return "failed", 500

    else:
        return r


@app.route('/designer/<int:id>', methods=['DELETE'])
def deleteDesigner(id):
    d = DesignerDAO()
    r = d.remove_from_db(id)
    if(r == "success"):
        return r
    else:
        return "failed", 500


@app.route('/designer', methods=['GET'])
def getAllDesigners():

    d = DesignerDAO()
    r = d.select_all_from_db()
    print(r)

    if(r == "error"):
        return "failed", 500
    else:
        return r
# endregion


if __name__ == '__main__':
    app.run(debug=True)
