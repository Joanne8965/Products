# 寫入txt. 檔

products = []               
while True:
    name = input('請輸入商品名稱/Insert a product: ')
    if name == 'q':         
        break
    price = input('請輸入價格/Insert a price: ')   
    products.append([name, price]) 
print(products)

for p in products:
    print(p[0], '的價格是', p[1], 'The price of',p[0], 'is', p[1])



# 字串可以做合併 + 和 * , 但不能減和除！  
    # 'abc' + '123' = 'abc123'
    # 'abc' * 3 = 'abcabcabc'


# 寫成 txt. 檔案
with open('products.txt', 'w') as f:        # 'w' = write
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')    # 寫入商品,逗點和價格合併， '\n' 分行的意思
                                             # 'f' = open('products.txt', 'w')










