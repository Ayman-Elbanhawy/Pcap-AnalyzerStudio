# coding: utf-8
"""
WTForms definitions for upload and filtering widgets.

Copyright (c) Ayman Elbanhawy (Softwaremile.com)
Code updates and documentation improvements for the public
Pcap-AnalyzerStudio repository.
"""

from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms.validators import DataRequired, AnyOf

class Upload(FlaskForm):
    """Minimal upload form used by the capture loader page."""
    pcap = FileField('pcap', validators=[DataRequired()])


class ProtoFilter(FlaskForm):
    """Protocol filter form retained for compatibility with the existing templates."""
    value = FileField('value')
    filter_type = FileField('filter_type', validators=[DataRequired(), AnyOf([u'all', u'proto', u'ipsrc', u'ipdst'])])
