# add charge

def packets_position_parser(packets, geom_dict):
    packets_arr = get_data_packets(packets)
    x, y, z_anode, direction = get_pixel_plane_position(packets_arr, geom_dict)
    t_drift = get_drift_time(packets_arr)
    z = get_drift_position(z_anode, direction, t_drift)
    
    x, y, z = swop_xz(x, y, z)
    x, y, z = shift_y(offset, x, y, z)
    return x, y, z
