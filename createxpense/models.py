from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TransactionTypes(models.Model):
	name = models.CharField(max_length=100,primary_key=True)
	
	def __str__(self):
		return self.name

class TransactItems(models.Model):
	trans_id = models.BigAutoField(primary_key=True)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)
	user_name = models.ForeignKey(User)
	amount = models.IntegerField()
	type_of_transaction =  models.ForeignKey(TransactionTypes)

	def __str__(self):
		return str(self.user_name) + ' - ' + str(self.amount) + ' Rs @ '+ str(self.created_at) + ' for ' + str(self.type_of_transaction)
		
