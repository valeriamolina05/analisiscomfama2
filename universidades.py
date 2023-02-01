#1. Importo a pandas
import pandas as pd

#2.Traigo fuente de datos
edadesCasa1=[25,25,25,25,25]
edadesCasa2=[1,4,24,26,70]

#3. genero los dataframes
dataFrame1=pd.DataFrame(edadesCasa1)
dataFrame2=pd.DataFrame(edadesCasa2)

#4. analisis descriptivo de los datos
analisis1=dataFrame1.describe()
analisis2=dataFrame2.describe()

#5. mostrar resultados 
print(analisis1)
print(analisis2)