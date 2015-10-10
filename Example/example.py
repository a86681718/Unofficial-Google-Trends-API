__author__ = 'fang'
from pyGTrends import pyGTrends

connector = pyGTrends('a86681718@gmail.com', 'amy8426ainos')
connector.download_report(('apple', 'microsoft'))
print connector.csv()