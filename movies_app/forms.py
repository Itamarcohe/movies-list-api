from django import forms
from django.forms import HiddenInput, ModelForm, DateInput

from .models import *


class MyDateWidget(DateInput):
    input_type = 'date'


class My_Watch_ListForm(ModelForm):
    watched_date = forms.DateField(widget=MyDateWidget())
    user = forms.ModelChoiceField(queryset=User.objects.all(),
                                  widget=HiddenInput(attrs={'class': 'form-control'}))
    movie_id = forms.ModelChoiceField(queryset=Movie.objects.all(),
                                      widget=HiddenInput(attrs={'class': 'form-control'}))

    class Meta:
        model = My_Watch_List
        fields = '__all__'
        exclude = ['is_deleted']


class Recommend_a_movieForm(ModelForm):
    movie = forms.ModelChoiceField(queryset=Movie.objects.all(),
                                   widget=HiddenInput(attrs={'class': 'form-control'}))

    recommender = forms.ModelChoiceField(queryset=User.objects.all(),
                                         widget=HiddenInput(attrs={'class': 'form-control'}))


    # recommend_to = forms.ModelMultipleChoiceField(
    #     queryset=User.objects.filter(user!=self.user)
    # )

    class Meta:
        model = Recommendations
        fields = '__all__'
        exclude = ['is_watched_by_receiver', 'date_watched_by_receiver', 'receiver_rating', 'date_recommended']


class Respond_Recommend(ModelForm):
    # movie = forms.ModelChoiceField(queryset=Movie.objects.all(),
    #                                widget=HiddenInput(attrs={'class': 'form-control'}))
    # recommender = forms.ModelChoiceField(queryset=User.objects.all(),
    #                                      widget=HiddenInput(attrs={'class': 'form-control'}))
    # recommend_to = forms.ModelChoiceField(queryset=User.objects.all(),
    #                                       widget=HiddenInput(attrs={'class': 'form-control'}))
    # message = forms.CharField(widget=HiddenInput(attrs={'class': 'form-control'}))
    # date_recommended = forms.DateField(widget=HiddenInput())
    # is_watched_by_receiver = forms.BooleanField(widget=CheckboxInput())
    date_watched_by_receiver = forms.DateField(widget=MyDateWidget())

    class Meta:
        model = Recommendations
        fields = '__all__'
        exclude = ['recommend_to', 'message', 'recommender']


