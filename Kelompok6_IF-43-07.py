import pandas as pd

def distance(data1, data2):
    size1 = data1.get('Ukuran')
    comfort1 = data1.get('Kenyamanan')
    eco1 = data1.get('Irit')
    speed1 = data1.get('Kecepatan')
    #price1 = data1.get('Harga (Ratus Juta)')

    size2 = data2.get('Ukuran')
    comfort2 = data2.get('Kenyamanan')
    eco2 = data2.get('Irit')
    speed2 = data2.get('Kecepatan')
    #price2 = data2.get('Harga (Ratus Juta)')    
    #print(size1, comfort1, eco1, speed1, price1, size2, comfort2, eco2, speed2, price2)
    jarakeu = ((size1 - size2)**2 + (comfort1 - comfort2)**2 + (eco1 - eco2)**2 + (speed1 - speed2)**2)**0.5

    return jarakeu

def kNN(k):
    ans = []
    for i in range(len(inp)):
        list_jarak = []
        for j in range(len(df)):
            pair = (distance(inp.iloc[i], df.iloc[j]), j)
            list_jarak.append(pair)
        list_jarak.sort()
    
    print(list_jarak)
    for j in range(k):
        neighbour_index = list_jarak[j][1]
        #print(df.iloc[neighbour_index]['Nama Mobil'])
        ans.append(df.iloc[neighbour_index]['Nama Mobil'])
    #print(ans)
    return ans


df = pd.read_excel('E:\Kuliah\Semester_4\AI\TuProAI3\mobil.xls')
print("Input(ukuran, kenyamanan, irit, kecepatan):")
si, co, ec, sp = map(float, input().split())
data = {'Ukuran': [si], 'Kenyamanan': [co], 'Irit' : [ec], 'Kecepatan' : [sp]}
inp = pd.DataFrame(data)
inp.head()
knn_res = kNN(5)
rec = {'Nama Mobil' : [i for i in knn_res]}
rekomendasi = pd.DataFrame(rec)
rekomendasi.head()
print(rekomendasi)
#rekomendasi.to_excel('rekomendasi.xls', index=False)