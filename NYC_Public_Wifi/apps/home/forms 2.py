
from django import forms
from .models import Review
from django.forms.widgets import Textarea, SelectDateWidget, DateTimeInput, DateInput


from django import forms
from django.forms import ModelForm
from .models import Hotspot_Location, Neighborhood, Provider


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rate', 'review']
        widgets = {
            'review': Textarea(attrs={'cols': 45, 'rows': 7})
        }


class BoroughForm(ModelForm):
    class Meta:
        model = Hotspot_Location
        fields = '__all__'
        label = {
            'Obj_id' : '',
            'Loc_name' : '',
            'Location' : '',
            'Latitude' : '',
            'Longitude' : '',
            'X_coordinate' : '',
            'Y_coordinate' : '',
            'Activated' : 'MM/DD/YY',
            'BIN' : '',
            'BBL' : '',
            
        }
        
        widgets = {
            'Obj_id' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'obj_id'}),
            'Loc_name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':''}),
            'Location' : forms.TextInput(attrs={'class':'form-control', 'placeholder':''}),
            'Latitude' : forms.TextInput(attrs={'class':'form-control', 'placeholder':''}),
            'Longitude' : forms.TextInput(attrs={'class':'form-control', 'placeholder':''}),
            'X_coordinate' : forms.TextInput(attrs={'class':'form-control', 'placeholder':''}),
            'Y_coordinate' : forms.TextInput(attrs={'class':'form-control', 'placeholder':''}),
            'Activated' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Activated Date'}),
            'BIN' : forms.TextInput(attrs={'class':'form-control', 'placeholder':''}),
            'BBL:' : forms.TextInput(attrs={'class':'form-control', 'placeholder':''}),
        }
        

class NeighborhoodForm(ModelForm):
    class Meta:
        model = Neighborhood
        fields = '__all__'
        label = {
            'Ntacode' : '',
            'Postcode' : '',
            'Nta' : '',
            
        }
        
        widgets = {
            'Ntacode' : forms.TextInput(attrs={'class':'form-control', 'placeholder':''}),
            'Postcode' : forms.TextInput(attrs={'class':'form-control', 'placeholder':''}),
            'Nta' : forms.TextInput(attrs={'class':'form-control', 'placeholder':''})
            }
        
        
class ProviderForm(ModelForm):
    class Meta:
        model = Provider
        fields = '__all__'
        label = {
            'Prov_id' : '',
            'Name' : '',
            'SSID' : '',
            'Source_id' : '',
            'Type' : '',
            'Loc_type' : '',
            'Remarks' : '',
            
        }
        
        widgets = {
            'Prov_id' : forms.TextInput(attrs={'class':'form-control', 'placeholder':''}),
            'Name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':''}),
            'SSID' : forms.TextInput(attrs={'class':'form-control', 'placeholder':''}),
            'Source_id' : forms.TextInput(attrs={'class':'form-control', 'placeholder':''}),
            'Loc_type' : forms.TextInput(attrs={'class':'form-control', 'placeholder':''}),
            'Remarks' : forms.TextInput(attrs={'class':'form-control', 'placeholder':''}),
            }
        
