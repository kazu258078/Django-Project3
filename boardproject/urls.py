from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('boardapp.urls')),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
] 
# print("Media_Root", static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
# print("Static_Root", *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#STATIC_ROOTがなければSTATICFILES_DIRSを探しに行く  



# プロジェクト作成
# django-admin startproject boardproject .
# アプリ作成
# python manage.py startapp boardapp
# templatesフォルダの作成
# settings.pyのINSTALLED_APPSとDIRSを指定(BASE_DIRはmanage.pyがあるところ)
# プロジェクトのurls.pyでアプリへのつなぎ込みを指定
# アプリ側のurls.pyを作成

# admin画面用のユーザーを作成(kazu,kazu)
# python manage.py createsuperuser

# model作成後に python manage.py makemigrationsとpython manage.py migrate
# admin.pyにfrom .models import BoardModelとadmin.site.register(BoardModel)を登録