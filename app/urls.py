from django.urls import path
from . import views

urlpatterns = [

    # setup the game
    path('', views.init, name="init"),

    # start the game
    path('start', views.start, name="start"),

    # draw api
    path('api/draw', views.draw, name="draw"),

    # get all remaining cards
    path('api/remaining', views.remaining, name="remaining"),

    # get all drawed cards
    path('api/drawed', views.drawed, name="drawed"),


]
