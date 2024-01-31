from django.contrib.auth import login, logout, authenticate
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET

from main.models import Post, Store, HomeBannerImg, DishesCategory, StoreMenu, CartItem, Review, CustomUser
from main.forms import CustomAuthenticationForm, CustomUserCreationForm
from django.contrib import messages
import logging
logger = logging.getLogger(__name__)

#1. html 파일을 인코딩해서 웹에 띄우는 작
def home_view(request):
    homebannerimgs = HomeBannerImg.objects.all()
    categories = DishesCategory.objects.all()
    return render(request, 'main/home.html', {'homebannerimgs': homebannerimgs, 'categories': categories})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)# 정보
        valid = form.is_valid()
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        if valid: #폼이 유효함(필드를 적당하게 적었는지)
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('main:home')

        else: #폼이 유효하지 않음
            existing_user = CustomUser.objects.filter(username=username).first()
            if existing_user:
                context = {
                    'error': '비밀번호를 확인해주세요'
                }
            else:
                context = {
                    'error': '존재하지 않는 사용자 입니다'
                }
            return render(request, 'main/login.html', context)
    else: #제대로된 방식으로 전달되지 않음
        form = CustomAuthenticationForm()
        return render(request, 'main/login.html', {form: form})

    return render(request, 'main/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('main:home')

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main:home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'main/signup.html', {'form': form})

#아이디 중복체크
def check_username(request):
    username = request.GET.get('username', None)
    if username:
        is_taken = CustomUser.objects.filter(username=username).exists()
        data = {'is_taken': is_taken}
        return JsonResponse(data)
    else:
        # username이 전달되지 않은 경우에 대한 처리
        return JsonResponse({'error': 'Username이 전달되지 않았습니다.'})

#검색기능
def search_view(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        stores = Store.objects.filter(name__contains=searched)
        return render(request, 'main/searched.html', {'searched': searched, 'stores': stores})
    else:
        return render(request, 'main/searched.html')

#음식 카테고리 리스트
def store_list_view(request, category_id):
    category = get_object_or_404(DishesCategory, pk=category_id)
    stores = Store.objects.filter(dishes_categories=category)
    return render(request, 'main/store_list.html', {'stores': stores, 'category': category})

#가게 상세설명
def store_posting_view(request, store_id):
    store = get_object_or_404(Store, pk=store_id)
    menus = StoreMenu.objects.filter(store=store)
    return render(request, 'main/store_posting.html', {'store': store, 'menus': menus})

#장바구니에 메뉴 추가 and 장바구니에 수량 1개 증가
def cart_add_view(request, menu_id):
    menu = get_object_or_404(StoreMenu, pk=menu_id)
    existing_item = CartItem.objects.filter(user=request.user, menu=menu).first()

    if existing_item:
        existing_item.quantity += 1
        existing_item.save()
    else:
        CartItem.objects.create(user=request.user, menu=menu)

    return redirect('main:cart')

#장바구니에 수량 1개 삭제
def cart_minus_view(request, menu_id):
    menu = get_object_or_404(StoreMenu, pk=menu_id)
    existing_item = CartItem.objects.filter(user=request.user, menu=menu).first()

    if existing_item.quantity > 1:
        existing_item.quantity -= 1
        existing_item.save()
    else:
        existing_item.delete() #해당 메뉴 장바구니에서 삭제
    return redirect('main:cart')

#장바구니에서 메뉴 삭제
def cart_delete_view(request, menu_id):
    menu = get_object_or_404(StoreMenu, pk=menu_id)
    existing_item = CartItem.objects.filter(user=request.user, menu=menu).first()
    if existing_item:
        existing_item.delete()

    return redirect('main:cart')

#장바구니 뷰
def cart_view(request):
    # 장바구니에 담긴 상품들을 보여주는 페이지
    # 이때 user은 자동으로 CustomUser의 User을 조회(user = models.ForeignKey('main.CustomUser', on_delete=models.CASCADE))이부분 때문에
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'main/shopping_cart.html', {'cart_items': cart_items})

#리뷰 뷰
def review_view(request, store_id):
    store = get_object_or_404(Store, pk=store_id)
    reviews = Review.objects.filter(store=store)
    my_reviews = Review.objects.filter(user=request.user, store=store)

    return render(request, 'main/review.html', {'store': store, 'reviews': reviews, 'my_reviews': my_reviews})


#####
def test(request):
    return render(request, 'main/test.html')

def blog(request):
    postlist = Post.objects.all()
    return render(request, 'main/blog.html', {'postlist': postlist})
def posting(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    post = Post.objects.get(pk=pk)
    return render(request, 'main/posting.html', {'post': post})
