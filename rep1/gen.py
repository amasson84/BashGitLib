ext=['txt']
prj=['my function is one I like to eat bread','my function is two I like to eat cream','my function is one I like to drink cream','my function is two I like to dance with bread']

for i,t in prj:
    file=open(i+ext,'w+')
    file.write(t)
    file.close()
