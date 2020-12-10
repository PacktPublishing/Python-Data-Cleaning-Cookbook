# import pandas
import pandas as pd

# get the R data
import rpy2.robjects as robjects
from rpy2.robjects import pandas2ri

pandas2ri.activate()
readRDS = robjects.r['readRDS']
nls97withvalues = readRDS('data/nls97withvalues.rds')

nls97withvalues
