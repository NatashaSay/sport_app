from django.db import models

# Create your models here.

# az postgres up --resource-group lab2 --location westus2 --sku-name B_Gen5_1 --server-name sportserver1
# --database-name sport --admin-user sport_user --admin-password TestLab2 --ssl-enforcement Enabled

# "python": "cnx = psycopg2.connect(database='sport', user='sport_user@sportserver1', host='sportserver1.postgres.database.azure.com', password='TestLab2', port='5432')",


class Athlete(models.Model):
    firstname = models.CharField(max_length=100, blank=False)
    lastname = models.CharField(max_length=100, blank=False)
    country = models.CharField(max_length=100, blank=False)
    age = models.IntegerField(blank=True)
