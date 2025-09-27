listfruit=["orange","orange","orange","apple","apple","apple","apple","apple","apple","banana","pineapple","mango","pawpaw","groundnut"]
for i in listfruit:
    print(i)
    if i=="orange":
        listfruit.remove(i)
    else:
        continue
    print(listfruit)

