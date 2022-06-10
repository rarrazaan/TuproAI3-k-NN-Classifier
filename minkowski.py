import pandas as pd

def distance(data1, data2):
    size1 = data1.get('Ukuran')
    comfort1 = data1.get('Kenyamanan')
    eco1 = data1.get('Irit')
    speed1 = data1.get('Kecepatan')
    price1 = data1.get('Harga (Ratus Juta)')

    size2 = data2.get('Ukuran')
    comfort2 = data2.get('Kenyamanan')
    eco2 = data2.get('Irit')
    speed2 = data2.get('Kecepatan')
    price2 = data2.get('Harga (Ratus Juta)')    
    #print(size1, comfort1, eco1, speed1, price1, size2, comfort2, eco2, speed2, price2)
    p = 1.5
    jarakeu = (abs(size1 - size2)**p + abs(comfort1 - comfort2)**p + abs(eco1 - eco2)**p + abs(speed1 - speed2)**p + abs(price1 - price2)**p)**p

    return jarakeu

def kNN(k):
    ans = []
    for i in range(len(inp)):
        list_jarak = []
        for j in range(len(df)):
            pair = (distance(inp.iloc[i], df.iloc[j]), j)
            list_jarak.append(pair)
        list_jarak.sort()
    
    #print(list_jarak)
    for j in range(k):
        neighbour_index = list_jarak[j][1]
        #print(df.iloc[neighbour_index]['Nama Mobil'])
        ans.append(df.iloc[neighbour_index]['Nama Mobil'])
    #print(ans)
    return ans


df = pd.read_excel('https://rarrazaan.github.io/mobil.xls')
print("Input(ukuran, kenyamanan, irit, kecepatan):")
si, co, ec, sp = map(int, input().split())
pr = float(input("Harga: "))
data = {'Ukuran': [si], 'Kenyamanan': [co], 'Irit' : [ec], 'Kecepatan' : [sp], 'Harga (Ratus Juta)' : [pr]}
inp = pd.DataFrame(data)
inp.head()
knn_res = kNN(3)
rec = {'Nama Mobil' : [i for i in knn_res]}
rekomendasi = pd.DataFrame(rec)
rekomendasi.head()
print(rekomendasi)
#rekomendasi.to_excel('rekomendasi.xls', index=False)