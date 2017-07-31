# -*- coding: utf-8 -*-

from flask_wtf import Form
from wtforms import FileField, SelectField, widgets
from wtforms.validators import DataRequired, ValidationError
from charts_test import db
from .models import Regions, Cities, Values



class RegionFilterForm(Form):
    """Region filter form."""

    region = SelectField("Region", choices=[])




class FileForm(Form):
    """File form."""

    file = FileField("File", validators=[DataRequired()])


