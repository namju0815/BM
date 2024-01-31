from django.contrib import admin
from django.urls import path
from main.views import home_view, login_view, logout_view, search_view, signup_view, store_list_view, \
    store_posting_view, test, blog, posting, cart_view, cart_add_view, cart_minus_view, cart_delete_view, \
    review_view, check_username
from django.conf.urls.static import static
from django.conf import settings

app_name = 'main'
#2. url 연결 views.index 함수가 호출 시 url연결
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),

    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),
    path('check_username/', check_username, name='check_username'),

    path('search/', search_view, name='search'),
    path('category/<int:category_id>/', store_list_view, name='store_list'),
    path('store/<int:store_id>/', store_posting_view, name='store_posting'),

    path('cart/', cart_view, name='cart'),
    path('cart/add/<int:menu_id>', cart_add_view, name='cart_add'),
    path('cart/minus/<int:menu_id>', cart_minus_view, name='cart_minus'),
    path('cart/delete/<int:menu_id>', cart_delete_view, name='cart_delete'),

    path('review/<int:store_id>', review_view, name='review'),

    path('test/', test, name='test'),
    path('blog/', blog, name='blog'),
    path('blog/<int:pk>', posting, name="posting")
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)