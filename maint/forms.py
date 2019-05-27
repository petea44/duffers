from django import forms

from duffers.models import Score
import datetime
class ScoreForm(forms.ModelForm):
    
    class Meta:
        model = Score
        fields = ('golfer', 'course','hcap','play_date')
    now = datetime.datetime.now().strftime('%Y-%m-%d')    
    YorN = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    hcap = forms.ChoiceField([('Y','Yes'),('N','No')])
    play_date=forms.DateField(input_formats=['%Y%m%d'],initial=datetime.datetime.today().strftime('%Y-%m-%d') )
class HolesForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ()
    stroke = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
    )    
    par1 = forms.ChoiceField(choices=stroke,required=True)
#     par1 = forms.ChoiceField(choices=stroke,required=True)
    par2 = forms.ChoiceField(choices=stroke,required=True)
    par3 = forms.ChoiceField(choices=stroke,required=True)
    par4 = forms.ChoiceField(choices=stroke,required=True)
    par5 = forms.ChoiceField(choices=stroke,required=True)
    par6 = forms.ChoiceField(choices=stroke,required=True)
    par7 = forms.ChoiceField(choices=stroke,required=True)
    par8 = forms.ChoiceField(choices=stroke,required=True)
    par9 = forms.ChoiceField(choices=stroke,required=True)
   
    par10 = forms.ChoiceField(choices=stroke,required=True)
    par11 = forms.ChoiceField(choices=stroke,required=True)
    par12 = forms.ChoiceField(choices=stroke,required=True)
    par13 = forms.ChoiceField(choices=stroke,required=True)
    par14 = forms.ChoiceField(choices=stroke,required=True)
    par15 = forms.ChoiceField(choices=stroke,required=True)
    par16 = forms.ChoiceField(choices=stroke,required=True)
    par17 = forms.ChoiceField(choices=stroke,required=True)
    par18 = forms.ChoiceField(choices=stroke,required=True)
