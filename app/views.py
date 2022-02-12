from flask_appbuilder import ModelView
from flask_appbuilder.fieldwidgets import Select2Widget
from flask_appbuilder.models.sqla.interface import SQLAInterface
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from . import appbuilder, db
from .models import Demo


class DemoView(ModelView):
    datamodel = SQLAInterface(Demo)
    add_columns = ["name","description"]
    edit_columns = ["name","description"]
    show_columns = ["name","description"]
    list_columns = ["name","description"]


db.create_all()

appbuilder.add_view(
    DemoView, "Demo", icon="fa-folder-open-o", category="Demo"
)