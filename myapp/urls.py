from django.urls import path
from .views import home, home_detail, portfolio, test, root_page, learning_context, using_bootstrap
urlpatterns=[
    path("home/<int:id>/detail/", home_detail, name="home_details"),
    path("test/", test, name="test"),
    path("portfolio/", portfolio, name="portfolio"),
    path("learning-context/", learning_context, name="learning_context"),
    path("using_bootstrap/", using_bootstrap, name="using_bootstrap"),
    path("", root_page, name="root_page"),
    path("", home),
]
