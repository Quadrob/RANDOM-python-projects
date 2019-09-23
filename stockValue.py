
stockWorth = 0
cafeMenu = ["coffee","tea","latte","hot chocolate","ice coffee"]
stock = {"coffee":27, "tea":14, "latte":20, "hot chocolate":33, "ice coffee":25}
price = {"coffee":10, "tea":7.50, "latte":14.50, "hot chocolate":12, "ice coffee":17.25}

for item in stock :
   stockWorth += (stock[item]*price[item])
   
print("The total stock worth is : R" + str(stockWorth))