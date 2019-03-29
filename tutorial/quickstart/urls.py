from django.conf.urls import url, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()



# 使用自动URL路由连接我们的API。
# 另外，我们还包括支持浏览器浏览API的登录URL。
urlpatterns = [

]

router.register(r'users', views.UserViewSet)
urlpatterns += router.urls

router.register(r'groups', views.GroupViewSet)
urlpatterns += router.urls
