from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('',Home,name='home'),
    path('user/',LogIn,name='login'),
    path('checkKyc/<str:walletAddresss>/',isKycVerified_1,name='checkKyc'),
    path('uploadKyc/<str:walletAddress>/',kycFileUploadDone,name='kycFileUploadDone'),
    path('userpage/<str:walletAddress>/',UserPage,name='userpage'),
    path('userpage/<str:walletAddress>/quiz/<str:quizId>/',quizzPage,name='quizzPage'),
    path('adminpanel/',AdminPanel,name='adminpanel'),
    path('addQuestion/',addQuestion,name='addQuestion')
    

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)