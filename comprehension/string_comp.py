
words = ["profession","cat","program","dam","process"]

start_pro =[w for w in words if w.startswith("pro")]

print(start_pro)

result ={w for w in words if w.endswith("am")}

print(result)