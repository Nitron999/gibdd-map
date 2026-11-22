[app]
title = GIBDD Map
package.name = gibddmap
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,json
version = 0.1
requirements = python3,kivy==2.3.0,kivy_garden.mapview,requests,urllib3,idna,chardet,certifi
orientation = portrait
android.permissions = INTERNET
android.api = 33
android.minapi = 24
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
