
from django.urls import path
from .views import OrderCreateView, ReviewCreateView, ExpenseCreateView

urlpatterns = [
    path('add-order/', OrderCreateView.as_view(), name='add-order'),
    path('add-review/', ReviewCreateView.as_view(), name='add-review'),
    path('add-expense/', ExpenseCreateView.as_view(), name='add-expense')
]
