# writes file 
def write_products(products, filename="products.txt"): 
    try: 
        with open(filename, 'w') as file:  
            for product_info in products.values(): 
                line = ",".join(product_info) 
                file.write(line + "\n") 
    except Exception as e: 
        print("Error writing to file: " + str(e)) 
 
''' it imports datetime module to create different and unique 
invoice each time''' 
from datetime import datetime   
 
 
# generate invoice 
def invoice_generation(transaction_type, customer_name, phone, items, total): 
    try: 
        now = datetime.now() 
        timestamp = str(now.year) + str(now.month) + str(now.day) + "_____" + 
str(now.hour) + str(now.minute) + str(now.second) #shows the year, month and day, 
similarly the time, hour,minutes and second 
        filename = transaction_type + "__invoice__" + timestamp + ".txt" 
        with open(filename, "w") as file: 
            file.write(transaction_type.upper() + " INVOICE\n")
     file.write("Transaction Date: " + str(now.year) + "-" + str(now.month) + "-" + 
str(now.day) + "___" + str(now.second) + "-" + str(now.minute) + "-" + str(now.hour) + 
"\n") 
            file.write("Customer: " + customer_name + "\nPhone: " + phone + "\n") 
            file.write("-" * 50 + "\n") 
            file.write("Product Name\t\tBrand\tQuantity\tPrice\t\tTotal\n") 
            for item in items: 
                line = item['product_name'] + "\t" + item['brand'] + "\t" + str(item['quantity']) + 
"\t" + str(item['unit_price']) + "\t" + str(item['total']) + "\n" 
                file.write(line) 
            file.write("-" * 50 + "\n") 
            file.write("Total: " + str(total) + "\n") 
 
        print(transaction_type + " invoice " + filename) 
    except Exception as e: 
        print("Error generating invoice: " + str(e)) 
 
''' import invoice_generation and write_products function from write ''' 
from write import invoice_generation, write_products 
