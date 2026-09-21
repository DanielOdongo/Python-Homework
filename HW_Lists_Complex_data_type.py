one_a=[0,1,2,3,4,5,6,7,8,9]
one_b= one_a[5] +3
one_c= [float(x) for x in one_a]
one_d=set(one_c)
one_e=one_d.copy()
one_e.add(10)
one_f=one_e.copy()
one_f.pop()
one_g=len(one_f)
one_h=one_g==len(one_a)
one_i=list(one_f)+one_a
one_j=set(one_i)
one_k=len(one_j)

one_a=[0,1,2,3,4,5,6,7,8,9]
one_b= one_a[5] +3
one_c= [float(x) for x in one_a]
one_d=set(one_c)
one_e=one_d.copy()
one_e.add(10)
one_f=one_e.copy()
one_f.pop()
one_g=len(one_f)
one_h=one_g==len(one_a)
one_i=list(one_f)+one_a
one_j=set(one_i)
one_k=len(one_j)

two_patient_dictionary_kinoko = {
"name":"Kinoko",
"year":2021
}
two_patient_dictionary_dango = {
"name": "Dango",
"year": 2019
}
two_patient_dictionary_mochi = {
"name": "Mochi",
"year": 2020
}
two_a = {
"two_patinet_dictionary_kinoko":two_patient_dictionary_kinoko,
"two_patient_dictionary_dango": two_patient_dictionary_dango,
"two_patient_dictionary_mochi": two_patient_dictionary_mochi
}
two_b = two_a["two_patient_dictionary_dango"]["name"]
two_a["two_patient_dictionary_mochi"]["year"]=2018
two_d={
    "kinoko":2021,
    "dango":2019,
    "mochi":2019
}
two_e = list(two_d.keys())
two_f = list(two_d.values())
two_g = dict(zip(two_e,two_f))

three_seta = {1,2,3,4,5}
three_setb = {2,3,4,5,6}
three_setc = {3,5,7,9}
three_setd = {2,4,6,8}
three_sete = {1,2,3,4}
three_a = three_sete.issubset(three_seta)
three_b = three_sete < three_seta
three_c = three_seta.intersection(three_seta)
three_d = three_setc.union(three_setd,three_sete)
three_e = three_d.copy()
three_e.add(9)
three_f = three_e== one_a
three_g = "they are mostly not the same due to the fact because one of the is a list and the other is a set. The data would need to be similiar in order for it to be == true."

four_a = 8
four_b = []
four_b.append(type(four_a))
four_c = four_b
four_d = four_a + 0.39
four_c.append(type(0.39))
four_e = four_c
four_f = round(four_d ** -10)
four_e.append(type(four_f))
four_g = four_e

five_a = {
0: int,
1: float,
2: int
}
print(five_a)
five_b = str(four_f + 300)
four_g.append(type(five_b))
five_c = four_g
five_d = five_b[:2]
four_g.append(type(five_d))
five_e = four_g
five_f = [int(x) for x in five_d]
four_g.append(type(five_f))
five_g = four_g
four_g.append(type(three_seta))
five_h = four_g
