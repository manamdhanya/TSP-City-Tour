import math

def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
    return R * 2*math.atan2(math.sqrt(a), math.sqrt(1-a))

def distance_matrix(places):
    n = len(places)
    dist = [[0.0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            d = haversine(places[i].lat, places[i].lon, places[j].lat, places[j].lon)
            dist[i][j] = dist[j][i] = d
    return dist
