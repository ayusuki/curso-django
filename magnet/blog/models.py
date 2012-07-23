from django.db import models

class Blog(models.Model):
    tipo = models.CharField(max_length=64, null=True)
    nome = models.CharField(max_length=64)
    dt_inicio = models.DateField(auto_now=True)
    dt_delete = models.DateField(null=True, blank=True)
    
    def __unicode__(self):
        return u'%s' % (self.nome)

class Conteudo(models.Model):
    blog = models.ForeignKey(Blog)
    dt = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=256)
    texto = models.TextField(null=True, blank=True)
    
    def __unicode__(self):
        return u'%s' % (self.titulo)
