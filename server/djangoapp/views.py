from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from .models import CarMake, CarModel
from .restapis import get_request_dealers, get_request_reviews, get_request_sentiments, post_request
from .restapis import get_dealers_from_cf, get_dealer_by_id_from_cf, get_dealer_by_state_from_cf, get_dealer_reviews_from_cf 
from .restapis import get_dealers_from_cf2, get_dealer_reviews_from_cf2
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.

# Create an `about` view to render a static about page
def about(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/about.html', context)  

# Create a `contact` view to return a static contact page
def contact(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/contact.html', context)  

# Create a `login_request` view to handle sign in request
def login_request(request):
    context = {}
    # Handles POST request
    if request.method == "POST":
        # Get username and password from request.POST dictionary
        username = request.POST['username']
        password = request.POST['psw']
        # Try to check if provided credentials can be authenticated
        user = authenticate(username=username, password=password)
        if user is not None:
            # If user is valid, call login method to login current user
            login(request, user)
            return redirect('djangoapp:index')
        else:
            # If not, return to login page again
            context['message'] = "Invalid username or password."
            return render(request, 'djangoapp/login.html', context)
    else:
        return render(request, 'djangoapp/login.html', context)



# Create a `logout_request` view to handle sign out request
def logout_request(request):
    # Get the user object based on session id in request
    print("Log out the user `{}`".format(request.user.username))
    # Logout user in the request
    logout(request)
    # Redirect user back to course list view
    return redirect('djangoapp:registration')


# Create a `registration_request` view to handle sign up request
def registration_request(request):
    context = {}
    # If it is a GET request, just render the registration page
    if request.method == 'GET':
        return render(request, 'djangoapp/registration.html', context)
    # If it is a POST request
    elif request.method == 'POST':
        # Get user information from request.POST
        username = request.POST['username']
        password = request.POST['psw']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        user_exist = False
        try:
            # Check if user already exists
            User.objects.get(username=username)
            user_exist = True
        except:
            # If not, simply log this is a new user
            logger.debug("{} is new user".format(username))
        # If it is a new user
        if not user_exist:
            # Create user in auth_user table
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                            password=password)
            # Login the user and redirect to dealer list page (Home page)
            login(request, user)
            return redirect("djangoapp:index")
        else:
            context['message'] = "User already exists."
            return render(request, 'djangoapp/registration.html', context)

# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):    
    if request.method == "GET":        
    #    url = "your-cloud-function-domain/dealerships/dealer-get"
        url = "https://service.eu.apiconnect.ibmcloud.com/gws/apigateway/api/82537bc72633db84be982fd56a9a90b1879ec76dd6a0550dd12d8e3ec73e3cca/dealerships/get-dealerships-seq"
        # Get dealers from the URL
        dealerships = get_dealers_from_cf(url)
        
        # Concat all dealer's short name
        dealer_names = ',   '.join([dealer.short_name for dealer in dealerships])
        # Return a list of dealer short name
        return HttpResponse(dealer_names)

# for dealers in tabular form        
def get_dealerships2(request):
    context = {}
    dealership_list = []
    if request.method == "GET":        
    #    url = "your-cloud-function-domain/dealerships/dealer-get"
        url = "https://service.eu.apiconnect.ibmcloud.com/gws/apigateway/api/82537bc72633db84be982fd56a9a90b1879ec76dd6a0550dd12d8e3ec73e3cca/dealerships/get-dealerships-seq"
        # Get dealers from the URL
        dealers_list = get_dealers_from_cf2(url) 
        context["dealers_dict_list"] = dealers_list    
    #    context = dealers_dict3
        # SUCCESSFUL : 2-LINES BELOW - Trial for creating and sending data through context
        # data_dict = [{'title1':'python', 'title2':'django'}, {'title1':'java', 'title2':'js'}]
        # context["dataset"] = data_dict

        # Concat all dealer's short name
    #    dealer_names = ',   '.join([dealer.short_name for dealer in dealerships])
        # Return a list of dealer short name
        # return HttpResponse(dealer_names)
        return render(request, 'djangoapp/index.html', context)

# Create a `get_dealer_details` view to render the reviews of a dealer
#def get_dealer_details(request):
def get_dealer_details(request, dealer_id):
#    context = []
    if request.method == "GET":
    #    url = "your-cloud-function-domain/dealerships/dealer-get"
        url = "https://service.eu.apiconnect.ibmcloud.com/gws/apigateway/api/82537bc72633db84be982fd56a9a90b1879ec76dd6a0550dd12d8e3ec73e3cca/review-get/get-reviews-seq"
        # Get dealers from the URL
        review_objects = get_dealer_reviews_from_cf(url, dealer_id)
        # Concat all dealer's short name
    #    dealer_reviews = context.append(review_objects)
        dealer_reviews = '<br><br>'.join([rev_obj.review for rev_obj in review_objects])
    #    dealer_reviews = '<br><br>'.join([(rev_obj.review + " - " + rev_obj.sentiment) for rev_obj in review_objects])
        
        # Return a list of dealer reviews
        return HttpResponse(dealer_reviews)

# Another view to return a list of reviews for a specific dealer
def get_dealer_details2(request, dealer_id):
    context = {}
    if request.method == "GET":
    #    url = "your-cloud-function-domain/dealerships/dealer-get"
        url = "https://service.eu.apiconnect.ibmcloud.com/gws/apigateway/api/82537bc72633db84be982fd56a9a90b1879ec76dd6a0550dd12d8e3ec73e3cca/review-get/get-reviews-seq"
        # Get dealers from the URL (List of dict objects)
        # This list of reviews has dealer_id as the first item
        dealer_review_details_list  = get_dealer_reviews_from_cf2(url, dealer_id)
        context["reviews_list"] = dealer_review_details_list
    if dealer_id % 2 == 0:
        return render(request, 'djangoapp/dealer_details.html', context)
    else:
        return render(request, 'djangoapp/dealer_details2.html', context)


# Create a `add_review` view to submit a review
def add_review(request, dealer_id):
    # First check if user is authenticated because only authenticated users can post reviews for a dealer.
    if request.user.is_authenticated:
        
        review = {}
        review['id'] = 5
        review['name'] = 'Ram Sahare'
        review['dealership'] = 11
        review['review'] = "This is a great car dealer"
        review['purchase'] = "yes"
        review['another'] = "field"
        review['purchase_date'] = '2018-05-05'
        review['car_make'] = 'Rolls Royce'
        review['car_model'] = 'Beauty'
        review['car_year'] = '2018'
        review["time"] = datetime.utcnow().isoformat()
        
        if request.method == "POST":
            id = request.POST['id']
            name = request.POST['name']
            dealership = request.POST['dealership']
            review = request.POST['review']
            purchase = request.POST['purchase']
            another = request.POST['another']
            purchase_date = request.POST['purchase_date']
            car_make = request.POST['car_make']
            car_model = request.POST['car_model']
            car_year = request.POST['car_year']
            time = datetime.utcnow().isoformat()
        #    time = request.POST['id']
            

            url = "https://service.eu.apiconnect.ibmcloud.com/gws/apigateway/api/82537bc72633db84be982fd56a9a90b1879ec76dd6a0550dd12d8e3ec73e3cca/review-save/save-review-seq"
            json_payload["review"] = review
            result = post_request(url, json_payload, dealerId=dealer_id)
    
    # return HttpResponse(result)
    return redirect("djangoapp:dealer_details2", dealer_id=dealer_id)



