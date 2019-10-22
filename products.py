# 記帳程式
# 學習：將小清單建立在大清單


products = []                # 建立商品清單
while True:
    name = input('請輸入商品名稱/Insert a product: ')
    if name == 'q':          # 逃出迴圈
        break
    price = input('請輸入價格/Insert a price: ')   # price 寫在'break' 下方是因為如果是 'q'就可以提早跳出 
    products.append([name, price]) # 將小清單name, price放入大清單'products'
print(products)

for p in products:
    print(p[0], '的價格是', p[1])


# 存取二維清單：

products[0][0]                  # 進入大清單第0格,再進入小清單第0格
