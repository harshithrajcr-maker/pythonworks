
def display_person(**kwargs):

    print(kwargs)

display_person(name="hari",age=21,n_place="tvm",w_place="kakkanad",salary=34000)


def operation(*args,**kwargs):

    op=kwargs.get("key")

    if op=="max":

        return max(args)
    
    else:
        return min(args)

print(operation(10,20,30,40,key="max"))
print(operation(10,20,30,40,key="min"))