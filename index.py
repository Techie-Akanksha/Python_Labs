#Topic - Rest API
import requests

# ⭐ Lesson: REST API design

#⭐  1. Resource-based URLs

# REST APIs mein URLs ko generally resources ke around design kiya jata hai, jaise meetings, users, documents aur tasks.

# Endpoint	Purpose

# GET /meetings	Saari meetings retrieve karna
# GET /meetings/101	Meeting 101 retrieve karna
# POST /meetings	Nayi meeting create karna
# DELETE /meetings/101	Meeting 101 delete karna


# Notice karo: URL mein resource ka naam meetings hai, aur HTTP method batata hai ki us resource ke saath kya action karna hai.

# Less ideal design:
# GET /getMeeting?id=101

# More REST-style design:
# GET /meetings/101

# Dono designs technically kaam kar sakte hain, lekin second design resource-oriented API conventions ko follow karta hai.

# ⭐ 2. Statelessness  

# REST ka ek important principle hai statelessness.

# Simple meaning: har request mein server ke paas us request ko process karne ke liye required context hona chahiye. Server requests ke beech client ki conversational session state ko implicitly yaad rakhne par depend nahi karta.

# Example:
# - Request 1: GET /meetings/101
# - Request 2: GET /meetings/102

# Har request independently process honi chahiye. Agar authentication required hai, toh har request mein valid token bhejna pad sakta hai.

# Interview answer: “Statelessness means each request must contain the information needed to process it, without relying on stored client session context from a previous request.”


# ⭐ 1. REST principles answer review
# Question |	Your answer |	Reason
# Q1: Meeting 205 retrieve karna |	B — GET /meetings/205	|  Resource URL meeting identify karta hai; GET retrieval indicate karta hai.
# Q2: Stateless authentication |B — Har request mein required token	Server | ko har independent request authenticate karne ke liye required credentials milne chahiye.
# Q3: Same URL, different methods |	A — Yes	| GET /meetings list retrieve karta hai, jabki POST /meetings creation request karta hai.

# Ek nuance: statelessness ka matlab yeh nahi ki server kabhi data store nahi kar sakta. Server meetings aur users ka persistent data store kar sakta hai; principle client ki request/session context par implicitly depend na karne ka hai.


# ⭐ 2. Safe methods vs idempotent methods

# Safe method: Request ka intended effect server ke resource state ko change karna nahi hota.
# A safe HTTP method is a method that is intended to retrieve data without changing the server's state.
# Simple words mein: server se data lena, bina server ka data change karne ke.

# Idempotent method: Same request repeat karne se intended final resource state wahi rehti hai.
# An idempotent method is a method where making the same request multiple times has the same intended effect on the server as making it once.
# Simple words mein: same request 1 baar bhejo ya 10 baar, server ki final state same honi chahiye.

# Method	Safe?	Idempotent?
# GET	     Yes	Yes
# HEAD	     Yes	Yes
# PUT	      No	Yes
# DELETE	  No	Yes
# POST	      No	Not necessarily

# DELETE ka example: resource pehli request mein delete ho sakta hai. Repeat request par 404 aa sakta hai, lekin final state mein resource deleted hi rehta hai. Isliye DELETE idempotent hai, chahe response same na ho.

# 3. Retry behavior — request dobara kab bhejni chahiye?

# Maan lo MeetMind AI ek meeting summary generate karne ke liye backend ko request bhejta hai.

# Network timeout aa gaya. Ab tumhe nahi pata ki server ne request process ki thi ya nahi.

# GET request
# Generally retry karna safer hota hai, kyunki GET ka intended purpose data retrieve karna hai aur woh safe/idempotent hota hai.

# POST request
# Blind retry risky ho sakta hai. Agar pehli request process ho chuki thi, toh doosri request duplicate resource ya action create kar sakti hai.

# Production APIs mein retries carefully configure ki jaati hain. Payment ya resource creation jaise operations ke liye API-supported idempotency key duplicate processing ko prevent karne mein help kar sakti hai. Har POST retry unsafe nahi hota, lekin operation ki semantics samajhna zaroori hai.


import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

for attempt in range(2):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        print(response.json()["title"])
        break

    except requests.exceptions.Timeout:
        print("Request timed out.")

        if attempt == 1:
            print("Maximum attempts reached.")

# Is example mein maximum do attempts hain. Timeout ke baad hi loop next attempt karta hai. Dhyan rahe, yeh basic learning example hai; production retry logic mein backoff, retryable errors aur retry limits ko carefully handle karna chahiye.

# Interview answer: “I consider HTTP method semantics before retrying a failed request. GET requests are generally safe to retry, while POST retries may cause duplicate actions unless the API supports appropriate idempotency controls.”


# Q1. Repeating PUT /users/10 with the same address

# PUT is idempotent. Agar request baar-baar bhejo aur har baar address "Pune" set karo, final state same rahegi. Iska matlab ye nahi ki har response identical hoga—sirf intended final state same honi chahiye.



# Q2. POST request timeout ho gaya

# Timeout ka matlab ye nahi ki server ne request process nahi ki. Ho sakta hai server ne record create kar diya ho, lekin response tumhare client tak nahi aaya. Blindly POST retry karne se duplicate record ban sakta hai.



# Q3. Safe and idempotent method

# GET ka intended purpose data retrieve karna hai, resource state change karna nahi. Isliye GET generally safe bhi hai aur idempotent bhi.


# Concept	Simple meaning	Example
# Safe	Intended resource state change nahi karna	GET /users/10
# Idempotent	Same request repeat karne se final intended state same rahe	PUT /users/10
# Retry	Failure/timeout ke baad request dobara bhejna	GET ko retry karna

# Interview-ready:
# “I consider HTTP method semantics before retrying a failed request. GET is generally safe and idempotent, while POST retries may create duplicate resources unless the API supports appropriate idempotency controls.”

# ⭐ Lesson: Authentication + environment variables

# Ab hum seekhenge ki Python se protected API ko request kaise bhejte hain aur API token ko code mein hardcode karne se kaise bachte hain.

# ⭐ Authentication header
# GET /meetings
# Server chahta hai ki request ke saath valid access token bhi aaye. Python mein hum headers= use kar sakte hain.

import requests

url = "https://api.example.com/meetings"

headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Accept": "application/json"
}

response = requests.get(
    url,
    headers=headers,
    timeout=5
)

response.raise_for_status()
data = response.json()

print(data)

# Authorization batata hai ki client authentication credentials bhej raha hai.

# Bearer token-based authentication mein commonly use hone wala scheme hai.

# Accept: application/json batata hai ki client JSON response prefer karta hai.

# api.example.com ek placeholder hai; ye code actual API token aur valid endpoint ke bina successful request nahi karega.

# ⭐Token ko environment variable mein rakhna

# Step A: Windows PowerShell mein temporary variable set karo
# $env:API_TOKEN = "your_actual_token"
# Ye variable current PowerShell session ke liye set hoga. Real token ko public chat ya GitHub par share mat karna.

# Step B: Python mein variable read karo
import os

token = os.getenv("API_TOKEN")

if not token:
    print("API token is missing")
else:
    print("API token is configured")

# os.getenv("API_TOKEN") environment variable ki value deta hai. Agar variable set nahi hai, to default behaviour mein None milta hai.

# Concept 3 — Dono ko combine karna
# Ab token ko request header mein safely use karte hain.

import os
import requests

token = os.getenv("API_TOKEN")

if not token:
    print("API token is missing")
else:
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }

    try:
        response = requests.get(
            "https://api.example.com/meetings",
            headers=headers,
            timeout=5
        )

        response.raise_for_status()
        print(response.json())

    except requests.exceptions.RequestException as error:
        print("Request failed:", error)

# Notice: f"Bearer {token}" environment variable ki value ko header string mein insert karta hai. Hum token ko code mein directly store nahi kar rahe.

# Production projects mein .env file aur python-dotenv bhi use kar sakte hain. .env ko .gitignore mein rakhna zaroori hai; environment variables secrets ko manage karne mein help karte hain, lekin application logs ya public repositories mein token print nahi karna chahiye.

import os
import requests
token = os.getenv("API_KEY")
if not token:
       print("API token is missing")
else:
    header = {
          "Authorization": f"Bearer {token}",
          "Accept": "application/json"
      }

    for attempt in range(2):
        try:
            response = requests.get(
                    "https://api.example.com/meetings",
                    headers=header,
                    timeout=5
            )
        
            response.raise_for_status()
            print(response.json()) 
            break

        except requests.exceptions.RequestException as error:
            print("Request failed:", error)

            if attempt == 1:
                    print("Maximum attempts reached.")


# Retry logic correctly kaise kaam karta hai?

# Retry ka matlab hai failed request ko limited number of times dobara bhejna. Lekin har failure temporary nahi hota.

# Error / situation |	Retry karna chahiye? |		Reason
# Temporary timeout |		Usually, limited retries |		Server slow ho sakta hai ya network temporarily busy ho sakta hai
# Connection error |	Sometimes |		Network/server temporarily unavailable ho sakta hai
# 401 Unauthorized |	Usually nahi |		Token missing ya invalid hai; pehle credentials fix karo
# 403 Forbidden |	Usually nahi |		Permission nahi hai; same request repeat karne se permission nahi milegi
# 404 Not Found |	Usually nahi |		Resource ya endpoint nahi mila; URL/resource check karo
# 500 Internal Server Error |	Sometimes |		Server-side problem temporary ho sakti hai
# 429 Too Many Requests |	API instructions ke according |		Rate limit ke liye Retry-After header respect karna pad sakta hai

# Ye general guidelines hain. Actual retry policy API documentation aur operation par depend karti hai.

# Isliye timeout ka matlab hamesha ye nahi ki server ne request process nahi ki.

# GET requests ko generally retry karna safer hota hai, jabki POST ke liye duplicate actions ka risk check karna zaroori hai. Agar API idempotency keys support karti hai, to unka use duplicate creation se bachane mein help kar sakta hai.

# Iska issue ye hai ki RequestException bahut broad hai. Ismein timeout, connection errors aur HTTP errors jaise different failures aa sakte hain. Tum sabko same tarah treat kar rahe ho.

# Learning ke liye pehle sirf timeout ko retry karna seekhte hain. Isse tumhe specific exceptions handle karne ki practice hogi.

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

for attempt in range(2):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        print(response.json()["title"])
        break

    except requests.exceptions.Timeout:
        print("Request timed out.")

        if attempt == 1:
            print("Maximum attempts reached.")

    except requests.exceptions.RequestException as error:
        print("Request failed:", error)
        break


# Q4 Kya har RequestException ko retry karna good production practice hai? Apne words mein reason batao.
# “We should not retry every API error. Temporary failures such as timeouts may be retried with a limit, while errors such as 401 or 403 usually require fixing authentication or permissions. POST requests also need special care because retries can create duplicate resources.”


# Q3. Kya POST timeout hone par blindly retry karna safe hai? Ek line mein reason bhi batao.
# “A POST request may have been processed by the server even if the client receives a timeout. Retrying it blindly can create duplicate resources, so I check the API's retry and idempotency support before retrying.”