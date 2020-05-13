from json import dumps

from flask import Blueprint, session, jsonify, request,render_template
from web.member.server import *

bp=Blueprint('bp_member',__name__,url_prefix="/tea/member",static_folder='static',template_folder='templates')

@bp.route("/")
def show_member():
    account=session['account']
    result=query_member(account=account)
    return render_template("member.html",ID=result.get("ID"),account=result.get("Account"),password=result.get("Password"),email=result.get("Email"),grade=result.get("Grade"),telephone=result.get("Telephone"))

@bp.route("/update_member",methods=["post"])
def update_member():
    password = request.values.get("password")
    email = request.values.get("email")
    telephone = request.values.get("telephone")
    result=update_member(password=password,email=email,telephone=telephone)
    return dumps(result)