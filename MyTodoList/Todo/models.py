from django.db import models

# Create your models here.
# Configure modelos para "Tarea" con campos para el título, la descripción, la fecha de vencimiento y el estado de finalización
class Todo(models.Model):
    title = models.CharField(max_length=45, verbose_name='titulo')
    description = models.TextField(verbose_name='descripcion')
    create_at = models.DateField(auto_now_add=True, verbose_name='fecha de creacion')
    expire_at = models.DateField(verbose_name='fecha de vencimiento')

    def __str__(self) -> str:
        return (f'{self.title} : {self.description}')
    
    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todo'
        db_table = 'tbl_todo'
        ordering = ['id']