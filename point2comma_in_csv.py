# -*- coding: iso-8859-15 -*-
"""
Ligne de commande POINT2COMMA_IN_CSV.PY utilisant comme paramêtre d'entrée un nom de dossier pour la recherche d'éventuels fichiers CSV
@author: Damien/Python4D
@summary: Permet de transformer les points en virgules dans les CSV se trouvant dans le dossier indiqué et ses sous-dossiers.
"""

import os,sys

if len(sys.argv)<=1:
  print u"! Tu n'as pas indiqué en argument un dossier en particulier, je considére le dossier et sous dossier actuel... !"
  dirtop="."
else:
  dirtop=os.path.abspath(sys.argv[1])
str_in="."
str_out=","
f_csv=[]
print u"Dossier sélectionné: '",dirtop,"'"
if os.path.exists(dirtop):
  for d,sd,f in os.walk(dirtop,topdown=False):
    for files in f:
      if files[-3:].lower()=="csv":
        f_csv.append(os.path.join(d,files))
  print u"Liste des fichiers 'csv' trouvés:",f_csv
  if f_csv!=[]:
    print(u"\nEtes vous sur de modifier tous les fichiers listés ci-dessus? \nTapez 'OUI':")
    ask=raw_input()
    if ask==u"OUI":
      for files in f_csv:
        s = open(files).read()
        s = s.replace(str_in, str_out)
        f = open(files, 'w')
        print u"J'écrase:",f
        f.write(s)
        f.close()
    else:
      print u"! abandon... !"
  else:
    print u"! aucun fichier csv trouvé !"
else:
  usage = sys.argv[0].split("\\")[-1]+u" <DIR>\n\n\tCherche les fichiers csv du dossier <DIR> et les sous-dossiers puis remplace les '.' par ','\n\tSi pas d'argument recherche dans le dossier courant\n\n"
  print usage
