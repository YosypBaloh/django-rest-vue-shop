from rest_framework.routers import SimpleRouter
from .views import ItemsPage

router = SimpleRouter()
router.register('api/items', ItemsPage)

urlpatterns = []
urlpatterns += router.urls
