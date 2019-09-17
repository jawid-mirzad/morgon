# start

# vakna upp
vaken = "n"                                           Det är ett värde.
print("Du sover djupt  som björnen i ide...")
while vaken == "n":                                   Det är ett värde om man svarar n det försättar fråga om vaken.
    vaken = input("Vaknar du?[y/n] ").lower()         Man svarar y eller n.

# duscha
print("Du masar dig upp och släpar dig in i duschen.") skriver ut filen.
print("Någon har lämnat en brödrost i din dusch")
duscha = input("Flyttar du på brödrosten? [y/n] ").lower() 
if duscha == "n":
    exit("Du elchockas och ditt äventyr är slut")
elif duscha == "y":
    print("frisk vatten sköljer över dig och du börjar äntligen vakna.")
else:
    print("DOSE NAT COMPUTE")

# årstid
season = False
while season == False:      De andra rader som är under while tillhör till vhile
    season = input("Vilken årstid är det? [vår, vinter, sommar, höst]").lower()
    if season == "vår" or season == "vinter" or season == "höst":
        print("Det är kallt och slask, fy tusan!")
        print("Du klär på dig vinterpälsen...")
    elif season == "sommar":
        print("Sommar! shorts och flip flops")
    else:
        season = False
