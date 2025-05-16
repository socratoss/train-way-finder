from django.db import models
from django.utils.timezone import now

from cities.models import City


class Route(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Route name"
    )
    travel_time = models.PositiveSmallIntegerField(
        verbose_name="Total travel time",
    )
    from_city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name="route_from_city_set",
        verbose_name="From city"
    )
    to_city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name="route_to_city_set",
        verbose_name="To city"
    )
    trains = models.ManyToManyField(
        "trains.Train",
        verbose_name="Train list"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created at"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated at"
    )

    def __str__(self):
        return f"Route {self.name} from {self.from_city} to {self.to_city}"

    class Meta:
        verbose_name = "Route"
        verbose_name_plural = "Routes"
        ordering = ["travel_time"]
