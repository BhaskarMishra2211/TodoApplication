from django import forms
from .models import Todo,Assign_task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TaskForm(forms.ModelForm):
	class Meta:
		model = Todo
		fields = ("task","completed","created_date","deadline")


class AssignForm(forms.ModelForm):
	class Meta:
		model = Assign_task
		fields = "__all__"

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

'''class AssignTaskForm(forms.Form):
    def __init__(self):              
        self.choice_list = [('test', 'test'),]        
        self.users = User.objects.all()        
        for self.x in self.users:
            self.choice_list.append([self.x.get_username(), self.x.get_username()])        
        self.CHOICES = self.choice_list
        super (AssignTaskForm, self).__init__()
        self.fields['User_choice'].widget = forms.Select(choices=self.CHOICES) 
        
    User_choice = forms.CharField(max_length=100)
    start_date = forms.DateField(widget=forms.SelectDateWidget())
    end_date = forms.DateField(widget=forms.SelectDateWidget())
	Task_Name = forms.CharField(widget=forms.Textarea)'''


class AssignTaskForm(forms.Form):
	def __init__(self):
		self.choice_list = [('test','test'),]
		self.users = User.objects.all()
		for self.x in self.users:
			self.choice_list.append([self.x.get_username(), self.x.get_username()])
		self.CHOICES = self.choice_list 
		super(AssignTaskForm,self).__init__()
		self.fields['SELECT_USER'].widget = forms.Select(choices=self.CHOICES)

	Task_Name = forms.CharField(widget = forms.TextInput)
	SELECT_USER = forms.CharField(max_length = 100)
	start_date = forms.DateField(widget=forms.SelectDateWidget())
	end_date = forms.DateField(widget=forms.SelectDateWidget())