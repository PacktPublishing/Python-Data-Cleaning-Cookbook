
class Collectionitem:
  collectionitemcnt = 0

  def __init__(self, colldict):
    self.colldict = colldict
    Collectionitem.collectionitemcnt+=1
   
  def birthyearcreator1(self):
    if ("birth_year" in self.colldict['creators'][0]):
      byear = self.colldict['creators'][0]['birth_year']
    else:
      byear = "Unknown"
    return byear

  def birthyearsall(self):
    byearlist = [item.get('birth_year') for item in \
      self.colldict['creators']]
    return byearlist

  def ncreators(self):
    return len(self.colldict['creators'])

  def ncitations(self):
    return len(self.colldict['citations'])






