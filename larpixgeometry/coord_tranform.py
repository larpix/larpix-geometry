# shift y
# switch xz
def swop_xz(x, y, z):
    return z, y, x

def shift_y(offset, x, y, z):
    return x, y - offset, z
