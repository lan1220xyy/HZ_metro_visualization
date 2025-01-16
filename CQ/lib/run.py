import show_fig as sh
import generate_fig as generate

dim = 10         #2 or 10
path = "DAYS"   #days or HOURS
len = 7         #7 or 18
dataset = 'HZ'

# generate.myFig(dataset,dim,path,len)
sh.show(path,dataset,len,dim)
#  [9,38,57,62,76] [15,36,41,43,44] [6,29,30,59,70] [6,15,37,46,50]