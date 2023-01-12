from django.db import models

# Create your models here.
class ProjectInfo(models.Model):
    github_url = models.URLField()
    live_url = models.URLField()
    project_name = models.CharField(max_length=200)
    project_description = models.CharField(max_length=600)
    project_image = models.FileField(upload_to="photo")
    project_id = models.URLField()
    project_id = models.URLField()
    show = models.BooleanField(default=False)

    def __str__(self):
        return self.project_name
