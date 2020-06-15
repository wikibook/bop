print('Simple Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']
# mylist는 단지 같은 객체를 가리키는 또 다른 이름일 뿐입니다!
mylist = shoplist

# 첫 번째 품목을 구입했으므로 리스트에서 제거합니다
del shoplist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)
# shoplist와 mylist 모두 'apple'이 없는 같은 리스트를 출력한다는 점에
# 유의합니다. 이것은 두 리스트가 같은 객체를 가리킨다는 사실을 보여줍니다.

print('Copy by making a full slice')
# 전체 슬라이스를 통해 사본을 만듭니다
mylist = shoplist[:]
# 첫 번째 항목 제거
del mylist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)
# 이제 두 리스트가 다르다는 데 주의합니다
