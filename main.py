print("Intrinsic Value Calculator")
print("------------------------------")
fcf=float(input("enter free cash flow: "))
gr=float(input("enter growth rate as(example: 10%=1.1): "))
a1=fcf*gr
a2=a1*gr
a3=a2*gr
a4=a3*gr
a5=a4*gr
a6=a5*gr
a7=a6*gr
a8=a7*gr
a9=a8*gr
a10=a9*gr
print("10th year free cashflow: ",a10)
fcfm=float(input("Enter average free cash flow multiple: "))
tv=fcfm*a10
print("Terminal Value: ",tv)
eri=float(input("Enter expected ROI(example:10%=1.1): "))
d1=a1/eri
d2=a2/(eri**2)
d3=a3/(eri**3)
d4=a4/(eri**4)
d5=a5/(eri**5)
d6=a6/(eri**6)
d7=a7/(eri**7)
d8=a8/(eri**8)
d9=a9/(eri**9)
d10=a10/(eri**10)
dtv=tv/(eri**10)
du=d1+d2+d3+d4+d5+d6+d7+d8+d9+d10
ivl=du+dtv
print("The intrinsic value: ",ivl)
av=float(input("Enter current marketcap: "))
while av>ivl:
  print("Overvalued")
  break

while av<ivl:
  print("Undervalued")
  break

while av==ivl:
  print("Perfectly valued")
  break

print("------------------------------")
