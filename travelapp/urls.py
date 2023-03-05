from. import views
from django.urls import path



urlpatterns = [

    path('',views.cycle,name='cycle'),
    path('aboutcycle/',views.aboutcycle,name='aboutcycle'),
    path('contactcycle/',views.contactcycle,name='contactcycle'),
    path('indexcycle/',views.indexcycle,name='indexcycle'),
    path('newscycle/',views.newscycle,name='newscycle')

]



#urlpatterns = [

    # path('',views.Home,name='Home'),
    # path('About/',views.About,name='About'),
    # path('Contact/',views.Contact,name='Contact'),
    # path('Details/',views.Details,name='Details'),
    # path('Thanks/',views.Thanks,name='Thanks')
#  ]
