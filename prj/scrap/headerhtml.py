#https://developers.arcgis.com/python/


from arcgis.gis import GIS

# Create an anonymous connection to ArcGIS Online
arcgis_online = GIS()
hurricane_pts = arcgis_online.content.search("Hurricane_tracks_points AND owner:atma.mani", "Feature Layer")[0]
hurricane_pts