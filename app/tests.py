from django.test import TestCase

from django.http import response
from django.test import SimpleTestCase

class Logic_2(SimpleTestCase):
    def test_2_3_2(self):
        response = self.client.get("/logic-2/lone-sum/2/3/2")
        self.assertContains(response, 3)

    def test_3_3_3(self):
        response = self.client.get("/logic-2/lone-sum/3/3/3")
        self.assertContains(response, 0)
    
    def test_1_2_3(self):
        response = self.client.get("/logic-2/lone-sum/1/2/3")
        self.assertContains(response, 6)

class String_2(SimpleTestCase):
    def test_catty(self):
        response = self.client.get("/string-2/cat-dog/catty")
        self.assertContains(response, False)
    def test_bro(self):
        response = self.client.get("/string-2/cat-dog/bro")
        self.assertContains(response, True)
    def test_doggo(self):
        response = self.client.get("/string-2/cat-dog/doggo")
        self.assertContains(response, False)

class Warmup_2(SimpleTestCase):
    def test_boi(self):
        response = self.client.get("/warmup-2/string-splosion/boi")
        self.assertContains(response, "bboboi")
    def test_ethan(self):
        response = self.client.get("/warmup-2/string-splosion/ethan")
        self.assertContains(response, "eetethethaethan")
    def test_people(self):
        response = self.client.get("/warmup-2/string-splosion/people")
        self.assertContains(response, "ppepeopeoppeoplpeople")

class Warmup_1(SimpleTestCase):
    def test_87(self):
        response = self.client.get("/warmup-1/near-hundred/87")
        self.assertContains(response, False)
    def test_92(self):
        response = self.client.get("/warmup-1/near-hundred/92")
        self.assertContains(response, True)
    def test_110(self):
        response = self.client.get("/warmup-1/near-hundred/110")
        self.assertContains(response, True)

from django.test import SimpleTestCase


class TestHeyYou(SimpleTestCase):
    def test_hey_nate(self):
        response = self.client.get("/hey/nate")
        self.assertContains(response, "Hello, nate!")

    def test_hey_bcca(self):
        response = self.client.get("/hey/BCCA")
        self.assertContains(response, "Hello, BCCA!")


class TestAgeIn(SimpleTestCase):
    def test_age_in_2050_born_2000(self):
        response = self.client.get("/age-in/2050/2000")
        self.assertContains(response, "50")

    def test_age_in_2050_born_0(self):
        response = self.client.get("/age-in/2050/0")
        self.assertContains(response, "2050")

    def test_age_in_2010_born_1995(self):
        response = self.client.get("/age-in/2010/1995")
        self.assertContains(response, "15")

    def test_age_in_1950_born_1920(self):
        response = self.client.get("/age-in/1950/120")
        self.assertContains(response, "30")


class TestOrderTotal(SimpleTestCase):
    def test_order_total_0_0_0(self):
        response = self.client.get("/order-total/0/0/0")
        self.assertContains(response, "0.0")

    def test_order_total_1_1_1(self):
        response = self.client.get("/order-total/1/1/1")
        self.assertContains(response, "7.0")

    def test_order_total_2_3_4(self):
        response = self.client.get("/order-total/2/3/4")
        self.assertContains(response, "17.5")

    def test_order_total_4_3_2(self):
        response = self.client.get("/order-total/4/3/2")
        self.assertContains(response, "24.5")