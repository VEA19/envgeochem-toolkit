# envgeochem-toolkit guide

Main objectives of program: Calculate davies activity coefficient , generate PHREEQC input files , plot Ligand Exchange points as a function of pH and Ionic Strength by processing PHREEQC output files & calculate Intrinsic stability constant from a file. Folder structure is very important.

Main folder

Create the following Subfolders with the name in bold:

• **code** : contains all the py files in this repository

• **pqi** folder : stores generated PQI files

• **pqo** folder : stores PQO files , PQO files need to be in this folder for the code to run

• **template** folder : contains examples of reference files for code input

• **validate** folder

• **lepcsv** folder

• **lepout** folder

• **table** folder 

• **output** folder 

• **davies** folder 

• **daviesfig** folder 

• **kintrinsic calculations** folder 

• **lepfig** folder 

• **template** folder 

• **data** folder : contains all databases in PHREEQC



A folder template will be linked. Absolute paths referenced in code need to be changed to correct paths based on your computer and data storage

Link to folder template:  https://www.dropbox.com/sh/g2ydrebe596ffrh/AAD_hFgS5LwFduAuTjh3ZEqea?dl=0

Instructions

1 Download the code folder into a main folder on your computer

2 Run searchui.py to extract metal/ligand reaction and stability constant from database e.g for iron - citrate complexation input fecitrate

i The result is stored in the table folder

3 Run Davies.py to generate master species section for PHREEQC input file, user input required in lines 315/316 , table of stability constant at different ionic strength for a metal-ligand reaction. Results are stored in the Davies folder

4 Run pqigenerator.py to generate PQI files for specific metal-ligand complexation at different ionic strengths. The user should add a list of ionic strengths to the list on line 8 and the chosen metal and ligand on line 93. PQI files are

stored in PQI folder

5 Run plot.py to generate a graph of stability constant against ionic strength for specific metal-ligand eg FeCitrate. The results are stored in the daviesfig folder

6 Run pqoextract.py to generate the data for plotting. User should change on line 180 to the metal , ligand of study and specify 3pH and 3 ionic strength of which PQO files are present. The result is stored in a csv file in lepcsv folder

7 Run lepph or lepion for generation of lep figures. Specify the metal in ionic form and the 2 ligands in line 103 of lepph.py or 88 of lepion.py. In LEPion , users will also need to specify the ionic strength. The graphs are stored in the lepfig folder

8 Run kintrinsic.py for converting a table of reactions with conditional stability constants to intrinsic value using the Davies activity model. A reference file is shown in the template folder. This code produces an excel sheet stored in the kintrinsic calculations folder.

9 Run main in LEPUI.py for the complete ligand exchange process from Davies calculation to PQI generation to plotting - must have phreeqc installed for this if not , run each item individually and add PHREEQC output files to PQO folder
