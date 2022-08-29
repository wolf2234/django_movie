from django.contrib import admin
from .models import *

# Register your models here.
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = '__all__'
#
#     class Meta:
#         model = Category

admin.site.register(Category)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(MovieShots)
admin.site.register(RatingStar)
admin.site.register(Rating)
admin.site.register(Reviews)


