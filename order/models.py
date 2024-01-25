from django.db import models


class OrderType(models.Model):
    type = models.CharField(verbose_name="Тип сделки", max_length=255)

    class Meta:
        verbose_name = "Тип сделки"
        verbose_name_plural = "Типы сделок"

    def __str__(self):
        return self.type


class OrderVariety(models.Model):
    variety = models.CharField(verbose_name="Вид сделки", max_length=255)

    class Meta:
        verbose_name = "Вид сделки"
        verbose_name_plural = "Виды сделок"

    def __str__(self):
        return self.variety


class Currency(models.Model):
    full_name = models.CharField(verbose_name="Полное наименование", max_length=255)
    short_name = models.CharField(verbose_name="Короткое наименование", max_length=255)

    class Meta:
        verbose_name = "Валюта"
        verbose_name_plural = "Валюты"

    def __str__(self):
        return self.full_name


class Order(models.Model):
    order_type = models.ForeignKey(
        OrderType, verbose_name=("Тип сделки"), on_delete=models.CASCADE
    )
    order_variety = models.ForeignKey(
        OrderVariety, verbose_name=("Вид сделки"), on_delete=models.CASCADE
    )
    currency = models.ForeignKey(
        Currency, verbose_name=("Валюта"), on_delete=models.CASCADE
    )
    tiker = models.CharField(verbose_name="Тикер ценной бумаги", max_length=255)
    count = models.IntegerField(verbose_name="Количество")
    type = models.CharField(verbose_name="Тип поручения", max_length=255)
    number = models.CharField(verbose_name="Номер", max_length=255)
    date = models.DateField(verbose_name="Дата")
    duration = models.CharField(verbose_name="Продолжительность", max_length=255)

    class Meta:
        verbose_name = "Поручение"
        verbose_name_plural = "Поручения"

    def __str__(self):
        return self.tiker
