import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy_garden.mapview import MapView, MapMarker
from gmplot import gmplot

class GirlSafetyApp(App):
    def build(self):
        return MapLayout()

    def mark_unsafe_area(self):
        # Simulate marking an unsafe area at a fixed point
        mapview = self.root.ids.mapview
        unsafe_marker = MapMarker(lat=37.7749, lon=-122.4194)  # Dummy coordinates for unsafe area
        mapview.add_marker(unsafe_marker)

        # Add this data to the map plotting tool (gmplot) for future route suggestions
        gmap = gmplot.GoogleMapPlotter(37.7749, -122.4194, 13)
        gmap.marker(37.7749, -122.4194, color="red")  # Mark unsafe area
        gmap.draw("assets/map_data/safe_route_map.html")  # Save updated map

    def send_sos(self):
        # Dummy SOS functionality - In a real app, this would send GPS coordinates to emergency contacts
        print("SOS sent! Sharing location with contacts.")

class MapLayout(BoxLayout):
    pass

if __name__ == '__main__':
    GirlSafetyApp().run()
