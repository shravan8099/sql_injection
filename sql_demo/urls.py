from django.urls import path
from . import views

urlpatterns=[
    path("main/",views.index,name='main'),
    path("solution1/",views.solution1,name='solution1'),
    path("solution2/",views.solution2,name='solution2'),

    
    path("fault_system/",views.fault_system,name='fault_system'),
    path("solution_one/",views.solution_one,name='solution_one'),
    path("solution_two/",views.solution_two,name='solution_two'),
]