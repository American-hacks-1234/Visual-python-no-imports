r = "\033[31m"  # Red
w = "\033[0m"  # White
b = "\033[34m"  # Cyan
g = "\033[32m"  # Green
p=  "\033[35m" #purple
G=  "\033[2m" #grey
print(f'{w}testing colors...')
print(f"{w}{r}█{w}{g}█{w}{b}█{w}{p}█{w}{w}█{w}{G}█{w}")
print("testing 2D rendering...")
i=g#1,3
ii=r#2,3
iii=b#3,3
iv=r#1,2
v=b#2,2
vi=g#3,2
vii=b#1,1
viii=g#2,1
ix=r#3,1
print(f"{i}█{w}"*2+f"{ii}█{w}"*2+f"{iii}█{w}"*2)
print(f"{iv}█{w}"*2+f"{v}█{w}"*2+f"{vi}█{w}"*2)
print(f"{vii}█{w}"*2+f"{viii}█{w}"*2+f"{ix}█{w}"*2)
def clearframe():
    global i
    global ii
    global iii
    global iv
    global v
    global vi
    global vii
    global viii
    global ix
    i=w#1,3
    ii=w#2,3
    iii=w#3,3
    iv=w#1,2
    v=w#2,2
    vi=w#3,2
    vii=w#1,1
    viii=w#2,1
    ix=w#3,1
clearframe()
print("testing frame...")
def frame():
    print(f"{i}█{w}"*2+f"{ii}█{w}"*2+f"{iii}█{w}"*2)
    print(f"{iv}█{w}"*2+f"{v}█{w}"*2+f"{vi}█{w}"*2)
    print(f"{vii}█{w}"*2+f"{viii}█{w}"*2+f"{ix}█{w}"*2)
frame()
print("testing complete!")
