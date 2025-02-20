from django.test import TestCase
from datetime import datetime
from .models import Reservations




class ReservationModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.reservation = Reservations.objects.create(
            firstName = 'John',
            lastName = 'Arnle'
        )

    def test_fields(self):
        self.assertIsInstance(self.reservation.firstName, str)
        self.assertIsInstance(self.reservation.lastName, str)

    def test_timestamps(self):
        self.assertIsInstance(self.reservation.bookingTime,datetime)
