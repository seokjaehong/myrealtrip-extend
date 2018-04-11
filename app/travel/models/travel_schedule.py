from django.conf import settings
from django.db import models
from .product_base import ProductBase
from .travel_information import TravelInformation


class TravelSchedule(ProductBase):
    travel_info = models.ForeignKey(
        TravelInformation,
        on_delete=models.CASCADE,
        verbose_name='travel_info')
    start_date = models.DateField('여행시작날짜')
    end_date = models.DateField('여행끝날짜', blank=True,null=True)

    reserved_user = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='reservation.Reservation',
        related_name="reserve_travel",
        blank=True,
    )

    class Meta:
        ordering = ['-creation_datetime']

    def __str(self):
        return self.pk
