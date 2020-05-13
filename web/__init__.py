def create_app():
    from flask import Flask
    app=Flask(__name__)

    from web.common.setting import Config
    app.config.from_object(Config)

    from flask_sqlalchemy import SQLAlchemy
    orm=SQLAlchemy(app)

    from web.common.utils import DBUtil
    db=DBUtil(orm)

    app.db=db

    """
        批量注册蓝图
        find_modules：查找指定包下面的所有模块
        参数说明：
        import_path：包路径
        include_packages：若为True则返回包内的子包，默认False
        recursive：是否递归搜索子包，默认False
    """
    from werkzeug.utils import find_modules, import_string
    for module_name in find_modules("web", recursive=True):
        """
            import_string：动态导入需要的模块或对象
            参数说明：
            import_name：要导入的模块或对象名称
            silent：若为True则忽略导入错误，返回None，默认False
        """
        module = import_string(module_name)
        if hasattr(module, "bp"):
            app.register_blueprint(module.bp)

    return app