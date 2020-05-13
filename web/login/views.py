from flask import Blueprint,session,render_template,url_for,redirect,request
from io import BytesIO
from web.login import service
from web.common.verification_code import generate_img


bp=Blueprint("bp_login",__name__,url_prefix="/tea/login",static_folder="static",template_folder="templates")


@bp.route("/")
def index():
    return render_template("login.html")



@bp.route("/code", methods=["get", "post"])
def code():
    code, img = generate_img()
    # 将验证码字符串储存在session中
    session["code"] = code.lower()
    # 图片以二进制形式写入
    buf = BytesIO()
    img.save(buf, "jpeg")
    # 获取图片内容(bytes类型)
    buf = buf.getvalue()
    return buf


#登录验证
@bp.route("/check", methods=["get", "post"])
def login():
    # 获取session中的验证码
    code = session.get("code")

    # 获取用户表单提交的数据
    user_code = request.values.get("txtCode").lower()
    user_name=request.values.get("name")
    pwd=request.values.get("pwd")
    #在数据库中查找匹配数据
    member= service.qurie_member(account=user_name)
    if member:
        session['account'] = member.get("Account")
        member_pwd=member.get("Password")
        if member_pwd==pwd and user_code == code:
            return redirect(url_for("bp_index.index"))
        else:
            return redirect(url_for("bp_login.index"))