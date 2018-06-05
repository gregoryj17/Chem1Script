h=1.008
he=4.003
li=6.941
be=9.012
b=10.81
c=12.01
n=14.01
o=16.00
f=19.00
ne=20.18
na=22.99
mg=24.31
al=26.98
si=28.09
p=30.97
s=32.07
cl=35.45
ar=39.95
k=39.10
ca=40.08
sc=44.96
ti=47.88
v=50.94
cr=52.00
mn=54.94
fe=55.85
co=58.93
ni=58.69
cu=63.55
zn=65.39
ga=69.72
ge=72.61
ars=74.92
se=78.96
br=79.90
kr=83.80
rb=85.47
sr=87.62
y=88.91
zr=91.22
nb=92.91
mo=95.94
tc=98.0
ru=101.1
rh=102.9
pd=106.4
ag=107.9
cd=112.4
ind=114.8
sn=118.7
sb=121.8
te=127.6
i=126.9
xe=131.3
cs=132.9
ba=137.3
la=138.9
hf=178.5
ta=180.9
w=183.9
re=186.2
os=190.2
ir=192.2
pt=195.1
au=197.0
hg=200.6
tl=204.4
pb=207.2
bi=209.0
po=209.0
at=210.0
rn=222.0
fr=223.0
ra=226.0
ac=227.0
rf=261.0
db=262.0
sg=263.0
bh=262.0
hs=265.0
mt=268.0
ds=281.0
rg=280.0
cn=285.0
uut=284.0
fl=289.0
uup=288.0
lv=293.0
uus=294.0
uuo=294.0
ce=140.1
pr=140.9
nd=144.2
pm=145.0
sm=150.4
eu=152.0
gd=157.3
tb=158.9
dy=162.5
ho=164.9
er=167.3
tm=168.9
yb=173.0
lu=175.0
th=232.0
pa=231.0
u=238.0
np=237.0
pu=244.0
am=243.0
cm=247.0
bk=247.0
cf=251.0
es=252.0
fm=257.0
md=258.0
no=259.0
lr=262.0
R=0.0820574
def sqrt(num):
    return pow(num, 0.5)
kB=8.3145
def rms(temp_celsius, mass_grams):
    return sqrt(3*kB*(273.15+temp_celsius)/(mass_grams/1000.0))
def eff(r1, m1, r2, m2):
    if r1 is None:
        return r2*sqrt(m2/m1)
    if r2 is None:
        return r1/sqrt(m2/m1)
    if m1 is None:
        return pow(r2/r1,2)*m2
    if m2 is None:
        return pow(r1/r2,2)*m1
