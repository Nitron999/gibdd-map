import json
import os
import tkinter as tk

import tkintermapview

FILE = os.path.join(os.path.expanduser("~"), "gibdd_posts.json")

root = tk.Tk()
root.title("ГИБДД на карте")
root.geometry("1000x700")

map_widget = tkintermapview.TkinterMapView(root, corner_radius=0)
map_widget.pack(fill="both", expand=True)
map_widget.set_position(55.7558, 37.6173)  # Москва
map_widget.set_zoom(11)

markers = []


def save():
    with open(FILE, "w") as f:
        json.dump([m.position for m in markers], f)


def add_post(coords):
    markers.append(map_widget.set_marker(coords[0], coords[1], text="ГИБДД"))
    save()


def undo():
    if markers:
        markers.pop().delete()
        save()


map_widget.add_right_click_menu_command(
    label="Добавить пост ГИБДД", command=add_post, pass_coords=True)

bar = tk.Frame(root)
bar.pack(fill="x")
tk.Button(bar, text="Удалить последний", command=undo).pack(side="left", padx=5, pady=5)
tk.Label(bar, text="Правая кнопка мыши по карте → Добавить пост").pack(side="left", padx=10)

if os.path.exists(FILE):
    with open(FILE) as f:
        for lat, lon in json.load(f):
            markers.append(map_widget.set_marker(lat, lon, text="ГИБДД"))

root.mainloop()
