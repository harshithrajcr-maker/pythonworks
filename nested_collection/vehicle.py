
vehicles = [
    {"name": "Swift", "brand": "Maruti Suzuki", "price": 650000, "model": 2021, "color": "White", "fuel_type": "Petrol"},
    {"name": "Baleno", "brand": "Maruti Suzuki", "price": 820000, "model": 2022, "color": "Blue", "fuel_type": "Petrol"},
    {"name": "Creta", "brand": "Hyundai", "price": 1500000, "model": 2023, "color": "Black", "fuel_type": "Diesel"},
    {"name": "i20", "brand": "Hyundai", "price": 950000, "model": 2021, "color": "Red", "fuel_type": "Petrol"},
    {"name": "Seltos", "brand": "Kia", "price": 1600000, "model": 2023, "color": "Silver", "fuel_type": "Diesel"},
    {"name": "Sonet", "brand": "Kia", "price": 1200000, "model": 2022, "color": "Grey", "fuel_type": "Petrol"},
    {"name": "Harrier", "brand": "Tata", "price": 1900000, "model": 2023, "color": "White", "fuel_type": "Diesel"},
    {"name": "Nexon", "brand": "Tata", "price": 1200000, "model": 2022, "color": "Blue", "fuel_type": "Petrol"},
    {"name": "Punch", "brand": "Tata", "price": 800000, "model": 2023, "color": "Green", "fuel_type": "Petrol"},
    {"name": "XUV700", "brand": "Mahindra", "price": 2200000, "model": 2023, "color": "Black", "fuel_type": "Diesel"},
    {"name": "Thar", "brand": "Mahindra", "price": 1700000, "model": 2022, "color": "Red", "fuel_type": "Petrol"},
    {"name": "Scorpio N", "brand": "Mahindra", "price": 2000000, "model": 2023, "color": "White", "fuel_type": "Diesel"},
    {"name": "City", "brand": "Honda", "price": 1500000, "model": 2021, "color": "Silver", "fuel_type": "Petrol"},
    {"name": "Amaze", "brand": "Honda", "price": 900000, "model": 2022, "color": "Grey", "fuel_type": "Petrol"},
    {"name": "Kiger", "brand": "Renault", "price": 800000, "model": 2021, "color": "Blue", "fuel_type": "Petrol"},
    {"name": "Duster", "brand": "Renault", "price": 1300000, "model": 2020, "color": "Brown", "fuel_type": "Diesel"},
    {"name": "EcoSport", "brand": "Ford", "price": 1100000, "model": 2021, "color": "White", "fuel_type": "Petrol"},
    {"name": "Endeavour", "brand": "Ford", "price": 3600000, "model": 2020, "color": "Black", "fuel_type": "Diesel"},
    {"name": "Altroz", "brand": "Tata", "price": 950000, "model": 2022, "color": "Golden", "fuel_type": "Petrol"},
    {"name": "Venue", "brand": "Hyundai", "price": 1300000, "model": 2023, "color": "Red", "fuel_type": "Petrol"}
]

all_vehicle_names = [v.get("name") for v in vehicles]

print("all vehicles\n",all_vehicle_names)

all_brands ={v.get("brand") for v in vehicles}

print("all vehicle brands\n",all_brands)

#display vehcle names whose color = red

vehicles_colour_red = [v.get("name") for v in vehicles if v.get("color")=="Red"]

print("red colour vehicles\n",vehicles_colour_red)

# display vehicles names  whose model 2022


vehicles_names_2022 =[v.get("name") for v in vehicles if v.get("model")==2022] 

print("model 2022 vehicles\n",vehicles_colour_red)

# display diesel vehile names

vehicles_deasal =[v.get("name") for v in vehicles if v.get("fuel_type")=="Diesel" ]

print("display diesel vehile names\n",vehicles_deasal)

# display all vehicle price

all_vehicle_price =[v.get("price") for v in vehicles ]

print("all vehicles price\n",all_vehicle_price)

# display vehicle names whose price > 10lac

gt_10lac = [v.get("name") for v in vehicles if v.get("price")>1000000]

print("gt 10lac\n",gt_10lac)

# display tata vehicle names

tata_vehicles =[v.get("name") for v in vehicles if v.get("brand")=="Tata"]

print("Tata vechicles\n",tata_vehicles)

# display tata vecle whose model 2022

tata_vehicles_model_2022 =[v.get("name") for v in vehicles if v.get("brand")=="Tata" and v.get("model")==2022]

print("tata vehicle model 2022\n",tata_vehicles_model_2022)

# display vehcle availabe at lowest price

lowest_price = min(v.get("price") for v in vehicles)

lowest_price_vehicle = [v.get("name") for v in vehicles if v.get("price") == lowest_price]

print("lowest price vehicle:", lowest_price_vehicle)

# dsipaly prices of maruthi suzuki vehicles

maruthi_susuki_vehicle_price = [v.get("price") for v in vehicles if v.get("brand")=="Maruti Suzuki"]

print("maruthi suzuki vehicle price\n",maruthi_susuki_vehicle_price)

# display hundayi vehicle names avaiale at > 5lac

hyundai_price_5lak =[v.get("name") for v in vehicles if v.get("brand")=="Hyundai" and v.get("price")>500000]

print("hyundai vehicles  above 5lac\n",hyundai_price_5lak)

# display vehicle names whose model in range of 2022 - 2024

range_of_2022_2024 =[v.get("name") for v in vehicles if 2022<= v.get("model")<=2024]

print("2022 to 2024 model vehicles\n",range_of_2022_2024)

# which brand have most number of vehicle



