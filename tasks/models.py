from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True

class Priority(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
         return self.name

class Category(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Task(BaseModel):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    deadline = models.DateTimeField()

    status = models.CharField(max_length = 100, choices = [("Pending", "Pending"), ("In Progress", "In Progress"),("Completed", "Completed")], default = "Pending")

    category = models.ForeignKey(Category, on_delete = models.CASCADE)

    priority = models.ForeignKey(Priority, on_delete = models.CASCADE)

class Note(BaseModel):
     task = models.ForeignKey(Task, on_delete = models.CASCADE)

     content = models.TextField()


class Subtask(BaseModel):
     parent_task = models.ForeignKey(Task, on_delete = models.CASCADE)

     title = models.CharField(max_length = 200)

     status = models.CharField(max_length = 50, choices = [("Pending", "Pending"), ("In Progress", "In Progress"),("Completed", "Completed")], default = "Pending")