from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.home,name ='todo_list'),
    path('add/',views.add_todo,name='add_todo'),
    path('addlist/',views.addList,name='addlist'),
    path('addform/<int:id>',views.additem_page,name='addform'),
    path('addtodo/',views.add_todo,name='addtodo'),
    path('todoitem/<int:id>',views.todo_item_page,name='todoitem'),
    path('deletelist/<int:id>',views.delete_list,name='deletelist'),
    path('deleteitem/<int:id>',views.delete_todo,name='deletetodo'),
    

]