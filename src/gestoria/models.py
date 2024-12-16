from django.db import models

# Create your models here.
class  Consorcio(models.Model):
    domicilio =models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.domicilio
    

class  Liquidaciones(models.Model):
    agregar =models.CharField(Consorcio, on_delete=models.SET_NULL, null=True )
    cerrar =models.CharField(Consorcio, on_delete=models.SET_NULL, null=True )
    abrir =models.CharField(Consorcio)    

class  Unidades(models.Model):
    nombre =models.CharField(Liquidaciones, on_delete=models.SET_NULL, null=True )
    apellido =models.CharField(Liquidaciones, on_delete=models.SET_NULL, null=True )
    piso_depto =models.PositiveIntegerField()


    
