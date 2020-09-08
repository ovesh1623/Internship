import time

def solution(D):
    d = {'Mon':None,'Tue':None,'Wed':None,'Thu':None,'Fri':None,'Sat':None,'Sun':None}

    for i in D:
        j = time.strftime("%A", time.strptime(i, "%Y-%m-%d"))
        if j == 'Monday':
            d['Mon'] = D.get(i) if d['Mon'] == None else d['Mon'] + D.get(i)
        elif j == 'Tuesday':
            d['Tue'] = D.get(i) if d['Tue'] == None else d['Tue'] + D.get(i)
        elif j == 'Wednesday':
            d['Wed'] = D.get(i) if d['Wed'] == None else d['Wed'] + D.get(i)
        elif j == 'Thursday':
            d['Thu'] = D.get(i) if d['Thu'] == None else d['Thu'] + D.get(i)
        elif j == 'Friday':
            d['Fri'] = D.get(i) if d['Fri'] == None else d['Fri'] + D.get(i)
        elif j == 'Saturday':
            d['Sat'] = D.get(i) if d['Sat'] == None else d['Sat'] + D.get(i)
        else:
            d['Sun'] = D.get(i) if d['Sun'] == None else d['Sun'] + D.get(i)
    
    for i in d:
        if d[i] == None:
            if i == 'Mon':
                d[i] = int((d['Sun'] + d['Tue'])/2)
            elif i == 'Tue':
                d[i] = int((d['Mon']+d['Wed'])/2)
            elif i == 'Wed':
                d[i] = int((d['Tue']+d['Thu'])/2)
            elif i == 'Thu':
                d[i] = int((d['Wed']+d['Fri'])/2)
            elif i == 'Fri':
                d[i] = int((d['Thu']+d['Sat'])/2)
            elif i == 'Sat':
                d[i] = int((d['Fri']+d['Sun'])/2)
            elif i == 'Sun':
                d[i] = int((d['Sat']+d['Mon'])/2)
    return d

D = {'2020-01-01':4,'2020-01-02': 4, '2020-01-03':6,'2020-01-04':8,'2020-01-05':2, '2020-01-07':2,'2020-01-08':-2}
print(solution(D))
