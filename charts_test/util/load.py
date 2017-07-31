# -*- coding: utf-8 -*-

import re
import os
import csv
from charts_test import db
from charts_test import models


def load_data(file_name):
    """
    Load data from file to db.

    Parse file with data and import
    information to db.
    """
    region_list = []

    with open("uploads/" + file_name, encoding="utf-8") as csvfile:
        read_CSV = csv.reader(csvfile, delimiter=",")
        for row in read_CSV:
            region_list.append([row[0], row[1], row[2]])
    return region_list



def import_data(region_list):
    """
    Import data from list to db.
    """
    
    del region_list[0]

    for item in region_list:
        region = models.Regions.query.filter_by(name=item[0]).first()
        if region:
            pass
        else:
            new_region = models.Regions(name=item[0])
            db.session.add(new_region)
            db.session.commit()
        city = models.Cities.query.filter_by(name=item[1]).first()
        if city:
            pass
        else:
            region = models.Regions.query.filter_by(name=item[0]).first()
            new_city = models.Cities(name=item[1], region=region.id)
            db.session.add(new_city)
            db.session.commit()
        city = models.Cities.query.filter_by(name=item[1]).first()
        new_value = models.Values(city=city.id, value=item[2])
        db.session.add(new_value)
        db.session.commit()
