import requests
import json
# import related models here
from .models import CarDealer, DealerReview
from requests.auth import HTTPBasicAuth
# Create a `get_request` to make HTTP GET requests
# e.g., response = requests.get(url, params=params, headers={'Content-Type': 'application/json'},
#                                     auth=HTTPBasicAuth('apikey', api_key))
# def get_request(url, **kwargs):
def get_request_dealers(url, **kwargs):
    print(kwargs)
    #print(dealer_id)
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

def get_request_reviews(url, **kwargs):
    print(kwargs)
    #print(dealer_id)
    print("GET from {} ".format(url))
    try:        
        response = requests.get(url, headers={'Content-Type': 'application/json'}, params=kwargs)
    except:
        # If any error occurs
        print("Network exception occurred")
    status_code = response.status_code
    print("With status {} ".format(status_code))
    json_data = json.loads(response.text)
    return json_data

def get_request_sentiments(url, **kwargs):
    print(kwargs)
    #print(dealer_id)
    print("GET from {} ".format(url))
    try:
        response = requests.get(url, params=params, headers={'Content-Type': 'application/json'}, auth=HTTPBasicAuth('apikey', api_key))        
    except:
        # If any error occurs
        print("Network exception occurred")
    
    status_code = response.status_code
    print("With status {} ".format(status_code))
    json_data = json.loads(response.text)
    return json_data


# Create a `post_request` to make HTTP POST requests
# e.g., response = requests.post(url, params=kwargs, json=payload)
def post_request(url, json_payload, **kwargs):
    print(kwargs)
    #print(dealer_id)
    print("POST from {} ".format(url))
    try:
        response = requests.post(url, params=kwargs, json=json_payload)        
    except:
        # If any error occurs
        print("Network exception occurred")
    
    status_code = response.status_code
    print("With status {} ".format(status_code))
    




# Create a get_dealers_from_cf method to get dealers from a cloud function
# def get_dealers_from_cf(url, **kwargs):
# - Call get_request() with specified arguments
# - Parse JSON results into a CarDealer object list
def get_dealers_from_cf(url, **kwargs):
    results = []
    # Call get_request with a URL parameter
    json_result = get_request_dealers(url)   
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

# method to get dealers in tabular form
def get_dealers_from_cf2(url, **kwargs):
    dealers_dict = {}
    # Call get_request with a URL parameter
    json_result = get_request_dealers(url)   
    if json_result:
        # Get the row list in JSON as dealers
     #   dealers = json_result["rows"][0]["doc"]["dealerships"]
        dealers = json_result["rows"][0]["doc"]
        dealers_dict = dealers            
    return dealers_dict




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
def get_dealer_reviews_from_cf(url, dealer_id):
#def get_dealer_reviews_from_cf(url, **kwargs):
    results = []
#    dealer_id = 1  -- use above method with dealer_by_id
    # Call get_request with a URL parameter
#    json_result = get_request(url)
    json_result = get_request_reviews(url, dealerId=dealer_id) 
   # json_result = get_request(dealer_id)   
    if json_result:
        # Get the row list in JSON as dealers
        reviews_details = json_result["rows"][0]["doc"]["reviews"]
        # For each dealer object
        for reviewed in reviews_details:
            # Get its content in `doc` object           
        #    dealer_doc = dealer["doc"]            
            if reviewed["id"] == dealer_id:           
                review_obj = DealerReview( dealership=reviewed["dealership"], name=reviewed["name"],
                    purchase=reviewed["purchase"], review=reviewed["review"], 
                    purchase_date=reviewed["purchase_date"], car_make=reviewed["car_make"], 
                    car_model=reviewed["car_model"], car_year=reviewed["car_year"],
                # sentiment="" is ok, giving review for any one dealer
                    sentiment="", 
                    id=reviewed["id"] 
                )
            # Adding sentiment - NOT WORKING - may BYPASS
            #    review_obj.sentiment = analyze_review_sentiments(review_obj.review)    
                results.append(review_obj)
    
    return results




# Create an `analyze_review_sentiments` method to call Watson NLU and analyze text
# - Call get_request() with specified arguments
# - Get the returned sentiment label such as Positive or Negative
def analyze_review_sentiments(text, **kwargs):
    params = dict()
    params["text"] = kwargs["text"]
    params["version"] = kwargs["version"]
    params["features"] = kwargs["features"]
    params["return_analyzed_text"] = kwargs["return_analyzed_text"]
    
    api_key = ""
    url = "https://api.eu-gb.natural-language-understanding.watson.cloud.ibm.com/instances/871f35fd-6629-4ee8-9c4f-b25283de3e68"
    
    json_result = get_request_sentiments(url, params=params, apikey=api_key)
    return json.loads(json_result)
#    response = requests.get(url, params=params, headers={'Content-Type': 'application/json'},
#                                    auth=HTTPBasicAuth('apikey', api_key))


