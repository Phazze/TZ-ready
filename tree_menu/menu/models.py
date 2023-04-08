from django.db import models


class MainMenu(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def __str__(self):
        return self.title


class Menu(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    name_slug = models.SlugField(max_length=100, unique=True, blank=True)
    menu = models.ForeignKey(MainMenu, on_delete=models.CASCADE, related_name='level', blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='child', blank=True, null=True)

    def __str__(self):
        return self.name
