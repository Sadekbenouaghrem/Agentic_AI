
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from agents.schema import schema
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.http import HttpResponse

def accueil(request):
    return HttpResponse("<h1>Bienvenue sur Agent AI</h1><p>Accédez à <a href='/graphql/'>GraphQL ici</a>.</p>")

urlpatterns = [
     path('', accueil),
    path('admin/', admin.site.urls),
    path('api/', include('agents.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
     path('', include('agents.urls')),
     path("graphql/",csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),

]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('agents.urls')),  # <-- Ajoute cette ligne
]
