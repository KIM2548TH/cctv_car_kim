from flask import Blueprint, render_template
from flask_login import login_required

module = Blueprint("map", __name__)


@module.route("/map")
@login_required
def map_view():
    """Display the university parking map"""
    return render_template("/map/map.html")
