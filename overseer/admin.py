from django.contrib import admin

from overseer.models import Service, Event, EventUpdate

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'order', 'date_updated')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}

class EventAdmin(admin.ModelAdmin):
    list_display = ('date_created', 'status', 'message')
    search_fields = ('message',)
    list_filter = ('services',)

class EventUpdateAdmin(admin.ModelAdmin):
    list_display = ('date_created', 'message', 'status', 'event')
    search_fields = ('message',)

admin.site.register(Service, ServiceAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(EventUpdate, EventUpdateAdmin)