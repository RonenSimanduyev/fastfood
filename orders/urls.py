from django.urls import path,include
from . import views
from rest_framework import routers
# from rest_framework.urlpatterns import format_suffix_patterns

router=routers.DefaultRouter()
router.register('category',views.CategoryView)
router.register('orders',views.OrdersView)
# router.register('orders',views.OrdersList, basename='MyModel')
router.register('dish',views.DishView)

urlpatterns=[
    path('',include(router.urls)),
    # path('orders/', views.OrdersList.as_view())
]

# urlpatterns = format_suffix_patterns(urlpatterns)
