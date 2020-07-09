from django.db import models

# Create your models here.

class BoardModel(models.Model):
    title = models.CharField(max_length=100)
    # TextFieldは長い文字をいれる場合に使用
    content = models.TextField()
    author = models.CharField(max_length=100)
    # upload_toでどこにuploadするかを指定する(settingsの中でImageファイルをどこにいれるかの指定をしている)
    # upload_toはsettingsで指定したものからさらに細かいディレクトリを指定(Modelごとに設定できる)
    # 何も書かなければsettingsで指定したデフォルトのディレクトリに入る
    images = models.ImageField(upload_to='')
    good = models.IntegerField(null=True, blank=True, default=0)
    read = models.IntegerField(null=True, blank=True, default=0)
    readtext = models.CharField(max_length=200, null=True, blank=True, default='a')
