from django.db import models

class Medcard(models.Model):
    datetime = models.DateTimeField('Дата и время обращения', auto_now_add=True)
    iin = models.CharField('ИИН', null=True, max_length=12)
    lastname = models.CharField('Фамилия', max_length=20, null=True)
    firstname = models.CharField('Имя', max_length=20, null=True)
    surname = models.CharField('Отчество', max_length=20, default='')
    birthdate = models.DateField('Дата рождения', null=True)
    faculty = models.CharField('Факультет', max_length=30, default='')
    group = models.CharField('Группа', max_length=30, default='')
    status = models.CharField('Должность', max_length=30, default='')
    address = models.CharField('Адрес',max_length=50, default='')
    simptoms = models.TextField('Краткий анамнез', null=True)
    diagnosis = models.ForeignKey('mkb', on_delete=models.PROTECT)
    suggestions = models.TextField('Назаначение', default='')
    perv_povt = models.CharField('Первичный или повторный', max_length=10, default='первичный')
    additions = models.TextField('Примечание', default='')

    def __repr__(self):
        return f'{type(self).__name__}({self.lastname!r}, {self.firstname!r}, {self.surname!r})'
    
    def get_absolute_url(self):
        return f'/students/{self.id}'

    class Meta:
        verbose_name = 'Медицинская карта'
        verbose_name_plural = 'Медицинские карты'

class mkb(models.Model):
    id = models.IntegerField('Номер',null=False, primary_key=True)
    name = models.TextField('Наименование', null=False)
    code = models.CharField('Код', max_length=15, null=False)
    parent_id = models.IntegerField('Номер родителя', null=True)
    parent_code = models.CharField('Код родителя', max_length=15, null=True)
    node_count = models.IntegerField('Количество', default=0)
    additional_info = models.TextField('Дополнительная информация',null=True)

    def __str__(self):
        return  self.name + ' ' + self.code 