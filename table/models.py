# from django.db import models

# Create your models here.
from django.db import models

class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('Available', 'Available'),
            ('Occupied', 'Occupied'),
            ('Reserved', 'Reserved')
        ],
        default='Available'
    )

    def __str__(self):
        return f"Table {self.table_number}"

class Order(models.Model):
    table = models.ForeignKey(
        Table,
        on_delete=models.CASCADE,
        related_name='orders'
    )
    item = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order for Table {self.table.table_number} - {self.item} x {self.quantity}"
