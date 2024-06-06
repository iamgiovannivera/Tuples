# 1. Tuple Mastery in Python

# def format_itineraries(itineraries):
#     formatted_str = ""
#     for index, itinerary in enumerate(itineraries, start=1):
#         traveler_name, origin, destination = itinerary
#         formatted_str += f"Itinerary {index}: {traveler_name} - From {origin} to {destination}\n"
#     return formatted_str.strip()

# # Example usage:
# itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
# formatted_itineraries = format_itineraries(itineraries)
# print(formatted_itineraries)


# 2. Python Data Structure Challenges


# library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

# def add_book(library, book):
#     if book not in library:
#         library.append(book)
#         print(f"Book '{book[0]}' by {book[1]} added to the library.")
#     else:
#         print(f"Book '{book[0]}' by {book[1]} is already in the library.")

# # Example usage:
# new_books = [("1984", "George Orwell"), ("To Kill a Mockingbird", "Harper Lee")]
# for book in new_books:
#     add_book(library, book)

# print(library)


# 3. Python Loops and Tuples 


# stock_data = [
#     ("AAPL", "2021-01-01", 130.0),
#     ("AAPL", "2021-01-02", 132.0),
#     ("MSFT", "2021-01-01", 220.0),
#     ("AAPL", "2021-01-03", 135.0),
#     ("MSFT", "2021-01-02", 225.0),
#     # More data...
# ]

# def average_closing_price(stock_data, stock_symbol):
#     total_price = 0
#     count = 0
#     for record in stock_data:
#         symbol, date, price = record
#         if symbol == stock_symbol:
#             total_price += price
#             count += 1
#     if count == 0:
#         return 0
#     return total_price / count

# # Example usage:
# average_price = average_closing_price(stock_data, "AAPL")
# print(f"Average closing price for AAPL: {average_price:.2f}")



# 4. Mastering Tuple Packing and Unpacking 


# orders = [
#     ("Alice", "Laptop", 1),
#     ("Bob", "Camera", 2),
#     # More orders...
# ]

# def process_orders(orders):
#     for order in orders:
#         customer_name, product, quantity = order
#         print(f"Customer {customer_name} ordered {quantity} {product}(s)")

# # Example usage:
# process_orders(orders)



# 5. Advanced Tuple Techniques


# catalog1 = (("Laptop", 1000), ("Camera", 500))
# catalog2 = (("Smartphone", 800), ("Tablet", 450))

# def merge_catalogs(*catalogs):
#     merged_catalog = ()
#     for catalog in catalogs:
#         merged_catalog += catalog
#     return merged_catalog

# # Example usage:
# merged_catalog = merge_catalogs(catalog1, catalog2)
# print("Combined Catalog:")
# for product, price in merged_catalog:
#     print(f"Product: {product}, Price: ${price}")

# # Example with more catalogs:
# catalog3 = (("Headphones", 150), ("Smartwatch", 300))
# merged_catalog = merge_catalogs(catalog1, catalog2, catalog3)
# print("\nCombined Catalog with more products:")
# for product, price in merged_catalog:
#     print(f"Product: {product}, Price: ${price}")