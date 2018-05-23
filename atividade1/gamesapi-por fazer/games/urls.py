"""
Book: Building RESTful Python Web Services
Chapter 2: Working with class based views and hyperlinked APIs in Django
Author: Gaston C. Hillar - Twitter.com/gastonhillar
Publisher: Packt Publishing Ltd. - http://www.packtpub.com
"""
from django.urls import path
from rest_framework.routers import DefaultRouter
from games.views import Games, GameCategories, Scores, Players


router = DefaultRouter()
router.register(r'games',Games)
router.register(r'game-categories',GameCategories)
router.register(r'players',Players)
router.register(r'scores',Scores)

urlpatterns = router.urls
