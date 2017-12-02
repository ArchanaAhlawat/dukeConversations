import datetime

from django import forms
from django.contrib.auth.models import User
from .models import Student, Dinner, Professor, Application

class loginForm(forms.Form):
	username = forms.CharField(max_length = 70, widget=forms.TextInput(attrs={'class' : 'form-control'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control'}))

class accountInfo(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(accountInfo, self).__init__(*args, **kwargs)

		#get the choice options from the Student model
		majors = Student._meta.get_field('major').choices
		pronouns = Student._meta.get_field('pronoun').choices
		years = Student._meta.get_field('year').choices

		#assign the choices
		self.fields['major'].choices = majors
		self.fields['pronoun'].choices = pronouns
		self.fields['year'].choices = years

		#give each field the class that engages css
		for field in self.fields:
			self.fields[field].widget.attrs.update({'class' : 'form-control'})

	class Meta:
		model = Student
		#define which fileds
		fields = ('username', 'name', 'unique_id', 'netid', 'phone_number', 'year', 'major', 'pronoun', 'food_restrictions')
		widgets = {
			#give each field class that engages css
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
			'unique_id': forms.TextInput(attrs={'class': 'form-control', 'min_length': 7, 'pattern':'[0-9]+', 'title':'Numbers only, no spaces or dashes.'}),
            'netid': forms.TextInput(attrs={'class': 'form-control'}),
			'phone_number': forms.TextInput(attrs={'class': 'form-control', 'pattern':'^[0-9]+$', 'title':'Numbers only, no spaces or dashes.'}),
            'year': forms.Select(attrs={'class': 'form-control'}),
			'major': forms.Select(attrs={'class': 'form-control'}),
            'pronoun': forms.Select(attrs={'class': 'form-control'}),
			'food_restrictions': forms.TextInput(attrs={'class': 'form-control'})
		}
		labels = {
			#give fields human readable labels
            'netid': 'NetID',
			'unique_id': 'Unique ID',
			'pronoun': 'Preferred pronouns'
        }

class registerDinner(forms.Form):
	def __init__(self,*args,**kwargs):
		self.user = kwargs.pop('user',None)
		super(registerDinner, self).__init__(*args,**kwargs)

		startdate = datetime.date.today()
		enddate = startdate + datetime.timedelta(days=20)

		#selecting all the dinners that are in the future
		future_dins = Dinner.objects.filter(date_time__range=[startdate, enddate]).values()

		#selecting all the applications already submitted by person
		applied = Application.objects.filter(username = self.user.username)
		applied = applied.values_list("dinner_id", flat=True)

		#creating tuples for the options to show, for future dinners, excluding already applied to

		for din in future_dins:
			options = [(x['id'], Professor.objects.get(pk = x['professor_id_id']).name + ", " + x['topic'] + ", " + str(x['date_time'].date())) for x in future_dins if x['id'] not in applied]
			options = sorted(options, key=lambda tup: tup[1].split(",")[2]) #sorting by soonest date

		#defining field types
		self.fields['dinner'].choices = options
		self.fields['dinner'].widget.attrs.update({'class' : 'form-control'})
		self.fields['interest'].widget.attrs.update({'class' : 'form-control'})

	dinner = forms.ChoiceField()
	interest = forms.CharField(widget=forms.Textarea)
