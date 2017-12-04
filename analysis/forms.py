
from django import forms

from .models import QueryDropdown

QUERY_CHOICES = (
	('1','Relative Abundance/Resistance of Plated Samples'),
	('2','Other'),)

class CustomQueryForm(forms.Form):
	query = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'ex: SELECT * FROM AGAR;'}))
# when rendered, form looks like: 
# <label for="your_query">Custom SQL query: </label>
# <input id="your_query" type="text" name="your_query" required />

class QueryDropdownForm(forms.Form):
	query = forms.ChoiceField(label="",choices=QUERY_CHOICES, required=True)

class FillQueryForm(forms.Form):
	select = forms.CharField(label="SELECT:", widget=forms.TextInput(attrs={'placeholder': 'Column name(s). Separate using commas.'}))
	from_field = forms.CharField(label="FROM:", widget=forms.TextInput(attrs={'placeholder': 'Table name(s). If inner join, separate using commas.'}))
	where = forms.CharField(label="WHERE:", widget=forms.TextInput(attrs={'placeholder': 'Conditions on column values, separated by AND. Leave blank if none.'}))
	limit = forms.CharField(label="LIMIT:", widget=forms.TextInput(attrs={'placeholder': 'Numerical value limiting number of rows returned.'}))

class MapForm(forms.Form):
	print("hello")
	# empty form for now, only has submit button 