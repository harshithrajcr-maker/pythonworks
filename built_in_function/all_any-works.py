
lst = [2,4,6,8,7,9,3]

t_f_lst=[num%2==0 for num in lst]

is_all_even=all(t_f_lst)

# print(is_all_even)

lst1 =["housefull","beautiful","peaceful","harmful","thinkful","powerful"]

end_ful=[w.endswith('ful') for w in lst1]

is_ful=all(end_ful)

# print(is_ful)

words = ["program","problem","prefect","apple"]

str_pro =[w.startswith('pro') for w in words]

# print(any(str_pro))

number =15

print(not any(number%i==0 for i in range(1,number)))