from django import forms

class BookForm(forms.Form):
    """form validation for editing book name"""
    
    name = forms.CharField(
        min_length=2,
        max_length=255,
        error_messages={
            'required': 'Name is required',
            'min_length': 'Name must be at least 2 characters',
            'max_length': 'Name must not exceed 255 characters',
        }
    )