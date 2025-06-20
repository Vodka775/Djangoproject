from django.db import models

# Create your models here.
class Question(models.Model):
    
    qno=models.IntegerField(primary_key=True)
    qtext=models.CharField(max_length=100)
    answer=models.CharField(max_length=50)
    op1=models.CharField(max_length=50)
    op2=models.CharField(max_length=50)
    op3=models.CharField(max_length=50)
    op4=models.CharField(max_length=50)
    subject=models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.qno , self.qtext , self.answer,self.op1,self.op2}";
    
    class Meta:
        db_table="question"

class UserData(models.Model):
    username=models.CharField(max_length=20,primary_key=True)
    password=models.CharField(max_length=20)
    mobno=models.IntegerField()

    def __str__(self) :
        return f"username is {self.username} and password is {self.password} and mobno is {self.mobno} "
    
    class Meta:
        db_table="userdata"

from django.db import models

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.FloatField()
    image_url = models.URLField(max_length=500, null=True, blank=True)

    def __str__(self):  
        return f"{self.product_name} | Price: ₹{self.price} | Quantity: {self.quantity}"

    class Meta:
        db_table = "Products"

    










