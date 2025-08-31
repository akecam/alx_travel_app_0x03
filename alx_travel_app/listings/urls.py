from django.urls import path, include
from django.http import JsonResponse
from rest_framework.routers import DefaultRouter
from .views import BookingViewSet, ListingViewSet


router = DefaultRouter()
router.register(r'listing', ListingViewSet)
router.register(r'booking', BookingViewSet)


# Sample view for testing
def test_view(request):
    return JsonResponse({'message': 'Listings API is working!'})

urlpatterns = [
    # path('', test_view),  # Accessible at /api/
    path('api/', include(router.urls)),
]

