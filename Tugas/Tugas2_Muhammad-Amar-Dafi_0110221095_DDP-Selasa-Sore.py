# Grab customer's name
customer_name = input("Masukkan nama anda : ")

# Product price list
price_list = {
    "Kipas Angin" : 1000000,
    "TV" : 2000000,
    "Mesin Cuci" : 3000000,
    "AC": 4000000,
    "Kulkas": 5000000
}
# Variable to store customer's selected products 
selected_products = {}

# Grab customer's seleted products
areThereMore = True
while areThereMore == True:
    print("\n===================================================")
    print("Pilihan Produk")
    print("[1] Kipas Angin  -> Rp. 1.000.000/unit")
    print("[2] TV \t\t -> Rp. 2.000.000/unit")
    print("[3] Mesin Cuci \t -> Rp. 3.000.000/unit")
    print("[4] AC \t\t -> Rp. 4.000.000/unit")
    print("[5] Kulkas \t -> Rp. 5.000.000/unit")
    product_selection = int(input("Pilihan anda : "))
    
    if product_selection == 1:
        key = "Kipas Angin"
    elif product_selection == 2:
        key = "TV"
    elif product_selection == 3:
        key = "Mesin Cuci"
    elif product_selection == 4:
        key = "AC"
    elif product_selection == 5:
        key = "Kulkas"
    else:
        print("Pilihan Invalid")
        break
    
    if key in selected_products:
        print(f"Anda telah membeli {key} sebanyak {selected_products[key]} ingin mengubah?")
        print("[1] Menambahkan")
        print("[2] Mengurangi")
        mod_selection = int(input("Pilihan : "))
        if mod_selection == 1:
            amount = int(input("Jumlah yang ingin ditambahkan : "))
            selected_products[key][0] = selected_products[key][0] + amount
            selected_products[key][1] = selected_products[key][0] * price_list[key]
        elif mod_selection == 2:
            amount = int(input("Jumlah yang ingin dikurangi : "))
            if amount > selected_products[key]:
                print("Invalid input")
                break
            selected_products[key][0] = selected_products[key][0] - amount
            selected_products[key][1] = selected_products[key][0] * price_list[key]
        else:
            print("Invalid Input")
            break

    else:
        print(f"Masukkan jumlah {key} yang ingin dibeli")
        selected_products[key] = [int(input("Jumlah : "))]
        selected_products[key].append(selected_products[key][0] * price_list[key])

    print("===================================================")
    print("Berikut daftar belanjaan anda : ")
    
    for key, value in selected_products.items():
        print(f"=> {key} sebanyak {value[0]} unit")

    areThereMore = input("Ada yang ingin di ubah[y/n]? ")
    if areThereMore == "y":
        areThereMore = True
    else:
        areThereMore = False

# Count the gross, discount, tax, and net 
gross = 0
for x in selected_products:
    gross = gross + selected_products[x][1]

discount = gross * (5/100)
promo = [
    ["Kulkas", 5, (20/100)],
    ["AC", 3, (10/100)]
]
for x in promo:
    key = x[0]
    qty = x[1]
    amount = x[2]
    if key in selected_products.keys() and selected_products[key][0] >= qty:
        discount =  discount + (selected_products[key][1] * amount)
tax = (gross - discount) * (10/100)
net = gross - discount + tax

# Print customer's receipt 
print("\n===================================================")
print("Nama Pelanggan \t\t: ", customer_name)
print("Produk yang dibeli")
for key, value in selected_products.items():
    if len(key) < 5:
        key = key + "\t"
    print(f"=> {key} \tx {value[0]}\t: Rp. {value[1]}")
print("===================================================")
print("Total harga kotor \t: Rp.", gross)
print("Diskon \t\t\t: Rp.", discount)
print("PPN \t\t\t: Rp.", tax)
print("Total harga bersih \t: Rp.", net)



 


