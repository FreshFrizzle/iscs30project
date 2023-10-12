from django.urls import path
from .views import (
            index, WidgetUserDetailView, WidgetUserCreateView, WidgetUserUpdateView 
        )


urlpatterns = [
    path('', index, name='index'),
    path('widgetusers/add', WidgetUserCreateView.as_view(), name='widgetuser-add'),
    path('widgetusers/<int:pk>/details', WidgetUserDetailView.as_view(), name='widgetuser-details'),
    path('widgetusers/<int:pk>/edit', WidgetUserUpdateView.as_view(), name='widgetuser-edit')
]

app_name = "dashboard"