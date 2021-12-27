record={ '101A':["Brown rice",50,45.50,41.25],
        '102B':["Whole Wheat",30,27.45,21.50],
        '102C':["Tomato sauce",25.50,20.25,18.70],
        '103D':["Mustard",40,39.45,37],
        '104E':["Barbeccue Sauce",45,43,41.50],
        '105F':["Red-wine vinegar",4000,3800,3750],
        '106G':["Salsa",200,189.50,170],
        '107H':["Extra Virgin Olive Oil",500,478.50,455.70],
        '108I':["Canola Oil",200,180,118],
        '109J':["Hot Pepper Sauce",100,98.50,91.25],
        '110K':["Bananas",60,55,50],
        '111L':["Apples",300,250,120],
        '112M':["Oranges",200,140,110],
        '113N':["Mangoes",100,80,50],
        '114O':["Strawberries",100,90,75],
        '115P':["Blueberries",95,80,75],
        '116Q':["Green Tea",250,225,200],
        '117R':["Sparkling Water",20,14.50,11],
        '118S':["Dried Apricots",270,250,230],
        '119T':["Dried Figs",100,95,90],
        '120U':["Dried prunes",90,85,80],
        '121V':["Almonds",900,870,850],
        '122W':["Cashews",1000,950,910],
        '123X':["Walnuts",800,770,720],
        '124Y':["Peanuts",400,380,360],
        '125Z':["Pecans",350,320,300],
        '201A':["Pistachios",1200,1180,1160],
        '202B':["Sunflower seeds",150,112.50,103.45],
        '203C':["Sesame seeds",120.50,110.25,101.40],
        '204D':["Whole flaxseeds",95.20,90.45,89.20],}
total=0
items=[]
"""print("The following are the items corresponding to them are their quality wise price per kg \n ",item_Record.values())"""
Registered={"AAA1001":["Surian",9500012345],"AAA1002":["Nila",9500023456],"AAA1003":["Arivazhagan",9712300078],"AAA1004":["Nithin Kumar",9586233333],"AAA1005":["Aravind",6931245872]}
n=int(input("How many items you want to purchase:"))
for i in range(n):
    item=input("What do you want to purchase:")
    quality=int(input("Enter the quality of item(1,2or3):"))
    quantity=float(input("How many kgs you want:"))
    for j in record:
        if(record[j][0]==item):
            amount=((record[j][quality])*(quantity))
            purchased=[j,item,amount]
            items.append(purchased)
            total+=amount
print(items)
user_name=input("Enter your name:")
userPh_No=int(input("Enter your phone number:"))
name=Registered.keys()
number=Registered.values()
if(((user_name in name) and (userPh_No in number))and (total>=10000)):
    cash_reward=(total*(1.2/100))
    purchase=total-cash_reward
    print(i,"is your customer id",user_name,userPh_No,"You have purchased",items,"Your total purchase is of",purchase,"Rs","as you are a registered user you have been awarded a Cash reward of",cash_reward)
if(((user_name not in name) and (userPh_No not in number))and (total>=10000)):
    discount=(total*(1/100))
    purchase=total-discount
    print(user_name,userPh_No,"You have purchased",items,"Your total purchase is of",purchase,"Rs"," \n as you have made a purchase of more than 10,000 Rs you have been awarded a discount of",discount)
else:
    print(user_name,userPh_No,"You have purchased",items,"Your total purchase is of",total,"Rs")
        

        
        

                
                
