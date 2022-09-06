from django.contrib import admin
from .models import *
from django import forms
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget

# Register your models here.


class MovieAdminForm(forms.ModelForm):
    description = forms.CharField(label='Description', widget=CKEditorUploadingWidget())

    class Meta:
        model = Movie
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    list_display_links = ('name',)


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_image')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = 'Image'


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')


class ReviewsInline(admin.TabularInline):
    model = Review
    extra = 1
    readonly_fields = ('name', 'email')


class MovieShotsInline(admin.TabularInline):
    model = MovieShots
    extra = 1
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f"<img src={obj.image.url} width='100' height='110'")

    get_image.short_description = 'Image'


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'url', 'draft')
    list_filter = ('category', 'year')
    search_fields = ('title', 'category__name')
    save_on_top = True
    save_as = True
    list_editable = ('draft',)
    actions = ["publish", "unpublish"]
    # fields = (('actors', 'directors', 'genres'),)
    form = MovieAdminForm
    readonly_fields = ('get_poster',)
    inlines = [MovieShotsInline, ReviewsInline]
    fieldsets = (
        (None, {
            "fields": (("title", "tagline"),)
        }),
        (None, {
            "fields": ("description", ("poster", "get_poster"))
        }),
        (None, {
            "fields": (("year", "world_premiere", "country"),)
        }),
        ("Actors", {
            "classes": ("collapse",),
            "fields": (("actors", "directors", "genres", "category"),)
        }),
        (None, {
            "fields": (("budget", "fees_in_usa", "fess_in_world"),)
        }),
        ("Options", {
            "fields": (("url", "draft"),)
        }),
    )

    def get_poster(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="100" height="110"')

    def unpublish(self, request, queryset):
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = "1 record was update"
        else:
            message_bit = f"{row_update} records was update"
        self.message_user(request, f"{message_bit}")

    def publish(self, request, queryset):
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = "1 record was update"
        else:
            message_bit = f"{row_update} records was update"
        self.message_user(request, f"{message_bit}")

    publish.short_description = 'Publish'
    unpublish.short_description = 'Unpublish'

    publish.allowed_permissions = ('change',)
    unpublish.allowed_permissions = ('change',)

    get_poster.short_description = 'Poster'


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'movie', 'get_image')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = 'Image'


# @admin.register(RatingStar)
# class RatingStarAdmin(admin.ModelAdmin):
#     list_display = ('id', 'value')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'ip', 'movie', 'star')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'parent', 'movie')
    readonly_fields = ('name', 'email')


admin.site.site_title = 'Django Movies'
admin.site.site_header = 'Django Movies'

admin.site.register(RatingStar)


