from django.db import models
from django.utils import timezone


class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField(null=True)
    admin = models.BooleanField(default=0,null=True)
    real_name = models.CharField(max_length=32,null=True)
    sex = models.CharField(max_length=32,null=True)
    phone = models.CharField(max_length=32,null=True)
    email=models.CharField(max_length=32,null=True)


class Device(models.Model):
    name=models.CharField(max_length=32)
    num=models.IntegerField(default=0)
    model_spec = models.CharField(max_length=32,default=None,null=True, blank=True)
    purchase_date = models.DateField(max_length=32,default= None,null=True, blank=True)
    image = models.ImageField(upload_to='photos/',null=True)
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE,null=True)

class Scrap(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    number = models.PositiveIntegerField()
    scrap_date = models.DateTimeField(auto_now_add=True,null=True)

class Borrow(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    number = models.PositiveIntegerField()
    borrow_date = models.DateTimeField(auto_now_add=True,null=True)
    return_date = models.DateTimeField(null=True, blank=True)
    status = models.IntegerField(default=0)
    tmp_device = models.ForeignKey(Device, null=True,on_delete=models.SET_NULL, related_name='tmp_devices')

    def borrow_device(self):
        if self.status==0:  # New borrow instance
            self.device.num -= self.number
            self.status=1
            self.device.save()
            self.tmp_device =Device.objects.create(name=self.device.name, num=self.number,
                          model_spec=self.device.model_spec,purchase_date=self.borrow_date,image=self.device.image,user=self.user)
        self.save()

    def return_device(self):
        if self.status == 1:
            self.return_date = timezone.now()
            self.device.num += self.number
            Device.objects.filter(id=self.tmp_device.id).delete()
            self.tmp_device =None
            self.status=3
            self.device.save()
        self.save()