
import pandas as pd
from daviesfunctions import StochiometricNumber
from daviesfunctions import ProductsReactants
from daviesfunctions import ChargeNumber
from daviesfunctions import ActiviityCalculator
from daviesfunctions import logkintrinsic
import os

#find the k intrinsic value from the k conditional and ionic strength for a particular reaction
def kintrinsic(excelsheet):
    dirlast = os.path.abspath('..')
    folder_name = 'kintrinsic calculations'
    if not os.path.exists(dirlast + folder_name):
        os.makedirs(dirlast + folder_name)
    kintrinsicoutput = dirlast + folder_name + '/tester.xlsx'
    filename, file_extension = os.path.splitext(excelsheet)
    if file_extension == '.xlsx':
        df = pd.read_excel(excelsheet)
    elif file_extension == '.csv':
        df = pd.read_csv
    activityCoe = []
    for i in range(len(df)):
        reaction = df.at[i,'Reaction']
        ion = df.at[i,'Ion Strength']
        reactants = []
        products = []
        stocR =[]
        stocP =[]
        chargeR =[]
        chargeP = []
        activities = []
        ProductsReactants(reaction,reactants,products)
        lenR = len(reactants) 
        lenP = len(products)
        StochiometricNumber(lenR,reactants,stocR)
        StochiometricNumber(lenP,products,stocP)
        chargeR = ChargeNumber(lenR,reactants,chargeR)
        chargeP =ChargeNumber(lenP,products,chargeP)
        a = logkintrinsic(ion,lenR,lenP,activityCoe,chargeR,chargeP)
    df['Activity coefficeint'] = a
    df['Log k Intrinsic'] = df['Log K'] + df['Activity coefficeint'] 
    df.to_excel(kintrinsicoutput, index=False)
        
b = kintrinsic('/Users/eniolaadeyemi/Downloads/Reactions for davies_Pdma.xlsx') #user should specify the file path for the file to be analysed




    

