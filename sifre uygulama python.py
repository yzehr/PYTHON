import random


def SifreOlustur(Uzunluk):
  alfabe="abcdefghijklmnoprtuvyzx"
  sifreler=[]
  for i in Uzunluk:
      sifre=""
      for j in range(i):
       IndexAta=random.randrange(len(alfabe))
       sifre=sifre+alfabe[IndexAta]
      sifre=DegistirSayi(sifre)
      sifre=DegistirBuyukHarf(sifre)
      sifreler.append(sifre)

  return sifreler
    

def DegistirSayi(sifre):
   for _ in range(random.randrange(1,3)):
    IndexDegistir=random.randrange(len(sifre))
    sifre=sifre[0:IndexDegistir] +str(random.randrange(10)) + sifre[IndexDegistir+1:]

   return sifre

def DegistirBuyukHarf(sifre):
   for _ in range(random.randrange(1,3)):
     IndexDegistir=random.randrange(len(sifre))
     sifre=sifre[0:IndexDegistir] +sifre[IndexDegistir].upper() + sifre[IndexDegistir+1:] 
   return sifre

  


def main():
    SifreAdedi=int(input("kac adet sifre istiyorsun: "))
    SifreUzunluk=[]
    for i in range(SifreAdedi):
      Uzunluk=int(input( str(i+1) + ".Sifren kac karakterli olsun istiyorsun: "))

      if Uzunluk<3 :
       Uzunluk=3

      SifreUzunluk.append(Uzunluk) 

   

  
   
    Sifre=SifreOlustur(SifreUzunluk)
    print("Sifre:", Sifre)

    for i in range(SifreAdedi):
      print(str(i+1)+ ".Sifreniz  "+ Sifre[i])

main()



















