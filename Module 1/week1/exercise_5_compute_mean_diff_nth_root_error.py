
def md_nre_single_sample(y,y_hat,n,p):
    assert all([isinstance(n, int), isinstance(p,int), isinstance(y,(float,int)), isinstance(y_hat,(float,int))])
    result = (y**(1/n) - y_hat**(1/n))**p
    print(result)

md_nre_single_sample(100, 99.5,2,1)