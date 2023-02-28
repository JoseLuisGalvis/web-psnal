from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=255, verbose_name = 'Titulo')
    degree_title = models.CharField(max_length=255, verbose_name = 'Titulo Obtenido')
    description = models.TextField(blank=True, null=True, verbose_name = 'Descripción')
    created = models.DateTimeField(auto_now_add= True, verbose_name = 'Fecha Creación')
    updated = models.DateTimeField(auto_now= True, verbose_name = 'Fecha Edición')
    
    class Meta:
        verbose_name = 'Formación'
        verbose_name_plural = 'Formaciones'
        ordering = ['-created']
    
    def __self__(self):
        return self.title
    

class Skill(models.Model):
    title = models.CharField(max_length=255, verbose_name = 'Titulo')
    image = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name = 'Imagen')
    created = models.DateTimeField(auto_now_add= True, verbose_name = 'Fecha Creación')
    updated = models.DateTimeField(auto_now= True, verbose_name = 'Fecha Edición')
    
    class Meta:
        verbose_name = 'Conocimiento'
        verbose_name_plural = 'Conocimientos'
        ordering = ['-created']
        
    def __str__(self):
        return self. title
