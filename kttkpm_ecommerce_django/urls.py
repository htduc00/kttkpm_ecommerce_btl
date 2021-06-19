"""kttkpm_ecommerce_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.contrib import admin

from django.conf.urls.static import static
from django.urls import path, include
from user import views as UserViews
import home
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('home/', include('home.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('user/', include('user.urls'), name='user'),
    path('logout/', UserViews.logout_func, name='logout'),
    path('login/', UserViews.login_form, name='login'),
    path('signup/', UserViews.signup_form, name='signup'),
    path('product/<int:id>/<slug>/', views.product_detail, name='product_detail'),
    path('addreview/<int:id>', views.addreview, name='addreview'),
    path('addcomment/<int:id>', views.addcomment, name='addcomment'),
    path('addcommentreply/<int:id>', views.addcommentreply, name='addcommentreply'),
    path('addtoshopcart', views.addtoshopcart, name='addtoshopcart'),
    path('shopcart', views.shopcart, name='shopcart'),
    path('deletefromcart/<int:id>',views.deletefromcart,name='deletefromcart'),
    path('orderproduct',views.orderproduct,name='orderproduct'),
    path('browserInvoice', views.browserInvoice, name="browserInvoice"),
    path('waitingInvoiceDetail/<int:orderID>', views.waitingInvoiceDetail, name="waitingInvoiceDetail"),
    path('exportInvoice', views.exportInvoice, name="exportInvoice"),
    path('admin/addProduct/', views.addProduct, name="adminAddProduct"),
    path('admin/submitProductOne/', views.submitProductOne, name="submitProductOne"),
    path('admin/submitProductTwo/', views.submitProductTwo, name="submitProductTwo"),
    path('admin/listProduct/', views.listProduct, name="adminListProduct"),
    path('admin/detailProduct/<int:id>',views.detailProduct, name='adminDetailProduct'),
    path('admin/reviewReport', views.reviewReport, name='adminReviewReport'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
