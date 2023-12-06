from django.db import models

# Create your models here.

# Categoria 
class Categoria(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self) -> str:
         return self.nome
#Post
class Post(models.Model): 
    titulo = models.CharField(max_length=255)
    corpo = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    modificado_em = models.DateTimeField(auto_now=True)
    categorias = models.ManyToManyField('Categoria', related_name= 'posts')

    def __str__(self) -> str:
         return self.titulo

 #Comentario
class Comentario(models.Model):
        autor = models.CharField(max_length=60)
        corpo= models.TextField()
        criado_em = models.DateTimeField(auto_now_add=True)
        post = models.ForeignKey("Post", on_delete=models.CASCADE)
        
        def __str__(self) -> str: 
             return f'{self.autor} em {self.post}'
