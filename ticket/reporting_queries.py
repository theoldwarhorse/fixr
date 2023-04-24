from django.db.models import Sum
from models import Event, Order, Ticket
from datetime import datetime, timedelta, date


def percentage_of_cancelled_orders_per_event(event: Event):
    event_orders = Order.objects.filter(event=event)
    cancelled_event_orders = Order.objects.filter(event=event, cancelled=True)

    if event_orders == 0:
        return 0
    else:
        return 100 * cancelled_event_orders / event_orders


def date_with_the_most_cancelled_tickets():
    max_cancelled_date = (
        Order.objects.filter(cancelled=True)
        .annotate(cancelled_count=Sum("quantity"))
        .values("fulfilled_at__date")
        .order_by("-cancelled_count")
        .first()["fulfilled_at__date"]
    )

    return max_cancelled_date
