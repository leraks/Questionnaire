from django import forms
from .models import *
from django.contrib.auth.models import User
from account.models import Profile

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class TestForm(forms.Form):
    question = forms.ChoiceField(widget=forms.RadioSelect, choices=())

    def __init__(self, test, id_user, user_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test = test
        self.id_user = id_user
        self.user_name = user_name
        del self.fields["question"]
        for question in test.question_set.all():
            choices = [(choice.id, choice.text_choice) for choice in question.choice_set.all()]
            self.fields[f"question_{question.id}"] = forms.ChoiceField(widget=forms.RadioSelect, choices=choices)
            self.fields[f"question_{question.id}"].label = question.text_question

    def save(self):
        data = self.cleaned_data
        submission = Submission(test=self.test)
        profile = Profile.objects.get(id=self.id_user)
        submission.save()

        for question in self.test.question_set.all():
            choice = Choice.objects.get(pk=data[f"question_{question.id}"])
            submission.answer.add(choice)

        correct_answer = 0
        for answer in self.test.question_set.all():
            if answer.correct_answer in [z.text_choice for z in submission.answer.all()]:
                correct_answer += 1
        submission.Number_of_correct_answers = correct_answer
        submission.profile_submission = self.user_name

        if correct_answer >= (len(self.test.question_set.all()) // 2):
            submission.status = "Пройден"
        else:
            submission.status = "Провален"

        profile.submission.add(self.test)

        submission.save()
        return submission




