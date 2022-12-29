querystring = {"SchemeCode": '120389, 120503, 119125, 119242, 118551'}
scheme_code1 = querystring.get("SchemeCode").split(',')
scheme_code = [i.strip() for i in querystring.get("SchemeCode").split(',')]


print(scheme_code)
print([i.strip() for i in querystring.get("SchemeCode").split(',')])
print(a)

