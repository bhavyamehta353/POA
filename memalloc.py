def first_fit(psize, bsize):
    totalmem = 0.0
    utilmem = 0.0
    for k in bsize: totalmem += k

    for i in psize:
        for j in range(len(bsize)):
            if(i <= bsize[j]):
                print("Inserted process size",i ,"in block size" , bsize[j])
                utilmem += i
                bsize[j] = 0
                break
        if j == len(bsize) - 1:
            print("Process size", i , "cannot be inserted")
    
    mem_utilization = (utilmem/totalmem)*100
    print("Memory Utilisation:",mem_utilization)

def best_fit(psize , bsize):
    totalmem = 0.0
    utilmem = 0.0
    for i in bsize: totalmem += i
    bsize.sort()
    for i in psize:
        for j in range(len(bsize)):
            if i <= bsize[j]:
                print("Inserted Process size",i ,"in block size" ,bsize[j])
                utilmem += i
                bsize[j] = 0
                break
        if j == len(bsize) - 1:
            print("Process size", i , "cannot be inserted")
    mem_utilization = (utilmem/totalmem)*100
    print("Memory Utilisation:",mem_utilization)
    
def worst_fit(psize , bsize):
    totalmem = 0.0
    utilmem = 0.0
    for i in bsize: totalmem += i

    bsize.sort(reverse = True)
    for i in psize:
        for j in range(len(bsize)):
            if i <= bsize[j]:
                print("Inserted Process size",i ,"in block size" ,bsize[j])
                utilmem += i
                bsize[j] = 0
                break
        if j == len(bsize) - 1:
            print("Process size", i , "cannot be inserted")
    mem_utilization = (utilmem/totalmem)*100
    print("Memory Utilisation:",mem_utilization)

blocksize = input("Block sizes separated by commas:").split(",")
processsize = input("Process size separated by commas:").split(",")

blocksize = [int(x) for x in blocksize]
processsize = [int(x) for x in processsize]

blocksize1 = blocksize.copy()
processsize1 = processsize.copy()

blocksize2 = blocksize.copy()
processsize2 = processsize.copy()

print(blocksize)
first_fit(processsize, blocksize)
print("\n")
best_fit(processsize1 , blocksize1)
print("\n")
worst_fit(processsize2, blocksize2)

