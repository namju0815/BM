from django.contrib import admin
from .models import Post, Store, StoreMenu, HomeBannerImg, CustomUser, DishesCategory, CartItem, Review

class StoreAdmin(admin.ModelAdmin):
    filter_horizontal = ('dishes_categories',)

#관리자가 게시글에 접근 가능
admin.site.register(Post)
admin.site.register(DishesCategory)
admin.site.register(Store, StoreAdmin)
admin.site.register(StoreMenu)
admin.site.register(HomeBannerImg)
admin.site.register(CustomUser)
admin.site.register(CartItem)
admin.site.register(Review)
