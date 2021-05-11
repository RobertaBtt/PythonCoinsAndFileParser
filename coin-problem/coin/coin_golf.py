import math
c=[2.0,1.0,0.50,0.20,0.10,0.05,0.02,0.01]
def get_coins(m):
    r=[]
    for k,v in enumerate(c):
        if m>=v:
            f,w=math.modf(m/v)
            r.extend([v]*int(w))
            if f == 0:break
            else:m=round(m-(v*w),2)
    return r


