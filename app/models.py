from django.db import models

# Create your models here.
class Departments(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название отдела")

    class Meta:
        verbose_name = "Отдел"
        verbose_name_plural = "Отдел"

    def __str__(self) -> str:
        return self.name 

class Employee(models.Model):
    firstName = models.CharField(max_length=255, verbose_name="Имя")
    lastName = models.CharField(max_length=255, verbose_name="Фамилия")
    middleName = models.CharField(max_length=255, verbose_name="Отчество", blank=True)
    phoneNumber = models.PositiveIntegerField(verbose_name="Номер телефона")
    adress = models.CharField(max_length =255,verbose_name="Адресс")
    department = models.ForeignKey(Departments, on_delete=models.CASCADE,verbose_name="Отдел")
    

    def __str__(self) -> str:
        return self.firstName + " " + self.lastName 

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудник"



class Auto(models.Model):
    user = models.ForeignKey(Employee, verbose_name="Водитель", on_delete=models.SET_NULL, null=True)
    model = models.CharField(max_length=255, verbose_name="Модель")
    avto_nomer = models.CharField(max_length =255, unique=True,verbose_name="Номер автомобиля")
    vin = models.CharField(max_length=255, unique=True,verbose_name="VIN код автомобиля")
    year_manufacture = models.DateField(verbose_name="Год изготовления")
    chassis = models.CharField(max_length=255, blank=True, verbose_name="Шасси")
    engine_power = models.PositiveIntegerField(verbose_name="Мощность двигателя")
    tech_inspection = models.DateField(verbose_name="Техосмотр")
    mileage = models.PositiveIntegerField(verbose_name="Пробег")

    average_fuel_use = models.PositiveSmallIntegerField(verbose_name="Среднее кол-во топлива на 100 км.")

    TYPE_CHOICES =(
        ("Грузовой","Грузовой"),
        ("Пассажирский","Пассажирский"),
    )
    type = models.CharField(max_length=20,
                  choices=TYPE_CHOICES,
                  default="PASSENGER")

    def __str__(self) -> str:
        return self.model + " " + self.avto_nomer + " " + self.user.firstName

    class Meta:
        verbose_name = "Транспорт"
        verbose_name_plural = "Транспорт"

    


    
