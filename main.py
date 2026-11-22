import json
import os

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy_garden.mapview import MapMarker, MapView


class GibddMapApp(App):
    title = "ГИБДД на карте"

    def build(self):
        self.file = os.path.join(self.user_data_dir, "posts.json")
        self.markers = []

        root = FloatLayout()
        self.map = MapView(lat=55.7558, lon=37.6173, zoom=11)  # Москва
        root.add_widget(self.map)

        # прицел в центре карты
        root.add_widget(Label(text="+", font_size="40sp",
                              size_hint=(None, None), size=(60, 60),
                              pos_hint={"center_x": .5, "center_y": .5}))

        bar = BoxLayout(size_hint=(1, None), height=120,
                        pos_hint={"x": 0, "y": 0}, spacing=10, padding=10)
        bar.add_widget(Button(text="+ Пост ГИБДД", on_release=self.add_post))
        bar.add_widget(Button(text="Удалить последний", on_release=self.undo))
        root.add_widget(bar)

        self.load()
        return root

    def add_post(self, *_):
        self._put(self.map.lat, self.map.lon)
        self.save()

    def undo(self, *_):
        if self.markers:
            self.map.remove_marker(self.markers.pop())
            self.save()

    def _put(self, lat, lon):
        m = MapMarker(lat=lat, lon=lon)
        self.map.add_marker(m)
        self.markers.append(m)

    def save(self):
        data = [[m.lat, m.lon] for m in self.markers]
        with open(self.file, "w") as f:
            json.dump(data, f)

    def load(self):
        if os.path.exists(self.file):
            with open(self.file) as f:
                for lat, lon in json.load(f):
                    self._put(lat, lon)


if __name__ == "__main__":
    GibddMapApp().run()
