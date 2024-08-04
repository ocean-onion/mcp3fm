from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required
from app.forms import PluginUploadForm, CustomizationForm, RatingForm

plugins = Blueprint('plugins', __name__)

@plugins.route('/upload', methods=['GET', 'POST'])
@login_required
def upload_plugin():
    form = PluginUploadForm()
    if form.validate_on_submit():
        flash('Plugin uploaded successfully!', 'success')
        return redirect(url_for('main.home'))
    return render_template('upload.html', form=form)

@plugins.route('/customize', methods=['GET', 'POST'])
@login_required
def customize_plugin():
    form = CustomizationForm()
    if form.validate_on_submit():
        flash('Plugin customized successfully!', 'success')
        return redirect(url_for('main.home'))
    return render_template('customize.html', form=form)

@plugins.route('/rate', methods=['GET', 'POST'])
@login_required
def rate_plugin():
    form = RatingForm()
    if form.validate_on_submit():
        flash('Plugin rated successfully!', 'success')
        return redirect(url_for('main.home'))
    return render_template('rate.html', form=form)
