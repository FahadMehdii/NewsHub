from django.core.management.base import BaseCommand
from fyp.models import History, ArchivedItem
from django.utils import timezone


class Command(BaseCommand):
    help = 'Moves expired history items to the archived model'

    def handle(self, *args, **options):
        ten_minutes_ago = timezone.now() - timezone.timedelta(minutes=1)

        expired_history = History.objects.filter(timestamp__lt=ten_minutes_ago)

        for history_item in expired_history:
            history_item.archive()
            history_item.delete()
