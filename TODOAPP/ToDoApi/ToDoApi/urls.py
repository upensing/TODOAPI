
from django.contrib import admin
from django.urls import path

from api.views import Entry, taskCreate, taskDelete, taskList #,taskUpdate

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", Entry),
    path("task_list/", taskList),
    path("task_create/", taskCreate),
    path("task_delete/<int:taskId>/", taskDelete),
    #path("task_update/<int:taskId>/", taskUpdate)
]
