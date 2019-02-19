def finalStockPrice(x):
  
   stock1_price = stock1[0] + sum(stock1[1]) 
   stock2_price = stock2[0] + sum(stock2[1]) 
   stock3_price = stock3[0] + sum(stock3[1]) 
   x = [stock1_price, stock2_price, stock3_price]
   return x


stock1 = [10, [1, -.5, 2, -1.45]]
stock2 = [2, [.4, -.2, .1, .05, -.23, .03]]
stock3 = [400, [10, -9, 9, 9, -20, 24, -22, 100, -24, -23]]

stocks = [stock1[0]]
stocks = [stock2[0]]
stocks = [stock3[0]]


for i in stocks:  
    print(finalStockPrice(i)) 