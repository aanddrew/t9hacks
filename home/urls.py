from django.urls import path


from .views import *

urlpatterns = [
        path('', HomePageView.as_view(), name='home'),
        path('addUser/', add_User_Form_Submission, name='addUser'),
        #path('sendcommand/', send_Command_Form_Submission, name='sendCommand'),
    ]
