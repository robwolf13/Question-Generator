# numbers to letters
small = ['zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
tens = ['mistake0','mistake1','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
# simple algorithm that take a number less than a billing and converts it into a str
def convert(n):
    if n < 20:
        return small[n]
    elif n < 100:
        if n % 10 == 0:
            return tens[n//10]
        else:
            return tens[n//10] + '-' + small[n%10]
    elif n < 1000:
        if n % 100 == 0:
            return convert(n//100) + ' hundred'
        else:
            return convert(n//100)+' hundred and '+convert(n%100)
    elif n < 10**6:
        if n % 1000 == 0:
            return convert(n//1000)+' thousand'
        else:
            return convert(n//1000)+' thousand '+convert(n%1000)
    else:
        if n % 10**6 == 0:
            return convert(n//10**6)+' million '
        else:
            return convert(n//10**6)+' million '+convert(n%10**6)




