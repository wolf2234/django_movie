from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    list_display_links = ('name',)

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age')

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')


class ReviewsInline(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = ('name', 'email')


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'url', 'draft')
    list_filter = ('category', 'year')
    search_fields = ('title', 'category__name')
    inlines = [ReviewsInline]
    save_on_top = True
    save_as = True
    list_editable = ('draft',)
    # fields = (('actors', 'directors', 'genres'),)
    fieldsets = (
        (None, {'fields': (('title', 'tagline'),)}),
        (None, {'fields': ('description', 'poster')}),
        (None, {'fields': (('year', 'world_premiere', 'county'),)}),
        ('Actors', {
            'classes': ('collapse',),
            'fields': (('actors', 'directors', 'genres', 'category'),)
        }),
        (None, {'fields': (('budget', 'fees_in_usa', 'fess_in_world'),)}),
        ('Options', {'fields': (('url', 'draft'),)}),
    )


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'movie')


@admin.register(RatingStar)
class RatingStarAdmin(admin.ModelAdmin):
    list_display = ('id', 'value')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'ip', 'name')


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'parent', 'movie')
    readonly_fields = ('name', 'email')


# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Actor, ActorAdmin)
# admin.site.register(Genre, GenreAdmin)
# admin.site.register(Movie, MovieAdmin)
# admin.site.register(MovieShots, MovieShotsAdmin)
# admin.site.register(RatingStar, RatingStarAdmin)
# admin.site.register(Rating, RatingAdmin)
# admin.site.register(Reviews, ReviewsAdmin)


