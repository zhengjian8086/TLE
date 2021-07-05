from django.db import models

class Users(models.Model):
    login = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=32)
    role_id = models.PositiveIntegerField()
    email = models.CharField(max_length=100)
    first = models.CharField(max_length=50)
    last = models.CharField(max_length=50)
    locale = models.CharField(max_length=10)
    default_testproject_id = models.IntegerField(blank=True, null=True)
    active = models.IntegerField()
    script_key = models.CharField(max_length=32, blank=True, null=True)
    cookie_string = models.CharField(unique=True, max_length=64)
    auth_method = models.CharField(max_length=10, blank=True, null=True)
    creation_ts = models.DateTimeField()
    expiration_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'