from django.db import models
class CheckedTitlesManager(models.Manager):
    def create_row(self, title, prediction, score):
        row = self.model(
            title = title,
            prediction= prediction,
            score = score
        )
        row.save(using=self.db)
        return row

    def get_existing_item(self, title):
        return   CheckedTitles.objects.get(title)
class CheckedTitles(models.Model):
    title = models.CharField(max_length=1024, unique=True)
    prediction = models.CharField(max_length=8)
    score = models.FloatField()
    def __str__(self):
        return self.title

    objects = CheckedTitlesManager()