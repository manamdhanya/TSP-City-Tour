import argparse, csv, json
from collections import namedtuple
from distance import distance_matrix
from tsp_solver import nearest_neighbor, two_opt, path_length

Place = namedtuple("Place", ["name", "lat", "lon"])

def read_csv(path):
    places = []
    with open(path, newline='', encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            name, lat, lon = row[0], float(row[1]), float(row[2])
            places.append(Place(name, lat, lon))
    return places

def export_geojson(places, path, roundtrip, out_file):
    coords = [[places[i].lon, places[i].lat] for i in path]
    if roundtrip:
        coords.append(coords[0])
    geojson = {
        "type": "FeatureCollection",
        "features": [{
            "type": "Feature",
            "geometry": {"type": "LineString", "coordinates": coords},
            "properties": {}
        }]
    }
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(geojson, f, indent=2)

def plot_route(places, path, roundtrip, save_png=None):
    import matplotlib.pyplot as plt

    lats = [places[i].lat for i in path]
    lons = [places[i].lon for i in path]
    plt.figure(figsize=(8, 6))

    plt.plot(lons, lats, 'bo-', color="blue")

    for i in range(len(path)-1):
        x1, y1 = places[path[i]].lon, places[path[i]].lat
        x2, y2 = places[path[i+1]].lon, places[path[i+1]].lat
        plt.annotate("", xy=(x2,y2), xytext=(x1,y1),
            arrowprops=dict(arrowstyle="->", color="blue", lw=1))

    if roundtrip:
        x1, y1 = places[path[-1]].lon, places[path[-1]].lat
        x2, y2 = places[path[0]].lon, places[path[0]].lat
        plt.annotate("", xy=(x2,y2), xytext=(x1,y1),
            arrowprops=dict(arrowstyle="->", color="blue", lw=1))

    for idx in path:
        plt.text(places[idx].lon, places[idx].lat, places[idx].name, fontsize=9)

    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.title("City Tour Route")
    plt.grid(True)

    if save_png:
        plt.savefig(save_png, dpi=180)
    else:
        plt.show()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", required=True)
    parser.add_argument("--start", default=None)
    parser.add_argument("--roundtrip", action="store_true",
                        help="Return to start point (make route a loop)")
    parser.add_argument("--algo", choices=["greedy","greedy-2opt"], default="greedy")
    parser.add_argument("--plot", action="store_true")
    parser.add_argument("--save-plot", default=None)
    parser.add_argument("--geojson", default="route.geojson")
    args = parser.parse_args()

    places = read_csv(args.csv)
    name_to_idx = {p.name:i for i,p in enumerate(places)}
    start_idx = 0 if args.start is None else name_to_idx[args.start]

    dist = distance_matrix(places)
    path = nearest_neighbor(dist, start=start_idx)
    if args.algo=="greedy-2opt":
        path = two_opt(path, dist)
    if args.roundtrip:
        path.append(path[0])

    total = path_length(path, dist)
    print("Optimal Path:", " -> ".join(places[i].name for i in path))
    print(f"Total Distance: {total:.2f} km")

    export_geojson(places, path, args.roundtrip, args.geojson)

    if args.plot or args.save_plot:
        plot_route(places, path, args.roundtrip, save_png=args.save_plot)

if __name__=="__main__":
    main()
