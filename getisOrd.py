#Importing Libraries
import arcpy
def getisOrd(workspace, fichier, champs, method):
    try:
        arcpy.env.workspace = workspace
        arcpy.HighLowClustering_stats(fichier, champs, "true", method, "EUCLIDEAN_DISTANCE", "ROW", 100, "#", "#")
        arcpy.addMessage("Résultat en format html enregistré dans la base de donnée")    
    except arcpy.ExecuteError:
    # Si une erreur à lieu, afficher le message :
        print(arcpy.GetMessages())
def getisOrdGi(fichier, champs, method, fdr, output):
    try:
        # Application de l'analyse
        arcpy.HotSpots_stats(fichier, champs, output,
                     method, "EUCLIDEAN_DISTANCE", 
                     "ROW", 100, "#", "#", fdr)
    except arcpy.ExecuteError:
    # Si une erreur à lieu, afficher le message :
        print(arcpy.GetMessages())
        
# Permet de lancer le script au cas où si le fichier est importé et non pas directement excécuté dans l'application
if __name__ == '__main__':
    #Viser le projet courant
    mxd = arcpy.mp.ArcGISProject("CURRENT")
    #Chercher la carte dans le projet
    aprx = mxd.listMaps("Map")[0]
    
    # Le nom de votre environnement de travail
    workspace = arcpy.GetParameterAsText(0)
    # Le shapefile à étudier
    fichier = arcpy.GetParameterAsText(1)
    # Le nom du champs
    champs = arcpy.GetParameterAsText(2)
    # Méthode à utiliser
    method = arcpy.GetParameterAsText(3)
    # Application ou non du FDR
    fdr = arcpy.GetParameterAsText(4)
    # Nom du shapefile de sortie
    output = arcpy.GetParameterAsText(5)
    # Application du Getis Ord General
    # getisOrd(workspace, fichier, champs, method)
    # Application du Getis Ord Gi*
    getisOrdGi(fichier, champs, method, fdr, output)
    aprx.addDataFromPath(output)
    
