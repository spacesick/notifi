from django import forms

from .models import Listing

from .period import Period


class ListingForm(forms.ModelForm):
    
    class Meta:
        text_input_style = 'focus:ring-indigo-500 focus:border-indigo-500 flex-1 block rounded-md w-full border-gray-300'
        model = Listing
        fields = [
            # 'url',
            'name',
            'crawl_url',
            'selector',
            'period',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': text_input_style, 'placeholder': 'Example Obsrvr'}),
            'crawl_url': forms.TextInput(attrs={'class': text_input_style, 'placeholder': 'https://example.com'}),
            'selector': forms.TextInput(attrs={'class': text_input_style, 'placeholder': '#site-forum-news'}),
            'period': forms.Select(choices=Period.choices, attrs={'class': 'shadow-sm focus:ring-indigo-500 focus:border-indigo-500 mt-1 block w-full border border-gray-300 rounded-md'})
        }

