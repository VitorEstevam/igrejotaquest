from flask import Flask, Blueprint, request
from connections.designerDAO import DesignerDAO

designer_routes = Blueprint('designer_routes', __name__)


@designer_routes.route('/designer', methods=['PUT'])
def updateDesigner():
    id = request.args.get('id')
    name = request.args.get('name')
    d = DesignerDAO()
    r = d.update_on_db(id, name)
    return r


@designer_routes.route('/designer', methods=['POST'])
def insertDesigner():
    d = DesignerDAO()
    name = request.args.get('name')
    r = d.insert_on_db(name)
    return r


@designer_routes.route('/designer', methods=['GET'])
def getDesigner():
    id = request.args.get('id')
    d = DesignerDAO()
    r = d.select_from_db(id)
    return r


@designer_routes.route('/designer', methods=['DELETE'])
def deleteDesigner():
    id = request.args.get('id')
    d = DesignerDAO()
    r = d.remove_from_db(id)
    return r


@designer_routes.route('/designers', methods=['GET'])
def getAllDesigners():
    d = DesignerDAO()
    r = d.select_all_from_db()
    return r
