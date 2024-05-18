import folium
import geopandas as gpd
import osmnx as ox

def mapWithCompetitors(center_lat, center_lng, radius, business_type):
    
    #Create the map
    m = folium.Map(location=[center_lat, center_lng], zoom_start=18)
    #Add a marker at the center
    folium.Marker(location=[center_lat, center_lng], popup='Center').add_to(m)

    #Circle specified the radius
    folium.Circle(location=[center_lat, center_lng],
                  radius=radius,
                  color='light_blue',
                  fill=True,
                  fill_color='blue').add_to(m)

    # Fetch OSM data
    point = (center_lat, center_lng)
    gdf = ox.geometries.geometries_from_point(point, tags={'amenity': business_type}, dist=radius)
    gdf_pois = gdf[gdf.geometry.type == 'Point']

    # ompetitor
    for idx, poi in gdf_pois.iterrows():
        folium.CircleMarker(
            location=[poi.geometry.y, poi.geometry.x],
            radius=2,
            color='red',
            fill=True,
            fill_color='red',
            popup=poi.get('name', 'No name')
        ).add_to(m)

    #Save the map to HTML file
    m.save('radius_map_with_competitors.html')

    #Display the map
    return m
