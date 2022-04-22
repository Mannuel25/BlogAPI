from django.urls import path
from .views import UserViewset, PostViewset
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('users', UserViewset, base_name='users')
router.register('', PostViewset, base_name='posts')

urlpatterns = router.urls
