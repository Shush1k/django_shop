from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from coupons.models import Coupon


class CouponTestCase(TestCase):
    def setUp(self) -> None:
        Coupon.objects.create(code="DFX",
                              valid_from=timezone.now(),
                              valid_to=timezone.now() + timezone.timedelta(days=1),
                              discount=100,
                              active=True)

    def test_single_coupon(self):
        coupon_count = Coupon.objects.count()
        self.assertEqual(coupon_count, 1)

    def test_discount_range(self):
        coupon = Coupon.objects.get(code="DFX")
        self.assertGreaterEqual(coupon.discount, 0)
        self.assertLessEqual(coupon.discount, 100)

    def test_valid_time_duration(self):
        coupon = Coupon.objects.get(code="DFX")
        self.assertLessEqual(coupon.valid_from, timezone.now())
        self.assertGreaterEqual(coupon.valid_to, timezone.now())

    def test_coupon_apply_view(self):
        coupon = Coupon.objects.get(code="DFX")
        response_get = self.client.get(reverse('coupons:apply'))
        response_post = self.client.post(reverse('coupons:apply'), {"code": coupon.code})

        self.assertEqual(response_get.status_code, 405)
        self.assertEqual(response_post.status_code, 302)



