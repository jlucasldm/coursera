hours = input('Enter Hours:')
rate = input('Enter Rate:')

hr = float(hours)
rt = float(rate)

def computepay(h,r):
    if hr > 40:
        pay=40*rt+((hr-40)*1.5*rt)
    else:
        pay=hr*rt
    return pay

print("Pay",computepay(hr,rt))