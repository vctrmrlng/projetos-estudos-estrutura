#SE A IDADE >=18
   #Tem habilitação?
   #Se tiver , escreva pode dirigir!!
   #SENÃO SE não tiver, escreva: Voce precisa de uma uma habilitação para dirigir
   #SENÃO, escreva Você não tem idade para dirigir

idade= 18
habilitação =True

if idade >=18:
    if habilitação:
        print("Pode dirigir!🚗")
    #pass      #para o caso ser usado depois
    else:
        print("✖️Você precisa de uma habilitação para dirigir.")
else:
    print("Você não tem idade para dirigir.")
