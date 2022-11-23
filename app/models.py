from django.db import models

# Create your models here.
class Employee(models.Model):
    FIO = models.CharField(max_length=255, verbose_name="ФИО")
    phoneNumber = models.PositiveIntegerField(verbose_name="Номер телефона")
    adress = models.CharField(max_length =255,verbose_name="Адресс")
    

    def __str__(self) -> str:
        return self.FIO 

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудник"


class Avto(models.Model):
    user = models.OneToOneField(Employee, verbose_name="Водитель", on_delete=models.SET_NULL, null=True)
    model = models.CharField(max_length=255, verbose_name="Модель")
    avto_nomer = models.CharField(max_length =255,verbose_name="Номер автомобиля")
    vin = models.CharField(max_length=255,verbose_name="VIN код автомобиля")
    manufacturer = models.CharField(max_length=255, verbose_name="Изготовитель")
    date_purchase = models.DateField(verbose_name="Дата покупки")
    year_manufacture = models.DateField(verbose_name="Год изготовления")
    chassis = models.CharField(max_length=255, verbose_name="Шасси")
    engine_power = models.PositiveIntegerField(verbose_name="Мощность двигателя")
    tech_inspection = models.DateField(verbose_name="Техосмотр")
    mileage = models.PositiveIntegerField(verbose_name="Пробег")

    TYPE_CHOICES =(
        ("FREIGHT","Грузовой"),
        ("PASSENGER","Пассажирский"),
    )
    type = models.CharField(max_length=20,
                  choices=TYPE_CHOICES,
                  default="PASSENGER")
    load = models.PositiveIntegerField(verbose_name="Макс. Загрузка пассажиров/груза")

    def __str__(self) -> str:
        return self.model + " " + self.avto_nomer

    class Meta:
        verbose_name = "Транспорт"
        verbose_name_plural = "Транспорт"

    


    
