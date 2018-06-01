from django.contrib import admin

from .models import *

admin.site.register((Character, Fighter, Mage, Cleric, Thief, Necromancer))
