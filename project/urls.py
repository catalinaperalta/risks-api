from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from api import views

# Register the viewset routes for each model
router = routers.DefaultRouter()
router.register(r'insurers', views.InsurerViewSet)
router.register(r'risks', views.RiskViewSet)
router.register(r'riskfields', views.RiskFieldViewSet)

urlpatterns = [
	path('admin/', admin.site.urls),
	# Set all viewset subroutes as children of the /api/ path
    path('api/', include(router.urls))
]