from django.contrib import admin
from django.urls import path
from drugapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.bas,name='base'),
    path('af',views.acform,name='Anrform'),
    path('plog',views.pollog,name='Policelogin'),
    path('socw',views.socwor,name='socwellogin'),
    path('poldash',views.poldash,name='poldash'),
    path('logout',views.Logout,name="lout"),
    path('com',views.complaint,name='com'),
    path('vc/<int:id>',views.viecom,name='vc'),
    path('alf',views.alform,name='alf'),
    path('alm',views.alertmsg,name='almsg'),
    path('va/<int:id>',views.viewalert,name='va'),
    path('awan',views.adetails,name='aw'),
    path('acom/<int:id>',views.acom,name='acom'),
    path('pwan',views.wanv,name='wanv'),
    path('vwan/<int:id>',views.vwan,name='vwan'),
    path('vwancom/<int:id>',views.vwancom,name='vwancom'),
    path('sur',views.survey,name='surway'),
    path('maln',views.maln,name='maln')

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)