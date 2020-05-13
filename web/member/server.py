from flask import current_app

from web.common.utils import results2dict


def query_member(**kwargs):
    sql="select * from member where account=:account"
    with current_app.db as db:
        result_proxy=db.session.execute(sql,kwargs)
        keys=result_proxy.keys()
        result=result_proxy.fetchone()
    return results2dict(keys,result)

def update_member(**kwargs):
    sql="update member set password=:password,email=:email,telephone=:telephone where account=:account"
    with current_app.db as db:
        db.session.execute(sql, kwargs)
    return {"result": True}