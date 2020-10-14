from django.urls import path

from stock import views

urlpatterns = [
path('indexview/',views.IndexView.as_view(),name="index"),
path('index_data/',views.IndexDataView.as_view()),
path('add_focus/<int:id>',views.add_focus.as_view()),
path('centerview/',views.CenterView.as_view()),
path('index.html/',views.RedictIndex.as_view()),
path('center_data/',views.CenterDataView.as_view()),
path('del_focus/<str:code>',views.DelFocus.as_view()),
path('update_focus/<str:code>',views.UpdateFocus.as_view()),
path('noteinfo_update/<str:code>/<str:noteinfo>',views.UpdateNoteInfo.as_view()),

]
