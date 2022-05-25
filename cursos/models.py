from django.db import models

class Base(models.Model): 
    create = models.DateTimeField(auto_now_add=True)
    atualization = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Course(Base):
    title = models.CharField(max_length=255)
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural: 'course'
        ordering = ['id']
    
    def __Str__(self):
        return self.title


class Avaliation(Base):
    cource = models.ForeignKey(Course, related_name='avaliations', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    comment = models.TextField(blank=True, default='')
    avaliation = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        verbose_name = 'avaliation'
        verbose_name_plural: 'avaliation'
        unique_together = ['email', 'cource'] ## name and email unique person.
        ordering = ['id']

    def __str__(self):
        return f'{self.name} tared the course {self.cource} out of {self.avaliation}'
    
