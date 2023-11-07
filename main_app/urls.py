from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
    path('memories/', views.memory_index, name='memory-index'),
    path('memories/<int:memory_id>/', views.memory_detail, name='memory-detail'),
    path('memories/create/', views.MemoryCreate.as_view(), name='memory-create'),
    path('memories/<int:pk>/update/', views.MemoryUpdate.as_view(), name='memory-update'),
    path('memories/<int:pk>/delete/', views.MemoryDelete.as_view(), name='memory-delete'),
]
