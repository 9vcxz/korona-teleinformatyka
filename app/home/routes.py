from flask import Blueprint, render_template, request
from app.models import Peak
from datetime import datetime
from app.forms.forms import SelectRangeForm
from colorama import Fore

home_bp = Blueprint('home', __name__)

# @home_bp.route('/')
# def homepage():
#     peaks = Peak.query.all()
#     # mountain_ranges = Peak.query.order_by(Peak.pasmo)
#     mountain_ranges = Peak.query.with_entities(Peak.pasmo).distinct().order_by(Peak.pasmo).all()
#     return render_template('home.html', peaks=peaks, year=datetime.now().year, mountain_ranges=mountain_ranges)

@home_bp.route('/', methods=['GET'])
def homepage():

    form = SelectRangeForm()

    try:
        selected_range = request.args.to_dict()['mountain-ranges']
    except KeyError:
        selected_range = None

    if selected_range == 'all-ranges' or selected_range == None:
        peaks = Peak.query.all()
    else:
        peaks = Peak.query.filter_by(pasmo=selected_range)
    
    # pasma do selecta
    mountain_ranges = Peak.query.with_entities(Peak.pasmo).distinct().order_by(Peak.pasmo).all()

    return render_template(
        'home.html',
        peaks=peaks,
        year=datetime.now().year,
        mountain_ranges=mountain_ranges,
        form=form,
        selected_range=selected_range
    )

