from django import forms 

class NumberForm(forms.Form):
    mafia_player = forms.IntegerField(min_value=5,required=True,label="" , 
                                      error_messages={'required' : 'زرنگ بازی در نیار داداش ' , 
                                      'min_value' : 'داداش بالاتر از ۵ باید بزنی' ,
                                      'invalid':'عدد وارد کن قربونت برم'})