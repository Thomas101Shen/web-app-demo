from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, RadioField, SubmitField
from wtforms.validators import DataRequired

class FieldsRequiredForm(FlaskForm):
  """Require radio fields to have content.
  This works around the bug that WTForms radio fields
  don't honor the `DataRequired` or `InputRequired` validators."""
  class Meta:
    def render_field(self, field, render_kw):
      if field.type == "_Option":
        render_kw.setdefault("required", True)
      return super().render_field(field, render_kw)

categories = [("regrout","Regrout"), ("restoration", "Restoration"), ("repair", "Repair"), ('miscelleneous', 'Miscellaneous')]

class ContactForm(FieldsRequiredForm):
	first_name = StringField('First Name', validators = [DataRequired()])
	last_name = StringField('Last Name', validators = [DataRequired()])
	address = StringField('Email Address', validators = [DataRequired()])
	description = TextAreaField('Describe your situation and what you are looking for')
	category = RadioField('Type of Service', choices = categories)
	submit = SubmitField('Contact Us')