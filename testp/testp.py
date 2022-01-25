import dataiku

def load_model():
  print('start load_model()')
  f = dataiku.Folder("29522.yCKNDeC2")
  folder_path = f.get_path()
  print('load_model:', folder_path)
  return 1

def testf(model=load_model()):
  print('start testf().')
  return 5
