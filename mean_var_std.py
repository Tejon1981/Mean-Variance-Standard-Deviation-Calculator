import numpy as np
def calculate(list):

    if len(list)!=9:
        raise ValueError("List must contain nine numbers.")
# Convierte la lista a array y redmimensiona
    array=np.array(list)
    array=array.reshape(3,3)
# Calcula las estadísticasS
    calculations={
        'mean': [array.mean(axis=0).tolist(), array.mean(axis=1).tolist(), float(array.mean())],
        'variance': [array.var(axis=0).tolist(), array.var(axis=1).tolist(), float(array.var())],
        'standard deviation': [(array.std(axis=0)).tolist(), (array.std(axis=1)).tolist(), float(array.std())],
        'max': [array.max(axis=0).tolist(), array.max(axis=1).tolist(), int(array.max())],
        'min': [array.min(axis=0).tolist(), array.min(axis=1).tolist(), int(array.min())],
        'sum': [array.sum(axis=0).tolist(), array.sum(axis=1).tolist(), int(array.sum())]
        }
    print()
    return calculations
#############################################
    

#test_list=[0,1,2,3,4,5,6,7,]
#results=calculate(test_list)
#print(results)