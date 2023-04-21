from django.contrib import admin 
from .models import ProductPerson, ProductDetails 

class ProductDetailsInline(admin.StackedInline):
    model = ProductDetails 
    can_delete = False
    verbose_name_plural = 'ProductDetails'
    list_display_links =('age',)
    
class ProductPersonAdmin(admin.ModelAdmin):
    inlines = [ProductDetailsInline]
    list_display = ('id','name','age','email')
    list_display_links = ('id', 'name')
    
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        
admin.site.register(ProductPerson, ProductPersonAdmin)
admin.site.register(ProductDetails)