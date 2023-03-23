from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.safestring import mark_safe
from malves import settings


class PublisedManager(models.Manager):
    def get_queryset(self):
        return super(PublisedManager,
                     self).get_queryset()\
                          .filter(status='publicado')


class Postagem(models.Model):
    ESCOLHA_STATUS = (
        ('rascunho', 'Rascunho'),
        ('publicado', 'Publicado'),
    )
    titulo = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publicar')
    autor = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              related_name='blog_posts')
    fonte = models.CharField(max_length=100, null=True, blank=True)
    corpo = models.TextField()
    publicar = models.DateTimeField(default=timezone.now)
    img = models.ImageField(upload_to='blog_img')
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=ESCOLHA_STATUS,
                              default='rascunho')

    objects = models.Manager()
    published = PublisedManager()

    class Meta:
        ordering = ('-publicar',)
        verbose_name = 'postagem'
        verbose_name_plural = 'postagens'

    @mark_safe
    def icone(self):
        return f'<img width="30px" height="30px" src="/media/{self.img}">'

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publicar.year,
                             self.publicar.month,
                             self.publicar.day, self.slug])
