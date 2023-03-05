# Une toolbox pour produire une analyse Getis-Ord General, une analyse Getis-Ord Gi* et une différence

2 scripts sont compris dans la toolbox.
1/ Un script pour calculer le Getis-Ord General et le Getis-Ord Gi*
Vous pouvez choisir :
- Votre environnement de travail
- Le fichier sur lequel appliqué l'analyse
- Le champs d'étude
- La méthode utilisée (INVERSE_DISTANCE, INVERSE_DISTANCE_SQUARED, FIXED_DISTANCE_BAND ou ZONE_OF_INDIFFERENCE)
- L'application ou non du FDR
- Le fichier de sortie

Les paramètres suivants sont imposés :
- La distance est de 100 mètres
- La standardisation est en ligne (ROW)
- Le rapport est obligatoirement créé dans la bade de donnée 
- La méthode euclidienne est utilisée pour calculer les distances (EUCLIDEAN_DISTANCE)

Pour plus d'information sur le Getis Ord General et le Getis-Ord Gi*, allez voir la documentation officielle d'Arcgis Pro :
- Getis-Ord General : https://pro.arcgis.com/fr/pro-app/latest/tool-reference/spatial-statistics/high-low-clustering.htm
- Getis-Ord Gi* : https://pro.arcgis.com/fr/pro-app/latest/tool-reference/spatial-statistics/hot-spot-analysis.htm

Le jeu de donnée test utilisé se trouve dans le dossier donneesTest. Ce jeu de donnée est un quadrillage pour 2013 et 2015 de la densité de population ayant la dengue. Le champs utilisé pour l'étude est "DEN_POB".

2/ Un script pour calculer le nombre d'entités ayant un Gi_Bin > 0 sur 1, 2 ou plusieurs années
Cet outil permet de repérer les clusters persistents sur plusieurs années.
Le jeu test par défaut utilise 2 années, mais il est possible d'étendre l'analyse temporelle à plusieurs années. 
