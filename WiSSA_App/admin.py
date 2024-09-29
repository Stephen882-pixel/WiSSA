from django.contrib import admin
from .models import SubscribedUsers,Post
from tinymce.widgets import TinyMCE
from django import forms


class SubscribedUsersAdmin(admin.ModelAdmin):
    list_display = ('email','created_date')

class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'body': TinyMCE(attrs={'cols': 80, 'rows': 30}),
        }

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    

# Register your models here.


admin.site.register(SubscribedUsers,SubscribedUsersAdmin)
admin.site.register(Post)
