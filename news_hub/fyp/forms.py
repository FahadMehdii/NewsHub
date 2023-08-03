from django import forms


class NewsForm(forms.Form):
    news_id = forms.IntegerField(widget=forms.HiddenInput)


