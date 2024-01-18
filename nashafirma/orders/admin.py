from .models import Order
from django.utils import timezone
from datetime import timedelta

from django.contrib import admin

class DateYesterdayFieldListFilter(admin.DateFieldListFilter):
    def __init__(self, field, request, params, model, model_admin, field_path):
        super().__init__(field, request, params, model, model_admin, field_path)

        today = timezone.now().date()
        tomorrow = today + timedelta(days=1)
        yesterday = today - timedelta(days=1)

        self.links = list(self.links)
        self.links.insert(
            2,
            (
                "Вчора",
                {
                    self.lookup_kwarg_since: str(yesterday),
                    self.lookup_kwarg_until: str(today),
                },
            ),
        )

        self.links = list(self.links)
        self.links.insert(
            2,
            (
                "Вчора та Сьогодні",
                {
                    self.lookup_kwarg_since: str(yesterday),
                    self.lookup_kwarg_until: str(tomorrow),
                },
            ),
        )


class MyModelAdmin(admin.ModelAdmin):
    list_display = ["created_at", "user", "done"]
    search_fields = ("created_at", "user", "done", "products")
    list_display_links = ("created_at", "user")
    # list_editable = ()
    list_filter = (("created_at", DateYesterdayFieldListFilter), "user", "done")


admin.site.register(Order, MyModelAdmin)

