# Price Data

item_dict = {'almonds': 6,
 'antioxidant juice': 9,
 'avocado': 1,
 'black tea': 4,
 'burgers': 4,
 'champagne': 3,
 'chicken': 4,
 'chocolate': 7,
 'chutney': 7,
 'cookies': 7,
 'cooking oil': 7,
 'cottage cheese': 9,
 'eggs': 9,
 'energy bar': 9,
 'energy drink': 3,
 'extra dark chocolate': 8,
 'french fries': 7,
 'fresh tuna': 9,
 'frozen smoothie': 7,
 'frozen vegetables': 2,
 'green grapes': 8,
 'green tea': 8,
 'honey': 9,
 'light cream': 5,
 'low fat yogurt': 4,
 'meatballs': 9,
 'milk': 5,
 'mineral water': 2,
 'oil': 9,
 'olive oil': 8,
 'pet food': 3,
 'protein bar': 1,
 'salad': 7,
 'salmon': 3,
 'shallot': 6,
 'shrimp': 2,
 'soup': 2,
 'spaghetti': 6,
 'spinach': 7,
 'tomato juice': 8,
 'tomatoes': 5,
 'turkey': 8,
 'vegetables mix': 3,
 'whole wheat flour': 5,
 'whole wheat pasta': 5,
 'whole wheat rice': 4,
 'yams': 7}

# transaction data

transaction_data = \
[['shrimp', 'almonds', 'avocado', 'vegetables mix', 'green grapes', 'whole wheat flour', 'yams', 'cottage cheese', 'energy drink', 'tomato juice', 'low fat yogurt', 'green tea', 'honey', 'salad', 'mineral water', 'salmon', 'antioxidant juice', 'frozen smoothie', 'spinach', 'olive oil'],
['burgers', 'meatballs', 'eggs'],
['chutney'],
['turkey', 'avocado'],
['mineral water', 'milk', 'energy bar', 'whole wheat rice', 'green tea'],
['low fat yogurt'],
['whole wheat pasta', 'french fries'],
['soup', 'light cream', 'shallot'],
['frozen vegetables', 'spaghetti', 'green tea'],
['french fries'],
['eggs', 'pet food'],
['cookies'],
['turkey', 'burgers', 'mineral water', 'eggs', 'cooking oil'],
['spaghetti', 'champagne', 'cookies'],
['mineral water', 'salmon'],
['mineral water'],
['shrimp', 'chocolate', 'chicken', 'honey', 'oil', 'cooking oil', 'low fat yogurt'],
['turkey', 'eggs'],
['turkey', 'fresh tuna', 'tomatoes', 'spaghetti', 'mineral water', 'black tea', 'salmon', 'eggs', 'chicken', 'extra dark chocolate'],
['meatballs', 'milk', 'honey', 'french fries', 'protein bar']]

def view_items():
 print('------------------View Items------------------')
 print('The number of items in the store are : ', len(item_dict))
 if len(item_dict) != 0:
  print('Here are all the items available in the store.')
  for key, value in item_dict.items():
   print(f"{key:<30} {value:<95}")

def view_transactions():
 print('------------------Total Transactions------------------')
 print('The number of transactions is : ', len(transaction_data))

def add_items():
 print('------------------Add Items to the store------------------')
 item_name = input('Enter the item to add : ')
 item_price = input('Enter the price of the item : ')
 item_dict[item_name] = item_price

def remove_items():
 print('------------------Remove Items from the store------------------')
 item_name = input('Enter the item to remove : ')
 item_dict.pop(item_name)

def findprice_item():
 print('------------------Find price of an item------------------\n')
 item_name = input('Enter the item name: ')
 item_price = item_dict[item_name]
 print(f"The price of {item_name} is {item_price}")

def search_transaction():
 print('------------------Search the transaction list------------------\n')
 transaction_num = int(input('Enter the transaction to find: '))
 transaction = transaction_data[transaction_num-1]
 print(f"There are {len(transaction)} items in this transaction and they are {transaction}")
 print(f"There are {len(transaction)} items in this transaction and they are\n")
 print(*transaction, sep="\n")
 find_totalcost(transaction)

def find_totalcost(transaction):
 total_cost_beftax = 0
 # for item in transaction:
 #  total_cost_beftax+= int(item_dict[item])
 total_cost_beftax += sum(int(item_dict[item]) for item in transaction)
 # total = sum(int(cost) for cost in item_dict[key for key in transaction])
 print(f"Total cost before tax: {total_cost_beftax}")
 find_total(total_cost_beftax)

def find_total(total_cost_beftax):
 tax = 5
 total_cost = total_cost_beftax + ((5/100) * total_cost_beftax)
 # total = sum(int(cost) for cost in item_dict[key for key in transaction])
 print(f"Mandatory govt. tax : {tax}")
 print(f"Total cost after tax : {total_cost}")

while True:
 print('------------------Welcome to the stores------------------\n')
 print('1. View items\n2. Total Transactions\n3. Add items\n4. Remove items\n5. Find Item price \n6. Search Transactions\n7. Quit\n')
 choice = input('Enter the number of your choice : ')
 if choice == '1':
  view_items()
 elif choice == '2':
  view_transactions()
 elif choice == '3':
  add_items()
  print('-------Item Added. Please have a look-----\n')
  view_items()
 elif choice == '4':
  remove_items()
  print('-------Item Removed. Please have a look-----\n')
  view_items()
 elif choice == '5':
  findprice_item()
  # print('-------Item Removed. Please have a look-----')
 elif choice == '6':
  search_transaction()
 elif choice == '7':
  print('------Quit-------')
  break
 else:
  print('You entered an invalid option')



