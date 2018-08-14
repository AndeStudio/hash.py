import hashlib

#algs hash算法列表 如md5 sha1/sha224/sha256/sha384/sha512 sha3_224/sha3_256/sha3_384/sha3_512
def hash(file,algs):
    alg=[]
    for i in range(len(algs)):
        alg.append(eval('hashlib.'+algs[i])())
    with open(file, 'rb') as f:
        for l in f:#分次读入文件,避免大文件时用read()会内存不足
            for i in range(len(alg)):#分别调用hash算法计算hash值并更新,相比单独重新可节约开销
                alg[i].update(l)
    return alg

file='hash.py'
algs=['md5','sha1']
hv=hash(file,algs)
for (a,h) in zip(algs, hv):
    print(a +" : " + h.hexdigest())
