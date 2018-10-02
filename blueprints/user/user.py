from flask import Blueprint,request,jsonify,current_app
from blueprints.user.inputes import RegisterInput,LoginInput
from blueprints.user.models import User
from random import randint
import jwt
import datetime
from login_required import login_required
import json
user_blueprint=Blueprint('user',__name__)
@user_blueprint.route('/')
def hello():
    return "Hello, its davids code"

@user_blueprint.route('/signup',methods=('GET','POST'))
def signup():
    if request.method=="POST":
        inputes=RegisterInput(request)
        if inputes.validate():
            data=request.json
            user=User()
            user.email=data['email']
            user.name=data['name']
            user.phone=data['phone']
            user.encrypt_password(data['password'])
            user.code = randint(0, 90000)
            user.save()
            return jsonify(code=1,message="You have successfully created an account")
        else:
            return jsonify(code=0,message="An error occured", errors=inputes.errors)
    else:
        return jsonify(code=0,message="An error occured")


@user_blueprint.route('/signin',methods=('GET','POST'))
def signin():
    if request.method=="POST":
        inputes=LoginInput(request)
        if inputes.validate():
            data=request.json
            email=data['email']
            user = User.query.filter_by(email=email).first()
            if user:
                # if user.confirmed == 0:
                #     return jsonify(code=0, message="You need to confirm your account. Please check your mail")
                if user.authenticate(user.password, data['password']):

                    token=jwt.encode({'user_id':user.id,'exp':datetime.datetime.utcnow()+datetime.timedelta(hours=24)},
                                     current_app.config['SECRET_KEY'],algorithm="HS256")
                    return jsonify(code=1,token=token.decode('UTF-8'),message="Login Successful")
                else:
                    return jsonify(code=0, message="Password or email is wrong")

@user_blueprint.route('/user',methods=('GET','POST'))
@login_required
def user():
    user_id=request.user_id
    user = User.query.filter_by(id=user_id).first()
    if user:
        user_schema = UserSchema()
        output = user_schema.dump(user).data
        return jsonify(code=1, data=output)
    return jsonify(code=0, message="This user does not exist")
    return "user"