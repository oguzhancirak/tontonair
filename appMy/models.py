from django.db import models


class Airways_depture(models.Model):
    name=models.CharField(("Havayolu adı"), max_length=50)
    city=models.CharField(("Şehir"),max_length=50)
    def __str__(self):
        return self.name

class Airways_arrive(models.Model):
    name=models.CharField(("Havayolu adı"), max_length=50)
    city=models.CharField(("Şehir"),max_length=50)
    def __str__(self):
        return self.name

class Airways_company(models.Model):
    name=models.CharField(("Havayolu şirketi"), max_length=50)
    brand=models.CharField(("Markası"),max_length=50)

    def __str__(self):
        return self.name

class Flight(models.Model):
    title=models.CharField(('Başlık'),max_length=50,null=True)
    model=models.ForeignKey(Airways_company, verbose_name=("uçuş şirketi"), on_delete=models.CASCADE)
    text=models.CharField(('Açıklama'),max_length=50,null=True)
    price=models.FloatField(('Fiyat'),max_length=50,null=True)
    time=models.DateField(("Zaman"), auto_now=False, auto_now_add=False,)
    variş_date=models.DateField(("varış Zamanı"), auto_now=False, auto_now_add=False,null=True,)
    depeture_place=models.ForeignKey(Airways_depture, verbose_name=("Kalkış yeri"), on_delete=models.CASCADE)
    arrive_place=models.ForeignKey(Airways_arrive, verbose_name=("Varış yeri"), on_delete=models.CASCADE)
    adult=models.IntegerField(("Yeşkin sayısı"),null=True,blank=True);
    child=models.IntegerField(("Cocuk sayısı"),null=True,blank=True);
    baggage=models.IntegerField(("Bagaj Ağırlığı"),null=True,blank=True)


    def __str__(self):
        return self.title
