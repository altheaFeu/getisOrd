import arcpy
def zonesTouches(liste):
    """
    Permet de déterminer si une zone est touchée
    1 = touchée, 0 = non touché
    """
    try:
        # Création du champs
        [arcpy.management.AddField(data, "zone_touche", "LONG") for data in liste]
        # Modification du champs
        [arcpy.management.CalculateField(data, f"zone_touche", "!Gi_Bin! > 0", "PYTHON3") for data in liste]
        
    except arcpy.ExecuteError:
    # Si une erreur à lieu, afficher le message :
        print(arcpy.GetMessages())
def joindreTables(liste):
    """
    Joindre les tables pour les dates
    """
    try:
        arcpy.management.JoinField(liste[0], "OBJECTID", liste[1], "OBJECTID")
        
    except arcpy.ExecuteError:
    # Si une erreur à lieu, afficher le message :
        print(arcpy.GetMessages())
def sommeTemporelle(donnee, champs):
    """
    Faire une somme des zones touchées
    """
    try:
        arcpy.management.AddField(donnee, "sommeTemp", "LONG")
        # Création du calcul
        chaines = "$feature.sommeTemp"
        chaines = [chaines + f" + $feature.{champ}" for champ in champs]
        # Application
        [arcpy.management.CalculateField(donnee, "sommeTemp", chaine, "ARCADE") for chaine in chaines]
        
    except arcpy.ExecuteError:
    # Si une erreur à lieu, afficher le message :
        print(arcpy.GetMessages())
def symSomme(mxd, aprx):
    """
    Modifier la symbologie de la couche finale sur les sommes
    """
    try:
        layer = aprx.listLayers('sommeTemp')[0]
        sym = layer.symbology 
        sym.updateRenderer('UniqueValueRenderer') 
        sym.renderer.fields = ['sommeTemp']
        colorRamp = mxd.listColorRamps("Errors")[0] 
        sym.renderer.colorRamp = colorRamp 
        
        layer.symbology = sym 
        
    except arcpy.ExecuteError:
    # Si une erreur à lieu, afficher le message :
        print(arcpy.GetMessages())
        
if __name__ == '__main__':
    #Viser le projet courant
    mxd = arcpy.mp.ArcGISProject("CURRENT")
    #Chercher la carte dans le projet
    aprx = mxd.listMaps("Map")[0]
    
    # Vos données :
    workspace = arcpy.GetParameterAsText(0)
    arcpy.env.workspace = workspace
    data = arcpy.GetParameterAsText(1)
    liste = data.split(';')
    zonesTouches(liste)
    joindreTables(liste)
    field_names = [f.name for f in arcpy.ListFields(liste[0]) if f.name.find("zone_touche") > -1]
    sommeTemporelle(liste[0], field_names)
    # Copie du fichier pour en avoir un séparé
    arcpy.management.Rename(liste[0], f"{workspace}/sommeTemp", "FeatureClass")
    aprx.addDataFromPath(f"{workspace}/sommeTemp")
    symSomme(mxd,aprx)
