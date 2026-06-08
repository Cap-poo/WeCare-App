 DEFINE FUNCTION read_products with filename products.txt 
 INITIALIZE an empty dictornary named products 
        TRY 
  OPEN filename and READ all line into info 
  SET product_name = 1 
  FOR each line in info” 
   REMOVE newline, SPLIT by comma 
   INCREMENT product_number 
 EXCEPT FileNotFoundError: 
  PRINT “File not found” 
 RETURN products 
END FUNCTION 
 
2.3.2 For write.py 
DEFINE FUNCTION write_products with parameter products, and file product.txt 
 START FUNCTION 
  TRY 
   OPEN filename in write mode as file 
   FOR each product_info in products: 
    JOIN product_info with comma into lines 
    WRITE line to file with newline 
  EXCEPT exception as e: 
   PRINT “Error writing to file” 
  END TRY 
END FUNCTION 
 
Invoice_generation 
 
DEFINE FUNCTION invoice_generation with parameters (transaction_type, 
customer_name, phone, items, total) 
START FUNCTION 
 TRY 
  GET current date and time  
  CREATE unique filename using transaction_type and timestamp 
  OPEN filename in write mode as file 
  WRITE invoice title and transaction time to file 
  WRITE customer name and phone 
  FOR each item in items: 
  FORMAT item details Into line 
  WRITE line to file 
  WRITE total amount 
  PRINT invoice filename 
 EXCEPT any error: 
  PRINT “Error generating invoice” 
 END TRY 
END FUNCTION 
 
2.3.3 For operation.py 
 
IMPORT invoice_generation, write_products from Write 
DEFINE FUNCTION sell_product with parameter products 
TRY 
 LOOP to check valid customer_name: 
  INPUT name 
  CHECKS name 
 LOOP until valid phone_number: 
  INPUT phone number 
  CHECKS phone 
INITIALIZE cart empty, grand_total 0 
 LOOP  
  DISPLAY all available Products  
 LOOP until valid selected_id 
  INPUT product ID 
  CHECKS id and exists in product.txt 
 TRY 
  INPUT quantity  
 EXCEPT valueError: 
  PRINT “Invalid quantity. Enter integer” 
 CALCULATE free_items = quantity // 3 
 CALCULATE total_required = quantity + free_items 
  
 IF total_required > available_stock: 
  PRINT “not sufficient Quanitity” 
  CONTINUE 
 UPDATE stock = stock – total_requred 
 CALCULATE unit_price = price * 3 
 CALCULATE item_total = unit_price * quantity 
 ADD grand_total to item_total 
 
 ASK if user wants to sell more 
 IF not ‘y’:  
  BREAK 
 CALL invoice_generation 
EXCEPT exception as e: 
 PRINT “An error occured” 
END FUNCTION 

Restocking 
DEFINE FUNCTION restock_products 
START FUNCTION  
 TRY 
  LOOP to check valid vendor_name: 
   INPUT vendor_name 
   CHECK name 
  LOOP to check valid phone 
   INPUT phone  
   CHECK number 
  INITIALIZE cart empty, total_cost 0 
   
  LOOP 
   DISPLAY available products from product.txt 
   
   LOOP to check valid selected_id: 
    INPUT product ID 
    CHECK id 
   TRY 
    INPUT quantity  
   EXCEPT ValueError: 
    PRINT “Invalid quantity. Please enter a number/ digits.” 
    CONTINUE 
   INPUT new price (optional) 
   IF price entered: 
    UPDATE price of product 
   CALCULATE total = unit_price * quantity 
   ADD total to total_cost 
   UPDATE product  
   APPEND product details to cart 
  
   ASK if users want to restock more 
   IF not y  
    BREAK 
  CALL invoice_generation 
 EXCEPT Exception as e: 
  PRINT “Error during restocking” 
END FUNCTION 
 
2.3.4 For main.py 
IMPORT read_products from read 
IMPORT write_products from write 
IMPORT sell_product, restock_product from operation 
 
DEFINE FUNCTION main 
START FUNCTION 
    DISPLAY “welcome to WeCare Wholesale System 
    CALL read_products  
 
    LOOP 
        DISPLAY menu options 
 TRY 
          GET user input as choice 
          IF choice == 1: 
              CALL sell_product(products) 
          ELIF choice == 2: 
              CALL restock_product(products) 
          ELIF choice == 3: 
              CALL write_products(products) 
              PRINT “Thank you and visit again” 
              BREAK  
        ELSE: 
            PRINT “Invalid Option, Please Choose Valid option” 
 EXCEPT ValueError: 
  PRINT “Please choose valid Option” 
     
END FUNCTION
