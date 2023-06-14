import random as rd

first_names = [
    "Aarav", "Advait", "Akash", "Amrita", "Ananya", "Arjun", "Avantika", "Ayush", "Chetan", "Deepika"
]

last_names = [
    "Agarwal", "Bhattacharya", "Chatterjee", "Das", "Gupta", "Iyer", "Jain", "Kapoor", "Lal", "Mishra"
]


cities = [
    "Mumbai", "Delhi", "Bangalore", "Kolkata", "Chennai", "Hyderabad", "Ahmedabad", "Pune", "Surat", "Jaipur",
    "Lucknow", "Kanpur", "Nagpur", "Indore", "Thane", "Bhopal", "Visakhapatnam", "Pimpri-Chinchwad", "Patna",
    "Vadodara", "Ghaziabad", "Ludhiana", "Coimbatore", "Agra", "Madurai", "Nashik", "Faridabad", "Meerut",
    "Rajkot", "Varanasi"
]

states = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh",
    "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland",
    "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand",
    "West Bengal"
]


def generate_address():
    full_name = (rd.choice(first_names))+ " "+(rd.choice(last_names))
    city = rd.choice(cities)
    state = rd.choice(states)
    zip_code = rd.randint(600001, 699999)
    address = f"{full_name} \n{city} \n{state} \n{zip_code}"

    return address

print(generate_address())