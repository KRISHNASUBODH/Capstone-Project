from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL

    # path for about view
    path('about/', views.about, name='about'),
    
    # path for contact us view
    path('contact/', views.contact, name='contact'),
    
    # path for registration
    path('registration/', views.registration_request, name='registration'),

    # path for login
    path('login/', views.login_request, name='login'),

    # path for logout
    path('logout/', views.logout_request, name='logout'),
    
    # path for dealerships not as a table
 #   path(route='', view=views.get_dealerships, name='index'),
  
    # path for dealerships in tabular form - later converted to index page in 2nd line
 #   path(route='dealertable/', view=views.get_dealerships2, name='dealertable'),
    path(route='', view=views.get_dealerships2, name='index'),
    # path for all-dealers reviews view - working ok
    #path(route='dealer_reviews/', view=views.get_dealer_details, name='dealer_reviews'),
    
    # path for a selected (id) dealer review view
    path('dealer/<int:dealer_id>/', views.get_dealer_details, name='dealer_details'),

    # path for a selected (id) dealer review view - displayed as bootstrap cards
    path('dealer2/<int:dealer_id>/', views.get_dealer_details2, name='dealer_details2'),

    # path for add a review view
    path('dealer3/<int:dealer_id>/', views.add_review, name='add_review'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)