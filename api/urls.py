from django.urls import path
from . import views
urlpatterns = [
    path('',views.apiOverview ,name="api-overview" ),
    path('task-list/',views.tasklist ,name="task-list" ),
    path('task-list-my/',views.my.as_view() ,name="task-list-my" ),
    path('task-detail/<str:pk>/',views.task_detail ,name="task-detail" ),
    path('task-create/',views.task_create ,name="task-create" ),
    path('task-update/<str:pk>/',views.task_update,name="task-update" ),
    path('task-delete/<str:pk>/',views.task_delete,name="task-delete" ),

]