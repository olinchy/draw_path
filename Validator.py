from frechet_distance import frechetDist


def validate(paths):
    if len(paths) >= 2:
        p = paths[0].xy()
        q = paths[1].xy()
        c = frechetDist(p, q)
        return "paths not match"
    else:
        return 'not enough paths to compare'
