def load_geom_dict(json_path):
    with open(json_path, "r") as f_geom_dict:
        geom_dict = json.load(f_geom_dict)

    return geom_dict
