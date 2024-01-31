from datetime import date
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def calculate_age(self):
        if self.birth_date:
            today = date.today()
            age = today.year - self.birth_date.year - (
                        (today.month, today.day) < (self.birth_date.month, self.birth_date.day))
            return age
        return None

class DishesCategory(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(null=True, upload_to="dishes_category", blank=True)

    def __str__(self):
        return self.name

class Store(models.Model):
    name = models.CharField(max_length=10)
    address = models.CharField(max_length=30)
    comment = models.CharField(max_length=30)
    store_phone_number = models.CharField(max_length=15)
    min_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    delivery_fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    img = models.ImageField(null=True, upload_to="store", blank=True)
    dishes_categories = models.ManyToManyField(DishesCategory)

    def __str__(self):
        return self.name

#가게 메뉴
class StoreMenu(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    menu_name = models.CharField(max_length=255)
    menu_comment =models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    img = models.ImageField(null=True, upload_to="store_menus", blank=True)

    def __str__(self):
        return f"{self.store.name} - {self.menu_name}"

#장바구니
class CartItem(models.Model):
    user = models.ForeignKey('main.CustomUser', on_delete=models.CASCADE)
    menu = models.ForeignKey(StoreMenu, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1) #수량

    def __str__(self):
        return f"{self.user.username} - {self.menu.menu_name} - {self.quantity}개"

#리뷰
class Review(models.Model):
    user = models.ForeignKey('main.CustomUser', on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)  # Store 모델을 참조
    menu = models.ForeignKey(StoreMenu, on_delete=models.CASCADE)
    review_text = models.TextField()
    img = models.ImageField(null=True, upload_to='review', blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return f"{self.user.username} - {self.store.name} - {self.menu.menu_name} - {self.rating}"

#홈배너
class HomeBannerImg(models.Model):
    name = models.CharField(max_length=20)
    content = models.CharField(max_length=30, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="banner")

    def __str__(self):
        return self.name



#게시글(Post) = 제목(postname), 내용(contents)
class Post(models.Model):
    postname = models.CharField(max_length=50)
    contents = models.TextField()

    def __str__(self):
        return self.postname