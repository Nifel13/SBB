import folium
from folium import plugins
from traductor_coords import trans_coords

def plot_route_leaflet(start_coordinates, end_coordinates):
    # Create a map centered at the starting coordinates
    my_map = folium.Map(location=start_coordinates, zoom_start=12)

    # Add markers for the starting and ending points
    folium.Marker(location=start_coordinates, popup='Inicio', icon=folium.Icon(color='green')).add_to(my_map)
    folium.Marker(location=end_coordinates, popup='Fin', icon=folium.Icon(color='red')).add_to(my_map)

    # Add Leaflet Routing Machine to the map
    folium.plugins.LocateControl().add_to(my_map)

    # Display the map
    my_map.save('ruta_leaflet.html')  # Save the map as an HTML file
    my_map

# Example coordinates for start and end points in Switzerland
start_coordinates_switzerland = [47.3769, 8.5417]  # Zurich
end_coordinates_switzerland = [46.8182, 8.2275]    # Center of Switzerland (fictional point)
start_station_id = trans_coords(str(start_coordinates_switzerland[1]), str(start_coordinates_switzerland[0]))
end_station_id = trans_coords(str(end_coordinates_switzerland[1]), str(end_coordinates_switzerland[0]))

# Plot the route using Leaflet
plot_route_leaflet(start_coordinates_switzerland, end_coordinates_switzerland)
