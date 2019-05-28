def fibs(num):
    fibs=[0,1]
    for i in range(num-1):
        fibs.append(fibs[-2]+fibs[-1])
    return fibs
