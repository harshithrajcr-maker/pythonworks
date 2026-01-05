try:

    file_path ="Error_handling\\numbers.txt"

    fr=open(file_path,"r")

    number=[]

    for line in fr:

        line =line.rstrip("\n")

        try:

            num = int(line)

            number.append(num)

        except Exception as e:

            continue

    print(number)

    max_num = max(number)
    min_num = min(number)
    total =sum(number)

    print(max_num)
    print(min_num)
    print(total)

    number_count = {num:number.count(num) for num in number}
    
    max_value = max(number_count.values())

    freq = [k for k,v in number_count if v==max_value]

    print(freq)

except Exception as e:
    print(e)