from django.contrib import admin
from .models import Categorie, Sous_Categorie, Article, ImgTable, Commande, LienImage, Taille
"""
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

class KinAchatLocationSite(AdminSite):
    site_title = ugettext_lazy('KinAchat & Location site Admin')
    site_header = ugettext_lazy('KinAchat & Location administration')
    index_title = ugettext_lazy('Site administration')

kin_achat_location_site=KinAchatLocationSite()
"""
# Register your models here.
admin.site.register(Categorie)
admin.site.register(Article)
admin.site.register(Commande)
admin.site.register(Sous_Categorie)
admin.site.register(ImgTable)
admin.site.register(LienImage)
admin.site.register(Taille)
