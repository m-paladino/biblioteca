from django.db import models
from django.db.models import Avg, Count, F


class PrestamoManager(models.Manager):
    """ managers para el modelo Lector """

    def prestamo_all(self):

        resultado = self.filter.all()

        return resultado
    
    
    def edad_promedio_libro_prestado(self, libro_id):
        return self.filter(
            libro__id=libro_id
        ).aggregate(
            edad_promedio=Avg('lector__edad')
        )
    

    def prestamos_por_libro(self):
        return self.values('libro', 'devuelto').annotate(
            titulo=F('libro__titulo'),
            num_prestamos=Count('libro')
        )
    