# 🚍 UrbanTransit GTFS Builder MX

> **Transforming geographic information into open public transport data.**

UrbanTransit GTFS Builder MX is an open-source toolkit that converts geographic route data (KML) into valid GTFS feeds ready for publication on Google Maps and other transit platforms.

Designed to help municipalities, universities, consultants and transit agencies publish public transport information quickly and consistently.

---

# 🌎 Mission

Promote open mobility data by making GTFS generation accessible to everyone, regardless of technical experience.

---

# ✨ Features

- ✅ Automatic KML parsing
- ✅ Automatic stop detection
- ✅ Automatic route detection
- ✅ Route-to-stop matching
- ✅ Side-of-road validation
- ✅ Distance calculation along the route
- ✅ Automatic travel time estimation
- ✅ GTFS schedule generation
- ✅ Automatic ZIP export
- ✅ Automatic project detection
- ✅ Multi-project processing
- ✅ GTFS Validator compatible

---

# 📦 Generated GTFS files

The program automatically generates:

- agency.txt
- calendar.txt
- feed_info.txt
- routes.txt
- shapes.txt
- stop_times.txt
- stops.txt
- trips.txt

Each project is exported as an independent GTFS ZIP.

Example:

```
Ruta001.kml

↓

Ruta001-GTFS.zip
```

---

# 🚀 Usage

Place one or more KML files inside:

```
data/kml/
```

Run:

```bash
py -m gtfs_builder.build_gtfs
```

UrbanTransit GTFS Builder MX will automatically detect every project and generate one GTFS feed for each.

---

# 📂 Project Structure

```text
urbantransit-gtfs-builder-mx/

├── archives/
├── data/
│   └── kml/
├── output/
├── gtfs_builder/
│   ├── build_gtfs.py
│   ├── parser.py
│   ├── validator.py
│   ├── route_matcher.py
│   ├── geometry.py
│   ├── time_engine.py
│   ├── trip_generator.py
│   ├── schedule_generator.py
│   ├── exporter.py
│   ├── project_loader.py
│   ├── models.py
│   ├── config.py
│   └── ui.py
│
└── README.md
```

---

# 📈 Project Status

## Version 0.8

### Completed

- ✅ Automatic KML parser
- ✅ Route matching engine
- ✅ Time Engine
- ✅ GTFS generation
- ✅ GTFS validation
- ✅ Automatic ZIP export
- ✅ Automatic project detection
- ✅ Console optimization
- ✅ Modular architecture

---

# 🛣️ Roadmap

## v0.9

- Multiple speed profiles
- Frequency generation
- Better geometry projection
- Automatic service generation

## v1.0

- Graphical User Interface (GUI)
- Configuration editor
- Complete documentation
- Stable production release

---

# 🤝 Contributing

Contributions are welcome.

If you'd like to improve the project, feel free to open an Issue or submit a Pull Request.

---

# 📄 License

MIT License

---

# 👷 Author

**Arq. Eduardo Tovar Gómez**

Open-source project created to improve public transportation data in Mexico.

GitHub:

https://github.com/EduardoTovarGomez/urbantransit-gtfs-builder-mx

---

## 🇲🇽 Designed in Mexico

Built with passion to make public transport more visible, accessible and open.