from django.db import models


class Width(models.Model):
    widht = models.CharField(name='Ширина', max_length=10)

    class Meta:
        verbose_name = 'Щирина'
        verbose_name_plural = 'Ширина'


class Profile(models.Model):
    profile = models.CharField(name='Профиль', max_length=10)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профиль'


class Diameter(models.Model):
    diameter = models.CharField(name='Диаметр', max_length=10)

    class Meta:
        verbose_name = 'Диаметр'
        verbose_name_plural = 'Диаметр'


class LoadRating(models.Model):
    load_rating = models.CharField(name='Индекс нагрузки', max_length=10)

    class Meta:
        verbose_name = 'Индекс нагрузки'
        verbose_name_plural = 'Индекс нагрузки'


class SpeedRating(models.Model):
    speed_rating = models.CharField(name='Индекс скорости', max_length=10)

    class Meta:
        verbose_name = 'Индекс скорости'
        verbose_name_plural = 'Индекс скорости'


class Manufacturer(models.Model):
    name = models.CharField(name='Производитель', max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Производитель'


class Tyre(models.Model):
    name = models.CharField(name='Шина', max_length=150)
    description = models.TextField(name='Описание')
    width = models.ForeignKey(Width, verbose_name='Ширина', on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, verbose_name='Профиль', on_delete=models.CASCADE)
    diameter = models.ForeignKey(Diameter, verbose_name='Диаметр', on_delete=models.CASCADE)
    load_rating = models.ForeignKey(
        LoadRating, verbose_name='Индекс нагрузки', on_delete=models.CASCADE
    )
    speed_rating = models.ForeignKey(
        SpeedRating, verbose_name='Индекс скорости', on_delete=models.CASCADE
    )
    run_flat = models.BooleanField(name='Ранфлет', default=False)
    manufacturer = models.ForeignKey(
        Manufacturer, verbose_name='Производитель', on_delete=models.CASCADE
    )
    images = models.ImageField(name='Изображения', upload_to='images/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Щина'
        verbose_name_plural = 'Шины'





