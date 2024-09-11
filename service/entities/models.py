from django.db import models

class Service(models.Model):
    name = model.CharField(max_length=50)
    full_price = model.PositiveIntegerField()
    


class Plan(models.Model):
    PLAN_TYPES = (
	("full", "Full"), ("student", "Student"), ("dicount","Discount")
)
    plan_type = model.CharField(choices=PLAN_TYPES, max_length=10)
    discount_percent = model.PositiveIntegerField(default=0,
						  validators=[
						      MaxValueValidator(100)
						  ])



