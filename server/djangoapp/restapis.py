import requests
import json
# import related models here
from .models import CarDealer
from requests.auth import HTTPBasicAuth
# Create a `get_request` to make HTTP GET requests
# e.g., response = requests.get(url, params=params, headers={'Content-Type': 'application/json'},
#                                     auth=HTTPBasicAuth('apikey', api_key))
def get_request(url, **kwargs):
    print(kwargs)
    print("GET from {} ".format(url))
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(url, headers={'Content-Type': 'application/json'}, params=kwargs)
    except:
        # If any error occurs
        print("Network exception occurred")
    status_code = response.status_code
    print("With status {} ".format(status_code))
    json_data = json.loads(response.text)
    return json_data
  #  return json_data.dealerships  - not working
  #  return json_data["dealerships"]  - not working

# Create a `post_request` to make HTTP POST requests
# e.g., response = requests.post(url, params=kwargs, json=payload)


# Create a get_dealers_from_cf method to get dealers from a cloud function
# def get_dealers_from_cf(url, **kwargs):
# - Call get_request() with specified arguments
# - Parse JSON results into a CarDealer object list
def get_dealers_from_cf(url, **kwargs):
    results = []
    # Call get_request with a URL parameter
    json_result = get_request(url)   
    if json_result:
        # Get the row list in JSON as dealers
        dealers = json_result["rows"][0]["doc"]["dealerships"]
        # For each dealer object
        for dealer in dealers:
            # Get its content in `doc` object
            dealer_doc = dealer           
        #    dealer_doc = dealer["doc"]            
            # Create a CarDealer object with values in `doc` object
        #    dealer_obj = CarDealer(id=dealer_doc.get("id"), city=dealer_doc.get("city"),
        #        state=dealer_doc.get("state"), st=dealer_doc.get("st"), 
        #        address=dealer_doc.get("address"), zip=dealer_doc.get("zip"), 
        #        lat=dealer_doc.get("lat"), long=dealer_doc.get("long"),
        #        short_name=dealer_doc.get("short_name"), full_name=dealer_doc.get("full_name")) 
            
            
            dealer_obj = CarDealer( id=dealer_doc["id"], city=dealer_doc["city"],
                state=dealer_doc["state"], st=dealer_doc["st"], 
                address=dealer_doc["address"], zip=dealer_doc["zip"], 
                lat=dealer_doc["lat"], long=dealer_doc["long"],
                short_name=dealer_doc["short_name"], 
                full_name=dealer_doc["full_name"] 
            )    
            results.append(dealer_obj)
    
    return results

# def get_dealer_by_id_from_cf(url, dealerId):
# - Call get_request() with specified arguments
# - Parse JSON results into a DealerView object list
def get_dealer_by_id_from_cf(url, dealerId):
    results = []
    # Call get_request with a URL parameter
    json_result = get_request(url, dealerId=dealerId)   
    if json_result:
        # Get the row list in JSON as dealers
        dealers = json_result["rows"]
        # For each dealer object
        for dealer in dealers:
            # Get its content in `doc` object           
            dealer_doc = dealer["doc"]            
            # Create a CarDealer object with values in `doc` object
        #    dealer_obj = CarDealer(id=dealer_doc.get("id"), city=dealer_doc.get("city"),
        #        state=dealer_doc.get("state"), st=dealer_doc.get("st"), 
        #        address=dealer_doc.get("address"), zip=dealer_doc.get("zip"), 
        #        lat=dealer_doc.get("lat"), long=dealer_doc.get("long"),
        #        short_name=dealer_doc.get("short_name"), full_name=dealer_doc.get("full_name")) 
            
            
            dealer_obj = CarDealer( id=dealer_doc["id"], city=dealer_doc["city"],
                state=dealer_doc["state"], st=dealer_doc["st"], 
                address=dealer_doc["address"], zip=dealer_doc["zip"], 
                lat=dealer_doc["lat"], long=dealer_doc["long"],
                short_name=dealer_doc["short_name"], 
                full_name=dealer_doc["full_name"] 
            )    
            results.append(dealer_obj)
    
    return results
        

# def get_dealer_by_state_from_cf(url, state):
# - Call get_request() with specified arguments
# - Parse JSON results into a DealerView object list
def get_dealer_by_state_from_cf(url, state):
    results = []
    # Call get_request with a URL parameter
    json_result = get_request(url, state=state)   
    if json_result:
        # Get the row list in JSON as dealers
        dealers = json_result["rows"]
        # For each dealer object
        for dealer in dealers:
            # Get its content in `doc` object           
            dealer_doc = dealer["doc"]            
            # Create a CarDealer object with values in `doc` object
        #    dealer_obj = CarDealer(id=dealer_doc.get("id"), city=dealer_doc.get("city"),
        #        state=dealer_doc.get("state"), st=dealer_doc.get("st"), 
        #        address=dealer_doc.get("address"), zip=dealer_doc.get("zip"), 
        #        lat=dealer_doc.get("lat"), long=dealer_doc.get("long"),
        #        short_name=dealer_doc.get("short_name"), full_name=dealer_doc.get("full_name")) 
            
            
            dealer_obj = CarDealer( id=dealer_doc["id"], city=dealer_doc["city"],
                state=dealer_doc["state"], st=dealer_doc["st"], 
                address=dealer_doc["address"], zip=dealer_doc["zip"], 
                lat=dealer_doc["lat"], long=dealer_doc["long"],
                short_name=dealer_doc["short_name"], 
                full_name=dealer_doc["full_name"] 
            )    
            results.append(dealer_obj)
    
    return results

# Create a get_dealer_reviews_from_cf method to get reviews by dealer id from a cloud function
def get_dealer_reviews_from_cf(url, **kwargs):
    results = []
    # Call get_request with a URL parameter
    json_result = get_request(url, dealerId=dealer_id)   
    if json_result:
        # Get the row list in JSON as dealers
        reviews_details = json_result["doc"]["reviews"]
        # For each dealer object
        for re-view in reviews_details:
            # Get its content in `doc` object           
        #    dealer_doc = dealer["doc"]            
                       
            review_obj = DealerReview( dealership=re-view["dealership"], name=re-view["name"],
                purchase=re-view["purchase"], review=re-view["review"], 
                purchase_date=re-view["purchase_date"], car_make=re-view["car_make"], 
                car_model=re-view["car_model"], car_year=re-view["car_year"],
                sentiment=re-view["sentiment"], id=re-view["id"] 
            )    
            results.append(dealer_obj)
    
    return results




# Create an `analyze_review_sentiments` method to call Watson NLU and analyze text
# def analyze_review_sentiments(text):
# - Call get_request() with specified arguments
# - Get the returned sentiment label such as Positive or Negative



