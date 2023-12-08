import matplotlib.pyplot as plt
from PIL import Image
#-----------------------------------------------first function-------------------------------------------
def bar():


    x=[i for i in range(1970,2005)]
    y=[40,45,48,50,51,54,56,58,59,61,64,65,68,69,71,74,76,79,82,84,86,89,93,95,98,101,105,109,110,111,112,115,117,118,120]
    plt.plot(x,y,'r.-')
    plt.xlabel("years")
    plt.ylabel("Industrial production index for chemicals")
    plt.title("Literacy and economic impact of Bhopal Gas Tragedy")
    plt.show()
    gas()
    
#-----------------------------------------------second function-------------------------------------------
def pic():


    print("======================")
    print("This are the prictures")
    print("======================")
    imaga = Image.open("pt1.png")
    image = Image.open("pt2.png")
    imagi = Image.open("pt3.png")
    imago = Image.open("pt4.jpg")

    imaga.show()
    image.show()
    imagi.show()
    imago.show()
    gas()

#-----------------------------------------------third function-------------------------------------------
def child():

    print("=================================================")
    print("Over 2,500 children in Bhopal are suffering from birth defects, a study \nconducted by an NGO working for Bhopal Gas Tragedy survivors has found. Over 2,500 children in Bhopal are \nsuffering from birth defects, a study conducted by an NGO working for Bhopal Gas Tragedy survivors has found")
    print("=================================================")
    imaga = Image.open("ps.png")
    image = Image.open("ps1.png")
    imagi = Image.open("ps2.png")
    imago = Image.open("ps3.png")

    imaga.show()
    image.show()
    imagi.show()
    imago.show()
    gas()


#-----------------------------------------------fourth function-------------------------------------------
def stats():
    x=[i for i in range(10)]
    y=[4,1,7,2,9,0,12,5,6,8]
    x2=[i+0.2 for i in range(10)]
    z=[4,2,9,2,4,0,1,5,5,2]
    plt.bar(x,y,color='red',width=0.2,label='male')
    plt.bar(x2,z,color='blue',width=0.2,label='female')
    plt.title("Sex wise distribution of severity of restriction")
    plt.xlabel("No. of subjects")
    plt.ylabel("Severity of resteiction")
    plt.legend()
    plt.show()
    gas()
#-----------------------------------------------fifth function-------------------------------------------
def pi():

    gg=[2,6,1,4,2,8]
    gland=['Oesophagus','Stomach','Colorectal','Liver','Gallbidder','Pancreas']
    explodes=[0,0,0,0,0,0.2]
    plt.pie(gg,labels=gland,explode=explodes)
    plt.title("Glands of people effected due to Bhopal Gas Tragedy")
    plt.show()
    gas()
#-----------------------------------------------menu function-------------------------------------------

def gas():
    print("Press the respective numeric key for your choice below:")
    print("-------------------------------------------------------")
    print("1. Graphical representation Literacy and economic impact of Bhopal Gas Tragedy")
    print("2. Pictures of people protesting for there rights!!")
    print("3. Images on the impact on the childrens due to this crisis")
    print("4. Bar-Graph of Sex wise distribution of severity of restriction")
    print("5. Show Piechart of Gland Effected of People")
    print("-------------------------------------------------------")
    n=int(input("You want a glance on :"))

    if n==1:
        bar()
    elif n==2:
        pic()
    elif n==3:
        child()
    elif n==4:
        stats()
    elif n==5:
        pi()
    else:
        print("oops!! Something went wrong")
#-----------------------------------------------interface/body function-------------------------------------------

print("The Bhopal disaster, also referred to as the Bhopal gas tragedy, was a gas leak incident on the night of 2–3 December 1984 at the Union Carbide India Limited (UCIL) pesticide plant in Bhopal, Madhya Pradesh, India.\nIt is considered among the world's worst industrial disasters.\nOver 500,000 people were exposed to methyl isocyanate (MIC) gas.\nThe highly toxic substance made its way into and around the small towns located near the plant")
x=input("Do you want more detail about this incident? (yes/no):")
if x.upper()=='YES':
    gas()
else:
    print("thanks for reading")


