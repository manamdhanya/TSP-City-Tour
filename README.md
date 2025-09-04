# TSP City Tour

An interactive **Travelling Salesman Problem (TSP)** solver for planning city tours.  
It finds the shortest possible route that visits all places exactly once and returns to the starting point (optional).  

Supports plotting routes on a map and exporting them as **GeoJSON** for use in mapping tools.  

## 🚀 Features
- Read places (name, latitude, longitude) from a CSV file  
- Choose starting location  
- Optional round trip (return to start)  
- Algorithms:
  - Greedy (Nearest Neighbor)  
  - Greedy + 2-opt (local optimization)  
- Export route as **GeoJSON**  
- Plot route using **Matplotlib**  

## 📂 Project Structure
```

TSP-City-Tour/
├── tsp.py             # Main entry script
├── tsp\_solver.py      # TSP algorithms (Nearest Neighbor, 2-opt, path length)
├── distance.py        # Distance matrix calculations (Haversine formula)
├── places\_sample.csv  # Example places dataset
├── README.md          # Project documentation
├── .gitignore         # Git ignore file

````

## 📊 Example Usage

Run with **Greedy Algorithm**:
```bash
python tsp.py --csv places_sample.csv --start "Eiffel Tower" --algo greedy --plot
````

Run with **Greedy + 2-opt optimization** and round trip:

```bash
python tsp.py --csv places_sample.csv --start "Eiffel Tower" --algo greedy-2opt --roundtrip --plot
```

Export route as **GeoJSON**:

```bash
python tsp.py --csv places_sample.csv --start "Eiffel Tower" --algo greedy-2opt --geojson route.geojson
```

## 📝 CSV Format

Your input file should look like this:

```csv
Eiffel Tower,48.8584,2.2945
Louvre Museum,48.8606,2.3376
Notre Dame,48.8530,2.3499
Arc de Triomphe,48.8738,2.2950
```

**Format:**

```
Place Name, Latitude, Longitude
```

## 📦 Dependencies

Install required libraries:

```bash
pip install matplotlib
```
