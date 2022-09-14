import yaml
import json
from collections import defaultdict

def rotate_pixel(pixel_pos, tile_orientation):
    return pixel_pos[0]*tile_orientation[2], pixel_pos[1]*tile_orientation[1]

def multi_layout_to_dict(yaml_path, json_path):

    with open(yaml_path) as gf:
        geometry_yaml = yaml.load(gf, Loader=yaml.FullLoader)

    pixel_pitch = geometry_yaml['pixel_pitch']
    chip_channel_to_position = geometry_yaml['chip_channel_to_position']
    tile_orientations = geometry_yaml['tile_orientations']
    tile_positions = geometry_yaml['tile_positions']
    tpc_centers = geometry_yaml['tpc_centers']
    tile_indeces = geometry_yaml['tile_indeces']
    xs = np.array(list(chip_channel_to_position.values()))[
        :, 0] * pixel_pitch
    ys = np.array(list(chip_channel_to_position.values()))[
        :, 1] * pixel_pitch
    x_size = max(xs) - min(xs) + pixel_pitch
    y_size = max(ys) - min(ys) + pixel_pitch

#    tile_geometry = defaultdict(int)
    geometry = defaultdict(lambda: (0,0))
    io_group_io_channel_to_tile = {}

    for tile in geometry_yaml['tile_chip_to_io']:
        tile_orientation = tile_orientations[tile]
        for chip in geometry_yaml['tile_chip_to_io'][tile]:
            io_group_io_channel = geometry_yaml['tile_chip_to_io'][tile][chip]
            io_group = io_group_io_channel // 1000
            io_channel = io_group_io_channel % 1000
            self._tile_id[([io_group], [io_channel])] = tile

        for chip_channel in geometry_yaml['chip_channel_to_position']:
            chip = chip_channel // 1000
            channel = chip_channel % 1000
            try:
                io_group_io_channel = geometry_yaml['tile_chip_to_io'][tile][chip]
            except KeyError:
                continue

            io_group = io_group_io_channel // 1000
            io_channel = io_group_io_channel % 1000
            x = chip_channel_to_position[chip_channel][0] * \
                self.pixel_pitch + self.pixel_pitch / 2 - x_size / 2
            y = chip_channel_to_position[chip_channel][1] * \
                self.pixel_pitch + self.pixel_pitch / 2 - y_size / 2

            x, y = rotate_pixel((x, y), tile_orientation)
            x += tile_positions[tile][2] + \
                tpc_centers[tile_indeces[tile][1]][0]
            y += tile_positions[tile][1] + \
                tpc_centers[tile_indeces[tile][1]][1]

            z = tile_positions[tile][0] + \
                tpc_centers[tile_indeces[tile][1]][2]
            direction = tile_orientations[tile][0]

            geometry[(io_group, io_channel, chip, channel)] = np.array([x, y, z, direction])

            
    with open(json_path, "w") as outfile:
        json.dump(dict(geometry), outfile)

