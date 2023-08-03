from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Good, Category, News, ArchivedItem


class GoodAdmin(ModelAdmin):
    actions = ['execute_scrapy_command_express_tribune', 'execute_scrapy_command_dawn_news',
               'execute_scrapy_command_geo_news', 'execute_scrapy_command_dawn_highlights', 'execute_scrapy_command_Top']

    def execute_scrapy_command_express_tribune(self, request, queryset):
        import subprocess
        subprocess.run(["scrapy", "crawl", "ExpressTribune"],
                       cwd='C:/Users/Fahad Mehdi/Django Projects/Myfyp/News aggregator/scrapy_quotes/scrapy_quotes')
        self.message_user(request, "Scrapy command for ExpressTribune executed successfully.")

    def execute_scrapy_command_dawn_news(self, request, queryset):
        import subprocess
        subprocess.run(["scrapy", "crawl", "DawnNews"],
                       cwd='C:/Users/Fahad Mehdi/Django Projects/Myfyp/News aggregator/scrapy_quotes/scrapy_quotes')
        self.message_user(request, "Scrapy command for DawnNews executed successfully.")

    def execute_scrapy_command_geo_news(self, request, queryset):
        import subprocess
        subprocess.run(["scrapy", "crawl", "GeoNews"],
                       cwd='C:/Users/Fahad Mehdi/Django Projects/Myfyp/News aggregator/scrapy_quotes/scrapy_quotes')
        self.message_user(request, "Scrapy command for GeoNews executed successfully.")

    def execute_scrapy_command_dawn_highlights(self, request, queryset):
        import subprocess
        subprocess.run(["scrapy", "crawl", "DawnHighlights"],
                       cwd='C:/Users/Fahad Mehdi/Django Projects/Myfyp/News aggregator/scrapy_quotes/scrapy_quotes')
        self.message_user(request, "Scrapy command for DawnHighlights executed successfully.")

    def execute_scrapy_command_Top(self, request, queryset):
        import subprocess
        subprocess.run(["scrapy", "crawl", "TOP"],
                       cwd='C:/Users/Fahad Mehdi/Django Projects/Myfyp/News aggregator/scrapy_quotes/scrapy_quotes')
        self.message_user(request, "Scrapy command for TOP executed successfully.")

    execute_scrapy_command_express_tribune.short_description = "Execute Scrapy Command (ExpressTribune)"
    execute_scrapy_command_dawn_news.short_description = "Execute Scrapy Command (DawnNews)"
    execute_scrapy_command_geo_news.short_description = "Execute Scrapy Command (GeoNews)"
    execute_scrapy_command_dawn_highlights.short_description = "Execute Scrapy Command (DawnHighlights)"
    execute_scrapy_command_Top.short_description = "Execute Scrapy Command (TOP)"


admin.site.register(Good, GoodAdmin)
admin.site.register(Category)
admin.site.register(News)
admin.site.register(ArchivedItem)
