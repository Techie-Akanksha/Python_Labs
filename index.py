#Topic - Rest API
import requests

# ⭐ Authentication + Headers
# Body = actual data
# Headers = data ke baare mein information aur request ki additional details

# Interview-ready
# Question: What is the difference between request headers and the request body?

# Answer:
# "The request body contains the actual data sent to the server, while request headers provide metadata about the request, such as the content type, accepted response format, and authentication information."


# ⭐ Common Headers
# 1. Content-Type
# Tum already jaanti ho.
# Content-Type: application/json

# Meaning
# "My request body JSON format mein hai."

# 2. Accept
# Accept: application/json

# Meaning
# "Mujhe response JSON format mein chahiye."

# Python mein Headers
headers = {
    "Authorization": "Bearer my_secret_token",
    "Accept": "application/json"
}
url = "https://api.example.com/data"
response = requests.get(url, headers=headers)

# ⭐ Authentication
# — server ko kaise pata chalega ki request kiski hai?

# Authentication ka matlab hai client ki identity verify karna. Authorization alag concept hai: verified client ko kis resource ka access allowed hai.


# Client
# Request bhejta hai, credentials ya token ke saath.

# Server
# Identity/token verify karta hai, phir permissions check kar sakta hai.

# Response
# Allowed ho toh result; otherwise appropriate error response.

# Common authentication methods
# - API key: Request ke saath secret key bheji jaati hai.
# - Bearer token: Authorization header mein token bheja jata hai.
# - Session/cookie: Server-managed login session ko identify karne ke liye use ho sakta hai.

# import requests

# url = "https://api.example.com/meetings"

# headers = {
#     "Authorization": "Bearer YOUR_ACCESS_TOKEN"
# }

# response = requests.get(
#     url,
#     headers=headers,
#     timeout=5
# )

# response.raise_for_status()
# print(response.status_code)

# Interview answer: “Authentication verifies the identity of a client, while authorization determines which resources or actions that client is permitted to access.”

#⭐ HTTP headers
#  — request ke saath extra information.Headers request ya response ke baare mein metadata carry karte hain.

# Teen important headers:
# Header	Purpose
# Content-Type	Request body kis format mein hai
# Accept	Client response mein kaunsa format prefer karta hai
# Authorization	Credentials/token bhejne ke liye

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    headers=headers,
    json={
        "title": "MeetMind AI",
        "body": "Meeting summary test",
        "userId": 1
    },
    timeout=5
)

response.raise_for_status()
print(response.status_code)
print(response.json())

# Yahan json= already Content-Type: application/json automatically set karta hai, isliye Content-Type manually dena usually unnecessary hai. Example ka purpose headers ka role samjhana hai.
# Yaad rakho:
# - json= → data bhejne ke liye.
# - headers= → request metadata aur authentication jaise details bhejne ke liye.
# - params= → URL query parameters ke liye.
# - timeout= → waiting ko limit karne ke liye.

# Interview answer: “HTTP headers carry metadata about a request or response. Content-Type describes the request body format, while Accept indicates the response formats the client can process.”


# ⭐Response validation
# Agar API request successful ho, toh kya iska matlab hai ki response data bhi correct hai?
# Nahi. HTTP 200 OK milne ke baad bhi response mein unexpected format, empty data, ya missing fields ho sakte hain. Isliye response ko validate karna important hai.


# Concept 1 — HTTP success vs data validation
# HTTP validation
# response.raise_for_status()
# Check karta hai ki response HTTP 4xx/5xx error toh nahi hai.

# Data validation
# response.json() aur Python checks
# Check karte hain ki data expected type aur structure mein hai ya nahi.

response.raise_for_status()
data = response.json()

if isinstance(data, list):
    print("Received a list")
else:
    print("Unexpected response format")

# Yahan isinstance(data, list) check karta hai ki data Python list hai ya nahi. Agar API list ke badle dictionary return kare, toh tum us difference ko detect kar sakte ho.

# Concept 2 — Empty response data handle karna
# Ek valid response mein empty list bhi ho sakti hai. Empty list zaroori nahi ki API failure ho.

if not data:
    print("No records found")
else:
    print("Records found:", len(data))

# Yeh code empty list [] aur other falsy values ke liye message print karega. Isliye pehle expected data type validate karna achha rahega, especially jab API ka response format fixed ho.

# Concept 3 — Status codes ko context mein samajhna
# Status	Meaning	Typical situation
# 200 OK	Request successful	Data retrieve kiya
# 201 Created	Resource creation report hui	POST se resource create hua
# 204 No Content	Request successful, response body nahi	DELETE ya another successful operation
# 400 Bad Request	Request invalid	Required input missing ya malformed
# 401 Unauthorized	Authentication required/invalid	Token missing ya invalid
# 403 Forbidden	Permission denied	User ko action allowed nahi
# 404 Not Found	Resource nahi mila	Meeting ID exist nahi karti
# 500 Internal Server Error	Server-side failure	Backend mein unexpected error


import requests
url = "https://jsonplaceholder.typicode.com/posts"
try:
    response = requests.get(
        url,
        params= {
            "userId" : 1
        },
        timeout = 5
    )
    response.raise_for_status()
    data = response.json()
    if isinstance(data, list):
        print("Received list")
        if not data:
            print("No posts found")
        else:
            print("Total Posts found: ", len(data))
            print("Post title: ",data[0]["title"])
    else:
        print("Unexpected response format")


except requests.exceptions.Timeout:
    print("The required timed out.")

except requests.exceptions.HTTPError as error:
    print("Http error occured: ", error)

except requests.exceptions.ConnectionError:
    print("Could not connect to the server ")
    
except requests.exceptions.RequestException as error:
    print("Request failed ", error)


# Interview-ready
# “I implemented a GET request with query parameters and timeout handling, validated the response type, handled empty results, and added exception handling for HTTP and connection-related failures.”

# “I implemented response validation to handle unexpected data types and empty results safely, and organized exception handlers from specific errors to the general request exception.”