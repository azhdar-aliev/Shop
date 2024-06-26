from django.conf import settings


class Cart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = request.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

