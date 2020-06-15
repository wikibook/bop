import pickle

# 객체를 저장할 파일의 이름
shoplistfile = 'shoplist.data'
# 구입할 품목의 리스트
shoplist = ['apple', 'mango', 'carrot']

# 파일에 씁니다
f = open(shoplistfile, 'wb')
# 객체를 파일에 저장합니다
pickle.dump(shoplist, f)
f.close()

# shoplist 변수를 삭제합니다
del shoplist

# 저장장치에서 읽어옵니다
f = open(shoplistfile, 'rb')
# 파일에서 객체를 불러옵니다
storedlist = pickle.load(f)
print(storedlist)
f.close()
