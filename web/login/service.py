from flask import current_app

from web.common.utils import results2dict

def qurie_member(**kwargs):
    sql = "select * from member where account=:account"
    with current_app.db as db:
        result_proxy=db.session.execute(sql,kwargs)
        keys=result_proxy.keys()
        result=result_proxy.fetchone()

    return results2dict(keys,result)