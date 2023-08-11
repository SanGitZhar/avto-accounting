from django.urls import path
from .views import AutoView, add_auto, add_worker, worker_detail

urlpatterns = [
    path('', AutoView.as_view(), name='index'),
    path('auto_creation/', add_auto, name='add_auto'),
    path('worker_creation/', add_worker, name='add_worker'),
    path('worker_detail/<int:worker_id>', worker_detail, name='worker_detail'),
]