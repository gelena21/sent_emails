from django.db import models


class Client(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=255)
    comment = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ['name']


class Mailout(models.Model):
    start_date = models.DateTimeField()
    period = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    message = models.ForeignKey('Message', on_delete=models.CASCADE)
    clients = models.ManyToManyField('Client')

    def __str__(self):
        return f'{self.status} ({self.start_date})'

    class Meta:
        verbose_name = ['-start_date']


class Message(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = ['subject']


class Attempt(models.Model):
    send_date = models.DateTimeField()
    status = models.CharField(max_length=255)
    response = models.TextField()
    mailout = models.ForeignKey('Mailout', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.send_date} - {self.status}'

    class Meta:
        verbose_name = ['-send_date']
