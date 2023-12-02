import folium
from folium import plugins

def plot_route_leaflet(start_coordinates, end_coordinates):
    # Crear un mapa centrado en las coordenadas del punto de inicio
    my_map = folium.Map(location=start_coordinates, zoom_start=12)

    # Agregar marcadores para los puntos de inicio y fin
    folium.Marker(location=start_coordinates, popup='Inicio', icon=folium.Icon(color='green')).add_to(my_map)
    folium.Marker(location=end_coordinates, popup='Fin', icon=folium.Icon(color='red')).add_to(my_map)

    # Configurar el servicio de enrutamiento
    routing = plugins.Routing(service='openrouteservice', waypoints=[start_coordinates, end_coordinates])

    # Agregar el servicio de enrutamiento al mapa
    routing.add_to(my_map)

    # Mostrar el mapa
    my_map.save('ruta_leaflet.html')  # Guardar el mapa como un archivo HTML
    my_map

# Coordenadas de inicio y fin en Suiza (puedes ajustar según tus ubicaciones)
start_coordinates_switzerland = [47.3769, 8.5417]  # Zurich
end_coordinates_switzerland = [46.8182, 8.2275]    # Centro de Suiza (punto ficticio)

# Trazar la ruta utilizando Leaflet y el servicio de enrutamiento de OpenRouteService
plot_route_leaflet(start_coordinates_switzerland, end_coordinates_switzerland)
