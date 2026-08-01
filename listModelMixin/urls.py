
from django.contrib import admin
from django.urls import path,include
from ModelMixin import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api-auth/', include('rest_framework.urls')),

    path('mixinlist/', views.ModelMixinList.as_view(), name='mixinlist'),
    path('mixincreate/', views.ModelMixinCreate.as_view(), name='mixincreate'),
]
