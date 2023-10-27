from django.db.models import *

class Post():
    title = CharField(verbose_name='посты',max_length=256)
    description = CharField(verbose_name='Описание',max_length=256)
    authot = CharField(verbose_name='Автор',max_length=256)
    
    def __str__(self):
        return f'{self.title}'