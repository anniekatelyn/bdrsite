
from django import forms

from .models import QueryDropdown

QUERY_CHOICES = (
	('1','Relative Abundance/Resistance of Plated Samples'),
	('2','Other'),)

class QueryForm(forms.Form):
	query = forms.CharField(label="Custom SQL Query:")
# when rendered, form looks like: 
# <label for="your_query">Custom SQL query: </label>
# <input id="your_query" type="text" name="your_query" required />

class QueryDropdownForm(forms.Form):
	query = forms.ChoiceField(choices=QUERY_CHOICES, required=True, label="Preselected Query:")