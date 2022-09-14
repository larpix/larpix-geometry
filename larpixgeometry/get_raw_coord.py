# xy and z
import numpy as np

def get_data_packets(packets):
    mask = packets['packet_type'] == 0
    packets_arr = packets.data[mask]
    return packets_arr

def get_pixel_plane_position(packets_arr, geom_dict):

    xyz = geom_dict[packets_arr['io_group'], packets_arr['io_channel'], packets_arr['chip_id'], packets_arr['channel_id']]
    x = xyz[:, 0]
    y = xyz[:, 1]
    z = xyz[:, 2]
    direction = yz[:, 3]
    return x, y, z, direction

def get_drift_time(packets, geom_dict):
    return t_drift

# get v_drift
def get_drift_position(z_anode, direction, t_drift):
    z = z_anode + direction * t_drift * v_drift
    return z
