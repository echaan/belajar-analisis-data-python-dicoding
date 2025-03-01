'''
    Measuring central tendency merupakan sekumpulan parameter statistik untuk menggambarkan nilai khas atau sentral yang mewakili keseluruhan observasi atau data. Nilai khas atau sentral tersebut direpresentasikan menggunakan tiga parameter statistik yaitu mean, median, dan mode
'''

import numpy as np
from scipy import stats 

jumlah_kucing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])

# mean = jumlah keseluruhan data dan dibagi dengan banyaknya data yang dimiliki
print(jumlah_kucing.mean())

#median - representasikan nilai tengah
print(np.median(jumlah_kucing))

#modus - nilai yang paling sering muncul dalam suatu data
print(stats.mode(jumlah_kucing)[0])
