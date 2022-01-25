import dataiku


def testf():
  print('start testf()')
  f = dataiku.Folder("29522.yCKNDeC2")
  folder_path = f.get_path()
  print('folder_path:', folder_path)
  return 2
