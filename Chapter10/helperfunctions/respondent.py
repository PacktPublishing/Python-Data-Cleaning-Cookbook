import math
import datetime as dt

class Respondent:
  respondentcnt = 0

  def __init__(self, respdict):
    self.respdict = respdict
    Respondent.respondentcnt+=1
   
  # add the number of children at home and not at home


  def childnum(self):
    return self.respdict['childathome'] + self.respdict['childnotathome']

  # select the weeksworked## keys and calcuate the average of their values
  def avgweeksworked(self):
    workdict = {k: v for k, v in self.respdict.items() \
      if k.startswith('weeksworked') and not math.isnan(v)}
    nweeks = len(workdict)
    if (nweeks>0):
      avgww = sum(workdict.values())/nweeks
    else:
      avgww = 0
    return avgww

  # define a function for calculating given start and end date
  def ageby(self, bydatestring):
    bydate = dt.datetime.strptime(bydatestring, '%Y%m%d')
    birthyear = self.respdict['birthyear']
    birthmonth = self.respdict['birthmonth']
    age = bydate.year - birthyear
    if (bydate.month<birthmonth or (bydate.month==birthmonth \
        and bydate.day<15)):
      age = age -1
    return age

  def baenrollment(self):
    colenrdict = {k: v for k, v in self.respdict.items() \
      if k.startswith('colenr') and v=="3. 4-year college"}
    if (len(colenrdict)>0):
      return "Y"
    else:
      return "N"



