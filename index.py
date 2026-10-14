#Topic - Rest API

# ⭐ GET vs POST, query parameters vs JSON body

# ⭐ GET — data retrieve karna
# response = requests.get(    "https://example.com/meetings/101",    params={"include_tasks": True},    timeout=5)



# 101 URL path mein resource identify karta hai. params query string add karta hai, jaise ?include_tasks=True.

# ⭐ POST — data submit karna
# response = requests.post(    "https://example.com/summarize",    json={"transcript": "Meeting transcript..."},    timeout=5)



# json= transcript ko request body mein JSON ke roop mein bhejta hai.

#⭐ Query parameters vs JSON body
# Feature	Query parameters	JSON body
# Python Requests argument	params=	json=
# Kahan bheja jata hai?	URL mein	Request body mein
# Common use	Filtering, searching, options	Data submit karna
# Example	?userId=1	{"transcript":"..."}
# Query parameters automatically secret nahi hote — woh URL mein visible ho sakte hain. Sensitive data, jaise passwords ya API keys, URL mein nahi bhejna chahiye.


# ⭐REST concept: Idempotency

# Idempotent operation ka matlab: same request ko multiple times repeat karne se server par intended final state nahi badalti, first request ke comparison mein.
# - GET: generally idempotent — data retrieve karne se resource change nahi hona chahiye.
# - PUT: generally idempotent — resource ko ek specified state mein set karna.
# - DELETE: HTTP semantics ke hisaab se idempotent — resource ko delete karne ke baad repeat request se final state wahi rehti hai, chahe response alag ho.
# - POST: generally idempotent nahi — same request repeat karne se multiple resources ya repeated actions ho sakte hain.

# Interview answer: “Idempotency means repeating the same request has the same intended effect on the resource state as making it once. GET, PUT, and DELETE are generally idempotent, while POST is not necessarily idempotent.”


