from django.db import models


class Test(models.Model):
    title = models.CharField(max_length=99, unique=True)
    description_mini = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.PROTECT)
    text_question = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255)

    def __str__(self):
        return self.text_question


class Choice(models.Model):
    question = models.ForeignKey(Question, null=True, on_delete=models.CASCADE)
    text_choice = models.CharField(max_length=255)

    def __str__(self):
        return f"Вопрос {self.question.text_question} - {self.text_choice}"


class Submission(models.Model):
    test = models.ForeignKey(Test, on_delete=models.PROTECT)
    profile_submission = models.CharField(max_length=255)
    Number_of_correct_answers = models.IntegerField(default=0, blank=True)
    answer = models.ManyToManyField(Choice)
    status = models.CharField(max_length=255)

    def __str__(self):
        return f"Пользователь: Name. {self.test.title}.  Статус теста - {self.status}"