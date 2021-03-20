from flask import Flask, render_template, request
from connections.designerDAO import DesignerDAO

from routes.designer_routes import designer_routes

app = Flask(__name__)

app.register_blueprint(designer_routes)


if __name__ == '__main__':
    app.run(debug=True)
