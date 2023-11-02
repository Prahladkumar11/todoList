from django.db import models

class Todolist(models.Model):
    list_title = models.CharField(max_length=100)
    def __str__(self):
        return self.list_title

class ToDoItem(models.Model):
    list = models.ForeignKey(Todolist, on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=100)
    due_date=models.DateField(null=True)


    def __str__(self):
        return self.title