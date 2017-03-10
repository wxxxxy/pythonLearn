def str2float(s):
    def char2num(s):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
    def str2int1(s):
        return reduce(lambda x,y:x*10+y,map(char2num,s))
    def str2int2(s):
        return reduce(lambda x,y:x/10+y,map(char2num,s[::-1]))
    #s[::-1]把字符串反转过来
    p = s.split('.')
    s1,s2 = str2int1(p[0]),str2int2(p[1])
    return s1+s2/10