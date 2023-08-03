import subprocess
import random
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetView, \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.core.paginator import Paginator
from django.shortcuts import redirect, get_object_or_404, render
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from datetime import date, timedelta

from django.views.decorators.http import require_POST
from django.views.generic import TemplateView, CreateView, ListView
from .models import News, Category, History, ArchivedItem
from django.db.models import Q
import re
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class MainPage(TemplateView):
    template_name = "fyp/MainPage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        search_query = self.request.GET.get('q')
        date_str = self.request.GET.get('date')

        if date_str:
            news_date = date.fromisoformat(date_str)
        else:
            news_date = date.today()

        if search_query:
            # Split the search query into individual words
            words = search_query.split()

            # Initialize an empty Q object for the query
            query = Q()

            # Perform search using OR operator for individual words
            for word in words:
                # Use regex to match whole words only
                word_regex = r'\b{}\b'.format(re.escape(word))
                query |= Q(title__iregex=word_regex) | Q(content__iregex=word_regex)

            # Filter the news items by the query and the specified date
            geopakistan_items = News.objects.filter(query, date_added=news_date, category__name='Geo Pakistan')
            geobusiness_items = News.objects.filter(query, date_added=news_date, category__name='Geo Business')
            geotechnology_items = News.objects.filter(query, date_added=news_date, category__name='Geo Technology')
            geoentertainment_items = News.objects.filter(query, date_added=news_date,
                                                         category__name='Geo Entertainment')
            geosports_items = News.objects.filter(query, date_added=news_date, category__name='Geo Sports')
            geoworld_items = News.objects.filter(query, date_added=news_date, category__name='Geo World')
            dawnpakistan_items = News.objects.filter(query, date_added=news_date, category__name='Dawn Pakistan')
            dawnbusiness_items = News.objects.filter(query, date_added=news_date, category__name='Dawn Business')
            dawnworld_items = News.objects.filter(query, date_added=news_date, category__name='Dawn World')
            dawnsports_items = News.objects.filter(query, date_added=news_date, category__name='Dawn Sports')
            dawntechnology_items = News.objects.filter(query, date_added=news_date, category__name='Dawn Technology')
            dawnworldentertainment_items = News.objects.filter(query, date_added=news_date,
                                                               category__name='Dawn World Entertainment')
            dawnbusinessentertainment_items = News.objects.filter(query, date_added=news_date,
                                                                  category__name='Dawn Business Entertainment')
            dawnpakistanentertainment_items = News.objects.filter(query, date_added=news_date,
                                                                  category__name='Dawn Pakistan Entertainment')
            expresspakistan_items = News.objects.filter(query, date_added=news_date, category__name='Express Pakistan')
            expressbusiness_items = News.objects.filter(query, date_added=news_date, category__name='Express Business')
            expressworld_items = News.objects.filter(query, date_added=news_date, category__name='Express World')
            expresstechnology_items = News.objects.filter(query, date_added=news_date, category__name='Express '
                                                                                                      'Technology')
            expressentertainment_items = News.objects.filter(query, date_added=news_date, category__name='Express '
                                                                                                         'Entertainment')
            expresssports_items = News.objects.filter(query, date_added=news_date, category__name='Express Sports')
            bbctop_items = News.objects.filter(query, date_added=news_date, category__name='BBC Top')
            thenewstop_items = News.objects.filter(query, date_added=news_date, category__name='TheNews Top')
            dunyanewstop_items = News.objects.filter(query, date_added=news_date, category__name='Dunya Top')

            # if self.request.user.is_authenticated:
            #     history_items = History.objects.filter(user=self.request.user)

        else:
            geopakistan_items = News.objects.filter(date_added=news_date, category__name='Geo Pakistan')
            geobusiness_items = News.objects.filter(date_added=news_date, category__name='Geo Business')
            geotechnology_items = News.objects.filter(date_added=news_date, category__name='Geo Technology')
            geoentertainment_items = News.objects.filter(date_added=news_date, category__name='Geo Entertainment')
            geosports_items = News.objects.filter(date_added=news_date, category__name='Geo Sports')
            geoworld_items = News.objects.filter(date_added=news_date, category__name='Geo World')
            dawnpakistan_items = News.objects.filter(date_added=news_date, category__name='Dawn Pakistan')
            dawnbusiness_items = News.objects.filter(date_added=news_date, category__name='Dawn Business')
            dawnworld_items = News.objects.filter(date_added=news_date, category__name='Dawn World')
            dawnsports_items = News.objects.filter(date_added=news_date, category__name='Dawn Sports')
            dawntechnology_items = News.objects.filter(date_added=news_date, category__name='Dawn Technology')
            dawnworldentertainment_items = News.objects.filter(date_added=news_date,
                                                               category__name='Dawn World Entertainment')
            dawnbusinessentertainment_items = News.objects.filter(date_added=news_date,
                                                                  category__name='Dawn Business Entertainment')
            dawnpakistanentertainment_items = News.objects.filter(date_added=news_date,
                                                                  category__name='Dawn Pakistan Entertainment')
            expresspakistan_items = News.objects.filter(date_added=news_date, category__name='Express Pakistan')
            expressbusiness_items = News.objects.filter(date_added=news_date, category__name='Express Business')
            expressworld_items = News.objects.filter(date_added=news_date, category__name='Express World')
            expresstechnology_items = News.objects.filter(date_added=news_date, category__name='Express Technology')
            expressentertainment_items = News.objects.filter(date_added=news_date, category__name='Express '
                                                                                                  'Entertainment')
            expresssports_items = News.objects.filter(date_added=news_date, category__name='Express Sports')
            bbctop_items = News.objects.filter(date_added=news_date, category__name='BBC Top')
            thenewstop_items = News.objects.filter(date_added=news_date, category__name='TheNews Top')
            dunyanewstop_items = News.objects.filter(date_added=news_date, category__name='Dunya Top')

        context['geopakistan_items'] = geopakistan_items
        context['geobusiness_items'] = geobusiness_items
        context['geotechnology_items'] = geotechnology_items
        context['geoentertainment_items'] = geoentertainment_items
        context['geosports_items'] = geosports_items
        context['geoworld_items'] = geoworld_items
        context['dawnpakistan_items'] = dawnpakistan_items
        context['dawnbusiness_items'] = dawnbusiness_items
        context['dawnworld_items'] = dawnworld_items
        context['dawnsports_items'] = dawnsports_items
        context['dawntechnology_items'] = dawntechnology_items
        context['dawnworldentertainment_items'] = dawnworldentertainment_items
        context['dawnbusinessentertainment_items'] = dawnbusinessentertainment_items
        context['dawnpakistanentertainment_items'] = dawnpakistanentertainment_items
        context['expresspakistan_items'] = expresspakistan_items
        context['expressbusiness_items'] = expressbusiness_items
        context['expressworld_items'] = expressworld_items
        context['expresstechnology_items'] = expresstechnology_items
        context['expressentertainment_items'] = expressentertainment_items
        context['expresssports_items'] = expresssports_items
        context['bbctop_items'] = bbctop_items
        context['thenewstop_items'] = thenewstop_items
        context['dunyanewstop_items'] = dunyanewstop_items
        context['user'] = self.request.user  # Add the user object to the context
        return context


def update_last_visited(request, news_id):
    models = [News]

    for model in models:
        try:
            news_item = model.objects.get(id=news_id)
            news_item.last_visited = timezone.now()
            news_item.save()

            # Only save to history if the user is logged in
            if request.user.is_authenticated:
                history_item = History(user=request.user, content=news_item.content, url=news_item.url,
                                       category=news_item.category)
                history_item.save()

            return redirect(news_item.url)  # Redirect to the news URL
        except model.DoesNotExist:
            pass

    return redirect('fyp:MainPage')


def without_history(request, news_id):
    models = [News]

    for model in models:
        try:
            news_item = model.objects.get(id=news_id)
            news_item.last_visited = timezone.now()
            news_item.save()
            return redirect(news_item.url)  # Redirect to the news URL
        except model.DoesNotExist:
            pass

    return redirect('fyp:MainPage')


class TechnologyPage(TemplateView):
    template_name = "fyp/Technology.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_query_1 = self.request.GET.get('q_1')
        date_str = self.request.GET.get('date')

        if date_str:
            news_date = date.fromisoformat(date_str)
        else:
            news_date = date.today()

        if search_query_1:
            # Split the search query into individual words
            words = search_query_1.split()

            # Initialize an empty Q object for the query
            query = Q()

            # Perform search using OR operator for individual words
            for word in words:
                # Use regex to match whole words only
                word_regex = r'\b{}\b'.format(re.escape(word))
                query |= Q(title__iregex=word_regex) | Q(content__iregex=word_regex)
            geotechnology_items = News.objects.filter(query, date_added=news_date, category__name='Geo Technology')
            expresstechnology_items = News.objects.filter(query, date_added=news_date,
                                                          category__name='Express Technology')
            dawntechnology_items = News.objects.filter(query, date_added=news_date, category__name='Dawn Technology')
        else:
            # If no search query is provided, retrieve all news items for the specified date and category
            geotechnology_items = News.objects.filter(date_added=news_date, category__name='Geo Technology')
            expresstechnology_items = News.objects.filter(date_added=news_date, category__name='Express Technology')
            dawntechnology_items = News.objects.filter(date_added=news_date, category__name='Dawn Technology')

        combined_items = list(geotechnology_items) + list(expresstechnology_items) + list(dawntechnology_items)
        random.shuffle(combined_items)

        paginator = Paginator(combined_items, self.paginate_by)
        page_number = self.request.GET.get('page', 1)
        items = paginator.get_page(page_number)

        context['items'] = items
        return context


class SportsPage(TemplateView):
    template_name = "fyp/Sports.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_query_1 = self.request.GET.get('q_1')
        date_str = self.request.GET.get('date')

        if date_str:
            news_date = date.fromisoformat(date_str)
        else:
            news_date = date.today()

        if search_query_1:
            # Split the search query into individual words
            words = search_query_1.split()

            # Initialize an empty Q object for the query
            query = Q()

            # Perform search using OR operator for individual words
            for word in words:
                # Use regex to match whole words only
                word_regex = r'\b{}\b'.format(re.escape(word))
                query |= Q(title__iregex=word_regex) | Q(content__iregex=word_regex)
            geosports_items = News.objects.filter(query, date_added=news_date, category__name='Geo Sports')
            expresssports_items = News.objects.filter(query, date_added=news_date, category__name='Express Sports')
            dawnsports_items = News.objects.filter(query, date_added=news_date, category__name='Dawn Pakistan Sports')
        else:
            # If no search query is provided, retrieve all news items for the specified date and category
            geosports_items = News.objects.filter(date_added=news_date, category__name='Geo Sports')
            expresssports_items = News.objects.filter(date_added=news_date, category__name='Express Sports')
            dawnsports_items = News.objects.filter(date_added=news_date, category__name='Dawn Sports')

        combined_items = list(geosports_items) + list(expresssports_items) + list(dawnsports_items)
        random.shuffle(combined_items)

        paginator = Paginator(combined_items, self.paginate_by)
        page_number = self.request.GET.get('page', 1)
        items = paginator.get_page(page_number)

        context['items'] = items
        return context


class EntertainmentPage(TemplateView):
    template_name = "fyp/Entertainment.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_query_1 = self.request.GET.get('q_1')
        date_str = self.request.GET.get('date')

        if date_str:
            news_date = date.fromisoformat(date_str)
        else:
            news_date = date.today()

        if search_query_1:
            # Split the search query into individual words
            words = search_query_1.split()

            # Initialize an empty Q object for the query
            query = Q()

            # Perform search using OR operator for individual words
            for word in words:
                # Use regex to match whole words only
                word_regex = r'\b{}\b'.format(re.escape(word))
                query |= Q(title__iregex=word_regex) | Q(content__iregex=word_regex)
            geoentertainment_items = News.objects.filter(query, date_added=news_date,
                                                         category__name='Geo Entertainment')
            expressentertainment_items = News.objects.filter(query, date_added=news_date, category__name='Express '
                                                                                                         'Entertainment')
            dawnpakistanentertainment_items = News.objects.filter(query, date_added=news_date, category__name='Dawn'
                                                                                                              'Pakistan Entertainment')
        else:
            # If no search query is provided, retrieve all news items for the specified date and category
            geoentertainment_items = News.objects.filter(date_added=news_date, category__name='Geo Entertainment')
            expressentertainment_items = News.objects.filter(date_added=news_date, category__name='Express '
                                                                                                  'Entertainment')
            dawnpakistanentertainment_items = News.objects.filter(date_added=news_date, category__name='Dawn Pakistan '
                                                                                                       'Entertainment')

        combined_items = list(geoentertainment_items) + list(expressentertainment_items) + list(
            dawnpakistanentertainment_items)
        random.shuffle(combined_items)

        paginator = Paginator(combined_items, self.paginate_by)
        page_number = self.request.GET.get('page', 1)
        items = paginator.get_page(page_number)

        context['items'] = items
        return context


class BusinessPage(TemplateView):
    template_name = "fyp/Business.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_query_1 = self.request.GET.get('q_1')
        date_str = self.request.GET.get('date')

        if date_str:
            news_date = date.fromisoformat(date_str)
        else:
            news_date = date.today()

        if search_query_1:
            # Split the search query into individual words
            words = search_query_1.split()

            # Initialize an empty Q object for the query
            query = Q()

            # Perform search using OR operator for individual words
            for word in words:
                # Use regex to match whole words only
                word_regex = r'\b{}\b'.format(re.escape(word))
                query |= Q(title__iregex=word_regex) | Q(content__iregex=word_regex)
            geobusiness_items = News.objects.filter(query, date_added=news_date, category__name='Geo Business')
            expressbusiness_items = News.objects.filter(query, date_added=news_date, category__name='Express Business')
            dawnbusiness_items = News.objects.filter(query, date_added=news_date, category__name='Dawn Business')
        else:
            # If no search query is provided, retrieve all news items for the specified date and category
            geobusiness_items = News.objects.filter(date_added=news_date, category__name='Geo Business')
            expressbusiness_items = News.objects.filter(date_added=news_date, category__name='Express Business')
            dawnbusiness_items = News.objects.filter(date_added=news_date, category__name='Dawn Business')

        combined_items = list(geobusiness_items) + list(expressbusiness_items) + list(dawnbusiness_items)
        random.shuffle(combined_items)

        paginator = Paginator(combined_items, self.paginate_by)
        page_number = self.request.GET.get('page', 1)
        items = paginator.get_page(page_number)

        context['items'] = items
        return context


class WorldPage(TemplateView):
    template_name = "fyp/World.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_query_1 = self.request.GET.get('q_1')
        date_str = self.request.GET.get('date')

        if date_str:
            news_date = date.fromisoformat(date_str)
        else:
            news_date = date.today()

        if search_query_1:
            # Split the search query into individual words
            words = search_query_1.split()

            # Initialize an empty Q object for the query
            query = Q()

            # Perform search using OR operator for individual words
            for word in words:
                # Use regex to match whole words only
                word_regex = r'\b{}\b'.format(re.escape(word))
                query |= Q(title__iregex=word_regex) | Q(content__iregex=word_regex)
            geoworld_items = News.objects.filter(query, date_added=news_date, category__name='Geo World')
            expressworld_items = News.objects.filter(query, date_added=news_date, category__name='Express World')
            dawnworld_items = News.objects.filter(query, date_added=news_date, category__name='Dawn World')
        else:
            # If no search query is provided, retrieve all news items for the specified date and category
            geoworld_items = News.objects.filter(date_added=news_date, category__name='Geo World')
            expressworld_items = News.objects.filter(date_added=news_date, category__name='Express World')
            dawnworld_items = News.objects.filter(date_added=news_date, category__name='Dawn World')

        combined_items = list(geoworld_items) + list(expressworld_items) + list(dawnworld_items)
        random.shuffle(combined_items)

        paginator = Paginator(combined_items, self.paginate_by)
        page_number = self.request.GET.get('page', 1)
        items = paginator.get_page(page_number)

        context['items'] = items
        return context


class PakistanPage(TemplateView):
    template_name = 'fyp/Pakistan.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_query_1 = self.request.GET.get('q_1')
        date_str = self.request.GET.get('date')

        if date_str:
            news_date = date.fromisoformat(date_str)
        else:
            news_date = date.today()

        if search_query_1:
            # Split the search query into individual words
            words = search_query_1.split()

            # Initialize an empty Q object for the query
            query = Q()

            # Perform search using OR operator for individual words
            for word in words:
                # Use regex to match whole words only
                word_regex = r'\b{}\b'.format(re.escape(word))
                query |= Q(title__iregex=word_regex) | Q(content__iregex=word_regex)
            geopakistan_items = News.objects.filter(query, date_added=news_date, category__name='Geo Pakistan')
            expresspakistan_items = News.objects.filter(query, date_added=news_date, category__name='Express Pakistan')
            dawnpakistan_items = News.objects.filter(query, date_added=news_date, category__name='Dawn Pakistan')
        else:
            # If no search query is provided, retrieve all news items for the specified date and category
            geopakistan_items = News.objects.filter(date_added=news_date, category__name='Geo Pakistan')
            expresspakistan_items = News.objects.filter(date_added=news_date, category__name='Express Pakistan')
            dawnpakistan_items = News.objects.filter(date_added=news_date, category__name='Dawn Pakistan')

        combined_items = list(dawnpakistan_items) + list(geopakistan_items) + list(expresspakistan_items)
        random.shuffle(combined_items)

        paginator = Paginator(combined_items, self.paginate_by)
        page_number = self.request.GET.get('page', 1)
        items = paginator.get_page(page_number)

        context['items'] = items
        return context


class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')


class SignupView(CreateView):
    form_class = SignupForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')


class PasswordChange(PasswordChangeView):
    template_name = 'registration/password_change.html'  # Replace with your desired template path
    success_url = 'password_change_done'  # Replace with your desired URL path for successful password change


class PasswordChangeDone(PasswordChangeDoneView):
    template_name = 'registration/password_change_done.html'


class MyPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset_form.html'
    success_url = reverse_lazy('password_reset_done')
    email_template_name = 'registration/password_reset_email.html'


class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'


class MyPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')


class MyPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete.html'


# def crawl_news(request): # Execute the 'scrapy crawl GeoNews' command run(['scrapy', 'crawl', 'GeoNews'],
# cwd='C:/Users/Fahad Mehdi/Django Projects/Myfyp/News aggregator/scrapy_quotes/scrapy_quotes') return HttpResponse(
# 'News crawling initiated')


def execute_scrapy_command(request):
    subprocess.run(["scrapy", "crawl", "GeoNews"],
                   cwd='C:/Users/Fahad Mehdi/Django Projects/Myfyp/News aggregator/scrapy_quotes/scrapy_quotes')
    return redirect('fyp:MainPage')


class HistoryListView(ListView):
    model = History
    template_name = 'fyp/History.html'
    context_object_name = 'history_items'
    ordering = ['-timestamp']  # Optional: specify the ordering of history items

    def get_queryset(self):
        # Optional: customize the queryset if needed
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        # if self.request.user.is_authenticated:
        #     history_items = History.objects.filter(user=self.request.user)
        # else:
        #     history_items = []
        return queryset

    def post(self, request, *args, **kwargs):
        if 'delete' in request.POST:
            history_id = request.POST['delete']
            history_item = get_object_or_404(History, id=history_id, user=self.request.user)
            history_item.delete()
            return redirect('fyp:history_list')

        return super().post(request, *args, **kwargs)


class ArchivedHistoryView(ListView):
    model = ArchivedItem
    template_name = 'archived.html'
    context_object_name = 'history_items'
