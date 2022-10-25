def powerofnumber(base,exp):
    # assert int(base) == base and int(base)>=0, "base has to be positive integer"
    if int(exp) in [0,1]:
        return base
    else:
        return int(base) * powerofnumber(int(base),int(exp)-1)

print(powerofnumber(2,4))