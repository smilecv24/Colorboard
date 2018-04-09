from django import forms


class GameForm(forms.Form):
	players = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of players'}))
	squares = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of Squares on the board'}))
	cards = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of Cards in the deck'}))
	sequence = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sequence of characters on the board'}))
	cardList = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cards in the deck'}))
