from math import sqrt
import math
import numbers
from typing import final

r = "Zn+2 + 2Citrate-3 = Zn(Citrate)-" #how to tackle water error

#splitting reactants and products 
reactants = []
products = []
def ProductsReactants(reaction,reactantlist,productlist):
    reaction_breakdown = reaction.split(" ")
    equal_sign = reaction_breakdown.index('=')
    for i in reaction_breakdown:
        position = reaction_breakdown.index(i)
        if position < equal_sign and i != '+':
            reactantlist.append(i)
        elif i != '=' and i != '+':
            productlist.append(i)
    return reactantlist , productlist

ProductsReactants(r,reactants,products)


#determining stochiometric amount for reactants and products 
h = len(reactants)
z = len(products)
stocR = []
stoc_product =[]

#finding stochiometric numbers
def StochiometricNumber(x,r_plist,newlist):
    for i in range(x):
        stoc_numb = r_plist[i][0]
        if stoc_numb.isdigit():
            newlist.append(float(stoc_numb))
        else:
            newlist.append(1.00)
    return newlist
    

xu = StochiometricNumber(z,products,stoc_product)
yu = StochiometricNumber(h,reactants,stocR)

#finding charge number
chargeR=[]
chargeP=[]
def ChargeNumber(x,r_plist,newlist): #function takes number of reactants in list , list of reactants , new list to store values
    for i in range(x):
        x = i
        stoc_numb = r_plist[x][-1]
        previous_value = r_plist[x][-2]
        if stoc_numb.isdigit(): 
            if previous_value == ')': #account for equations (OH)2 where 2 is not the charge
                newlist.append(0.00)
            else:
                newlist.append(float(r_plist[x][-1]))
        elif stoc_numb == '+' or stoc_numb == '-': #add code that checks if the previous one is a sign then add it as the charge value 
            newlist.append(1.00)
        elif stoc_numb == ')':
            newlist.append(0)
    return newlist
#need to account for +/- that comes before the number 
a = ChargeNumber(h,reactants,chargeR)
b = ChargeNumber(z,products,chargeP)


#calculations 
I = [0.1]

values = [] #list

def ActiviityCalculator(IonicList,NumberReactant, NumberProduct,Storagelist,chargeR,chargeP): #how to specify type , will make the code easier to read / use
    for ion in IonicList:
        A = 0.51
        figure_react = 0
        for i in range(NumberReactant):
            calc1 = -A*chargeR[i]*chargeR[i]
            print(chargeR[i])
            calc2 = sqrt(ion)/(1+sqrt(ion))
            calc3 = -0.3*ion
            final_react = (calc1*(calc2+calc3))
            figure_react += final_react
        print(figure_react)
        figure_prod = 0
        for i in range(NumberProduct):
            calc1prod = -A*chargeP[i]*chargeP[i]
            calc2prod = sqrt(ion)/(1+sqrt(ion))
            calc3prod = -0.3*ion
            final_prod = (calc1prod*(calc2prod+calc3prod))
            figure_prod += final_prod
        print(final_prod)
        activity = figure_prod - figure_react
        Storagelist.append(activity)
    return Storagelist
 

def logkintrinsic(ion,lenR,lenP,activityCoe,chargeR,chargeP):
    A = 0.51
    figure_react = 0
    for i in range(lenR):
        calc1 = -A*chargeR[i]*chargeR[i]
        calc2 = sqrt(ion)/(1+sqrt(ion))
        calc3 = -0.3*ion
        final_react = (calc1*(calc2+calc3))
        figure_react += final_react
    print(figure_react)
    figure_prod = 0
    for i in range(lenP):
        calc1prod = -A*chargeP[i]*chargeP[i]
        calc2prod = sqrt(ion)/(1+sqrt(ion))
        calc3prod = -0.3*ion
        final_prod = (calc1prod*(calc2prod+calc3prod))
        calc3prod = -0.3*ion
        figure_prod += final_prod
    print(final_prod)
    activity = figure_prod - figure_react
    activityCoe.append(activity)
    return activityCoe
        




a = ActiviityCalculator(I,h,z,values,chargeR,chargeP)
print(a)




        





