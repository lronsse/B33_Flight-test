import pandas as pd
from scipy.io import loadmat


annots = loadmat('data.mat')
'''
con_list = [[element for element in upperElement] for upperElement in annots['obj_contour']]
newData = list(zip(con_list[0], con_list[1]))
columns = ['obj_contour_x', 'obj_contour_y']
df = pd.DataFrame(newData, columns=columns)'''

print(sorted(annots.keys()))
print(annots)
#print(annots['__header__'])
