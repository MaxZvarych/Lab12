from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from models.Securities import Securities
import json
import copy



with open('secret.json') as f:
    SECRET=json.load(f)

DB_URI= "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}".format(
    user=SECRET["user"],
    password=SECRET["password"],
    host=SECRET["host"],
    port=SECRET["port"],
    db=SECRET["db"]
)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

class SmartSecurities(Securities, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    document_owner=db.Column(db.String(5) , unique=False)
    price= db.Column(db.Integer , unique=False)
    level_of_risk= db.Column(db.String(6), unique=False)
    trend_of_bidding = db.Column(db.String(10), unique=False)
    importance_of_security= db.Column(db.Integer , unique=False)

    def __init__(self,document_owner,price,level_of_risk,trend_of_bidding,importance_of_security):
        super().__init__(document_owner,price,level_of_risk,trend_of_bidding)
        self.importance_of_security=importance_of_security

class SmartSecuritiesSchema(ma.Schema):
    class Meta:
        fields= ('document_owner','price','level_of_risk' , 'trend_of_bidding', 'importance_of_security','id')

smart_security_schema = SmartSecuritiesSchema()
smart_securities_schema = SmartSecuritiesSchema(many=True)

@app.route("/smart_securities", methods=["POST"])
def add_smart_security():
    smart_securities = SmartSecurities(request.json['document_owner'],
                                                 request.json['price'],
                                                 request.json['level_of_risk'],
                                                 request.json['trend_of_bidding'],
                                                 request.json['importance_of_security'])
    db.session.add(smart_securities)
    db.session.commit()
    return smart_security_schema.jsonify(smart_securities)

@app.route("/smart_securities", methods=["GET"])
def get_security():
    all_smart_securities= SmartSecurities.query.all()
    result=smart_securities_schema.dump(all_smart_securities)
    return jsonify({'smart_securities': result})

@app.route("/smart_securities/<id>", methods=["GET"])
def smart_securities_detail(id):
    smart_securities= SmartSecurities.query.get(id)
    if not smart_securities:
        abort(404)
    return smart_security_schema.jsonify(smart_securities)

@app.route("/smart_securities/<id>", methods=["PUT"])
def smart_securities_update(id):
    smart_securities = SmartSecurities.query.get(id)
    if not smart_securities:
        abort(404)
    old_smart_securities = copy.deepcopy(smart_securities)
    smart_securities.document_owner = request.json['document_owner']
    smart_securities.price = request.json['price']
    smart_securities.level_of_risk = request.json['level_of_risk']
    smart_securities.trend_of_bidding = request.json['trend_of_bidding']
    smart_securities.importance_of_security = request.json['importance_of_security']
    db.session.commit()
    return smart_security_schema.jsonify(old_smart_securities)

@app.route("/smart_securities/<id>", methods=["DELETE"])
def smart_securities_delete(id):
    smart_securities=SmartSecurities.query.get(id)
    if not smart_securities:
        abort(404)
    db.session.delete(smart_securities)
    db.session.commit()
    return smart_security_schema.jsonify(smart_securities)

if __name__== '__main__':
    db.create_all()
    app.run(debug=True, host='localhost')