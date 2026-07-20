"""
UrbanTransit GTFS Builder MX
---------------------------------
Archivo:
project_loader.py

Descripción:
Localiza automáticamente todos los proyectos KML.
"""

from pathlib import Path


class ProjectLoader:

    def __init__(self, folder):

        self.folder = Path(folder)

    def get_kml_files(self):

        return sorted(

            self.folder.glob("*.kml")

        )