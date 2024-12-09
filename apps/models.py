from django.db import models

class About(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField() 
    image = models.ImageField(upload_to='about/', blank=True, null=True)  # Sayt haqida tasvir
    created_at = models.DateTimeField(auto_now_add=True)  # Yaratilgan vaqt

    def __str__(self):
        return self.title


class Service(models.Model):
    name = models.CharField(max_length=200)  # Xizmat nomi
    description = models.TextField()  # Xizmat tavsifi
    image = models.ImageField(upload_to='services/', blank=True, null=True)  # Xizmatga tegishli tasvir (opsional)
    created_at = models.DateTimeField(auto_now_add=True)  # Yaratilgan vaqt
    updated_at = models.DateTimeField(auto_now=True)  # So'nggi yangilanish vaqti

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=200)  # Blog maqolasi sarlavhasi
    content = models.TextField()  # Blog maqolasi matni
    author = models.CharField(max_length=100)  # Maqola muallifi
    image = models.ImageField(upload_to='blog/', blank=True, null=True)  # Blogga tegishli tasvir
    created_at = models.DateTimeField(auto_now_add=True)  # Yaratilgan vaqt

    def __str__(self):
        return self.title
