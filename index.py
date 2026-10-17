#Topic - Rest API
import requests

# ⭐ Lesson: REST API design

# ⭐topic : JSON response validation

# Ab hum seekhenge ki API se response milne ke baad kaise check karein ki data expected format mein hai ya nahi.

# Tumne pehle isinstance(data, list) use kiya tha. Ab usi concept ko thoda aur practical banate hain.

# Concept 1 — Status code 200 ka matlab data correct hona nahi hai

# Maan lo API 200 OK return karti hai, lekin tumhara program ek list expect kar raha hai aur response mein dictionary milti hai.
# Expected response:
# [
#   {"id": 1, "title": "Learn REST API"}
# ]

# Unexpected response:
# {
#   "message": "No data available"
# }
# Rule: HTTP success aur application-level data validation do alag checks hain.

# Concept 2 — Response ka type aur required fields validate karna

# Example: humein ek post ka response chahiye, jisme id aur title hone chahiye.
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()

    data = response.json()

    if isinstance(data, dict):
        if "id" in data and "title" in data:
            print("Post ID:", data["id"])
            print("Post title:", data["title"])
        else:
            print("Required fields are missing")
    else:
        print("Unexpected response format")

except requests.exceptions.Timeout:
    print("Request timed out.")

except requests.exceptions.HTTPError as error:
    print("HTTP error:", error)

except requests.exceptions.RequestException as error:
    print("Request failed:", error)


# Samjho:
# - isinstance(data, dict) check karta hai ki response Python dictionary hai.
# - "id" in data check karta hai ki dictionary mein id key hai.
# - "title" in data check karta hai ki title key hai.
# - raise_for_status() HTTP 4xx/5xx errors ko raise karta hai.
# Ye basic validation hai. Real applications mein fields ke data types aur values bhi validate karte hain.

# Concept 3 — Agar response valid JSON hi nahi hai?

# response.json() assume karta hai ki response body JSON mein parse ho sakti hai. Lekin server kabhi HTML error page ya malformed JSON bhi return kar sakta hai.

# Aise case mein JSON decoding error aa sakta hai. Tumhare existing RequestException handler mein Requests ka JSON decoding error bhi catch ho sakta hai, lekin clearer error handling ke liye use separately handle kar sakte hain.

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()

    data = response.json()

except requests.exceptions.JSONDecodeError:
    print("The server returned invalid JSON.")

except requests.exceptions.RequestException as error:
    print("Request failed:", error)

    # Yahan specific JSON error ko general request error se pehle rakha hai. Dhyan rahe, invalid JSON response ko retry karna automatically correct decision nahi hai—pehle API ka behaviour samajhna chahiye.

import requests
try:
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=5)
    response.raise_for_status()
    data = response.json()
    if isinstance(data, dict):
        if "id" in data and "title" in data:
            print("Post ID:", data["id"])
            print("Post title:", data["title"])
        else:
            print("Required fields are missing")
    else:
        print("Unexpected response format")

except requests.exceptions.Timeout:
    print("Request timed out.")
except requests.exceptions.HTTPError as error:
    print("HTTP error:", error)
except requests.exceptions.JSONDecodeError:
    print("The server returned invalid JSON.")
except requests.exceptions.ConnectionError:
    print("Could not connect to the server")
except requests.exceptions.RequestException as error:
    print("Request failed:", error)

# “I validate API responses beyond the HTTP status code by checking the expected data structure and required fields before accessing them. I also handle request failures and invalid JSON responses.”

 # ⭐ Topic: REST API design and HTTP methods revision

# Method |	Endpoint	 |	Purpose
# GET	 |	/meetings |		Sabhi meetings retrieve karna
# GET |		/meetings/101 |		Meeting 101 retrieve karna
# POST |		/meetings |		Nayi meeting create karna
# PUT |		/meetings/101 |		Meeting 101 ko replace/update karna
# PATCH |		/meetings/101 |		Meeting 101 ke selected fields update karna
# DELETE |		/meetings/101 |		Meeting 101 delete karna


# PUT vs PATCH
# Suppose meeting 101 mein ye data hai:
# {
#   "title": "Project Review",
#   "owner": "Aman",
#   "status": "scheduled"
# }

# Agar sirf status ko "completed" karna hai:
# - PATCH: Sirf status field update karne ke liye use hota hai.
# - PUT: Generally resource ki complete representation replace karne ke liye use hota hai.

# Exact behaviour API contract par depend karta hai. PUT ko idempotent design kiya jata hai, jabki PATCH operation idempotent bhi ho sakta hai ya nahi bhi—ye update operation par depend karta hai.

# Combined Python REST API practice
import requests
try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts", 
        params={"userId":1},
        timeout=5
    )
    response.raise_for_status()
    data = response.json()
    if isinstance(data, list):
        if not data:
            print("No posts found for this user.")
        else:
            print("Total post: ", len(data))
            
            if isinstance(data[0], dict) and "title" in data[0]:
                print("Title of the first post:", data[0]["title"])
            else:
                print("No title found for this post")
    else:
        print("Unexpected response format")


except requests.exceptions.Timeout:
    print("Request timed out.")
except requests.exceptions.HTTPError as error:
    print("HTTP error: ", error)
except requests.exceptions.JSONDecodeError:
    print("The server returned invalid JSON.")
except requests.exceptions.ConnectionError:
    print("Could not connect to the server")
except requests.exceptions.RequestException as error:
    print("Request failed: ", error)

# Interview-ready
# I use query parameters to filter API resources, validate response structures before accessing data, and handle HTTP errors, timeouts, and connection failures using appropriate exception handling.