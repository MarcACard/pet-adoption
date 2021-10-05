from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.fields.core import BooleanField
from wtforms.validators import InputRequired, NumberRange, Optional, URL


class PetForm(FlaskForm):
    """View and Edit Pet form"""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = StringField("Species")
    photo_url = StringField("Photo Url", validators=[Optional(), URL()])
    age = IntegerField(
        "Pet Age", validators=[InputRequired(), NumberRange(min=1, max=30)]
    )
    notes = TextAreaField("Additional Notes")
    availability = BooleanField("Available for Adoption", default=True)
