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
    # path('finches/<int:finch_id>/add-feeding/', views.add_feeding, name='add-feeding'),
    # path('toys/create/', views.ToyCreate.as_view(), name='toy-create'),
    # path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toy-detail'),
    # path('toys/', views.ToyList.as_view(), name='toy-index'),
    # path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toy-update'),
    # path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toy-delete'),
    # path('cats/<int:finch_id>/assoc-toy/<int:toy_id>/', views.assoc_toy, name='assoc-toy'),
]
