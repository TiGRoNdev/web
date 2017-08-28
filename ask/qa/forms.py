from django import forms
from qa.models import Question, Answer


class AskForm(forms.Form):
	title = forms.CharField(max_length=100)
	text = forms.CharField(widget=forms.Textarea)

	def clean(self):
		text = self.cleaned_data['text']
		if len(text) > 1000:
			raise forms.ValidationError('Symbols in text > 1000')
		return "Successfully completed"
	
	def save(self):
		question = Question(**self.cleaned_data)
		question.save()
		return question


class AnswerForm(forms.Form):
	question = forms.CharField(max_length=100)
	text = forms.CharField(max_length=600, widget=forms.Textarea)
	
	def clean_question(self):
		question = self.cleaned_data['question']
		try:
			test_question = Question.objects.get(title=str(question))
		except Question.DoesNotExist:
			raise forms.ValidationError('Question with this title does not exist')
		return "Successfully completed"