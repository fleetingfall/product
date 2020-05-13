from flask import Blueprint,session,render_template,url_for,redirect



bp=Blueprint("bp_index",__name__,url_prefix="/tea",static_folder="static",template_folder="templates")


@bp.route("/")
def index():
    account = session.get("account")
    if account:
        return render_template("index.html",account=account)
    else:
        return redirect(url_for("bp_login.index"))



@bp.route("/delete")
def delete():
    session.clear()
    return redirect(url_for("bp_login.index"))

