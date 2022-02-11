from django import forms
from figures.models import Circle

class FigureRequestForm(forms.Form):
	amount = forms.IntegerField(
		min_value=1, 
		max_value=min(len(Circle.get_free_figures()), 100), 
		widget=forms.NumberInput(attrs={'placeholder': 'сколько?', 'class': 'input-num'}), 
		label=''
	)

	name = forms.CharField(
		max_length=30, 
		widget=forms.TextInput(attrs={'placeholder': 'имя или псевдоним', 'class': 'input-name'}), 
		label=''
	)
