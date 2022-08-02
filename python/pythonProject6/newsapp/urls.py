from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="indexfile"),
    path('international', views.international, name="internationalfile"),
    path('national', views.national, name="nationalfile"),
    path('entertainment', views.entertainment, name="entertainmentfile"),
    path('politics', views.politics, name="politicsfile"),
    path('health', views.health, name="healthfile"),
    path('sports', views.sports, name="sportsfile"),
    path('education', views.education, name="educationfile"),
    path('business', views.business, name="businessfile"),
    path('miscellaneous', views.miscellaneous, name="miscellaneousfile"),
    path('world', views.world, name="worldfile"),
    path('science', views.science, name="sciencefile"),
    path('hatke', views.hatke, name="hatkefile"),
    path('technology', views.technology, name="technologyfile"),
    path('automobile', views.automobile, name="automobilefile"),
    path('startup', views.startup, name="startupfile"),
]