from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=255, verbose_name = 'Titulo')
    description = models.TextField(blank=True, null=True, verbose_name = 'Descripción')
    image = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name = 'Imagen')
    link =  models.URLField(max_length=255, blank=True, null=True, verbose_name = 'Enlace')
    created = models.DateTimeField(auto_now_add= True, verbose_name = 'Fecha Creación')
    updated = models.DateTimeField(auto_now= True, verbose_name = 'Fecha Edición')
    
    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['-created']
        
    def __str__(self):
        return self. title
    
    