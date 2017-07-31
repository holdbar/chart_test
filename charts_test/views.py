# -*- coding: utf-8 -*-

import re
import os

from flask import render_template, flash, request, redirect, jsonify
from charts_test import app, db
from .forms import RegionFilterForm, FileForm
from .models import Regions, Cities, Values
from werkzeug import secure_filename
from charts_test.util.load import load_data, import_data


@app.route("/")
@app.route("/index", methods=["GET", "POST"])
def index():
    """Upload view."""

    form = FileForm()
    if request.method == "POST" and form.file.data:
            filename = secure_filename(form.file.data.filename)
            form.file.data.save("uploads/" + filename)
            import_data(load_data(filename))
            return redirect("/charts")
    return render_template("index.html",
                            titleh="Upload data",
                            form=form)



@app.route("/charts", methods=["GET", "POST"])
def charts():
    """Charts view."""

    form = RegionFilterForm()
    regions = [(r.id, r.name) for r in Regions.query.all()]
    form.region.choices = regions
    return render_template("charts.html",
                            title="Charts",
                            form=form)



@app.route("/get_chart_data", methods=["POST"])
def get_chart_data():
    """Util view for AJAX load data from db."""

    region_id = request.form["region"]
    region = Regions.query.get(region_id)
    cities = Cities.query.filter_by(region=region_id).all()
    results_dict = {}
    for city in cities:
        value = Values.query.filter_by(city=city.id).first()
        results_dict[city.name] = value.value
    return jsonify(results_dict)

