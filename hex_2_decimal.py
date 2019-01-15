import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Reading the data into a csv file
df = pd.read_csv('can_data_just_hex.csv')

#extracting columns and grouping them in pairs
bit0 = df.loc[:,['bit00','bit01']]
bit1 = df.loc[:,['bit10','bit11']]
bit2 = df.loc[:,['bit20','bit21']]
bit3 = df.loc[:,['bit30','bit31']]
bit4 = df.loc[:,['bit40','bit41']]
bit5 = df.loc[:,['bit50','bit51']]
bit6 = df.loc[:,['bit60','bit61']]
bit7 = df.loc[:,['bit70','bit71']]

#combining the respective pairs

b0 = bit0['bit00'] + bit0['bit01']
b1 = bit1['bit10'] + bit1['bit11']
b2 = bit2['bit20'] + bit2['bit21']
b3 = bit3['bit30'] + bit3['bit31']
b4 = bit4['bit40'] + bit4['bit41']
b5 = bit5['bit50'] + bit5['bit51']
b6 = bit6['bit60'] + bit6['bit61']
b7 = bit7['bit70'] + bit7['bit71']

# converitng from hex to decimal
def hex2dec(b):
    b = np.asarray(b).reshape((len(b),1))
    d = np.zeros((len(b),1))
    for i in range(len(b)):
        if type(b[i,0]) == str:
            d[i,0] = int(b[i,0],16)
        else:
            c = np.array_str(b[i,0])
            d[i,0] = int(c,16)

    return d

# storing values in respective arrays as decimal values
d0 = hex2dec(b0)
d1 = hex2dec(b1)
d2 = hex2dec(b2)
d3 = hex2dec(b3)
d4 = hex2dec(b4)
d5 = hex2dec(b5)
d6 = hex2dec(b6)
d7 = hex2dec(b7)

#data visualization
x = np.arange(len(d0)).reshape(len(d0),1)

plt.plot(x,d0)
plt.plot(x,d1)
plt.plot(x,d2)
plt.plot(x,d3)
plt.plot(x,d4)
plt.plot(x,d5)
plt.plot(x,d6)
plt.plot(x,d7)
plt.gca().legend(('b0','b1','b2','b3','b4','b5','b6','b7'))
plt.show()
