from django.db import models
from django.utils.text import slugify

class Movie(models.Model):
    """电影数据模型"""
    title = models.CharField(max_length=255, verbose_name="电影标题")
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField(blank=True, verbose_name="电影描述")
    release_year = models.PositiveIntegerField(blank=True, null=True, verbose_name="上映年份")
    genre = models.CharField(max_length=100, blank=True, verbose_name="类型")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "电影"
        verbose_name_plural = "电影"
        ordering = ['-created_at']


class MovieLink(models.Model):
    """电影链接模型"""
    movie = models.ForeignKey(Movie, related_name='links', on_delete=models.CASCADE, verbose_name="电影")
    title = models.CharField(max_length=255, blank=True, verbose_name="链接标题")
    url = models.URLField(verbose_name="链接地址")
    quality = models.CharField(max_length=50, blank=True, verbose_name="画质")  # 例如: 720p, 1080p
    is_working = models.BooleanField(default=True, verbose_name="是否有效")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return f"{self.movie.title} - {self.quality}"

    class Meta:
        verbose_name = "电影链接"
        verbose_name_plural = "电影链接"
