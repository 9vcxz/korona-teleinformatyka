from flask import Blueprint, render_template, request
from app.models import Peak
from datetime import datetime
from colorama import Fore
from app.forms.forms import SelectPeaksForm

home_bp = Blueprint('home', __name__)

# @home_bp.route('/')
# def homepage():
#     peaks = Peak.query.all()
#     # mountain_ranges = Peak.query.order_by(Peak.pasmo)
#     mountain_ranges = Peak.query.with_entities(Peak.pasmo).distinct().order_by(Peak.pasmo).all()
#     return render_template('home.html', peaks=peaks, year=datetime.now().year, mountain_ranges=mountain_ranges)


# wersja bez wtforms
# @home_bp.route('/')
# def homepage():
#     try:
#         # pobranie wybranego pasma z query stringa
#         selected_range = request.args.to_dict()['mountain-ranges']
#     except KeyError:
#         selected_range = None

#     # lista z wybranymi (lub wszystkimi) rekordami
#     if selected_range == 'all-ranges' or selected_range == None:
#         peaks = Peak.query.all()
#     else:
#         peaks = Peak.query.filter_by(pasmo=selected_range)

#     # posortowana alfabetycznie lista z odrębnymi nazwami pasm
#     mountain_ranges = Peak.query.with_entities(Peak.pasmo).distinct() \
#                             .order_by(Peak.pasmo).all()
    
#     return render_template(
#         'home.html',
#         peaks=peaks,
#         # year=datetime.now().year,
#         mountain_ranges=mountain_ranges,
#         selected_range=selected_range
#     )

# z użyciem wtforms
@home_bp.route('/', methods=["GET", "POST"])
def homepage():
    # lista z posortowanymi alfabetycznie odrębnymi nazwami pasm
    mountain_ranges = Peak.query.with_entities(Peak.pasmo).distinct() \
                        .order_by(Peak.pasmo).all()
    for count, range in enumerate(mountain_ranges):
        mountain_ranges[count] = range._asdict()['pasmo']
    mountain_ranges.insert(0, 'Pokaż wszystkie')

    peaks_form = SelectPeaksForm()
    # wypełenienie możliwości wyboru nazwami pasm
    peaks_form.mountain_peaks_select.choices = mountain_ranges

    peaks = Peak.query.all()

    
    if peaks_form.is_submitted():
        selected_range = peaks_form.data['mountain_peaks_select']
        if selected_range == 'Pokaż wszystkie':
            return render_template('home.html', peaks_form=peaks_form, peaks=peaks)
        
        peaks = Peak.query.filter_by(pasmo=selected_range)
        return render_template('home.html', peaks_form=peaks_form, peaks=peaks)

    return render_template('home.html', peaks_form = peaks_form, peaks=peaks)