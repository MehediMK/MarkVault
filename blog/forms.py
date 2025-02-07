from django import forms


class BlogForm(forms.Form):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter blog title'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter your content here'}))
    format_choice = forms.ChoiceField(choices=[('md', 'Markdown'), ('json', 'JSON')], widget=forms.RadioSelect)
