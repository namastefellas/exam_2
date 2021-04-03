from django.db import models

# Create your models here.


class Poll(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    question = models.CharField(null=False, blank=False, max_length=300)

    class Meta:
        db_table = 'polls'
        verbose_name = 'Poll'
        verbose_name_plural = 'Polls'

    def __str__(self):
        return f'{self.question}'


class Choice(models.Model):
    choice_text = models.CharField(null=False, blank=False, max_length=300)
    poll = models.ForeignKey('webapp.Poll', on_delete=models.CASCADE, verbose_name='Poll', related_name='polls', default=1)

    class Meta:
        db_table = 'choices'
        verbose_name = 'Choice'
        verbose_name_plural = 'Choices'

    def __str__(self):
        return f'{self.choice_text}'