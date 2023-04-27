def normalize_dataset(ds, mm_scale=1, pix_scale=1, dt=1, d=1, U_theo=1):
    """ Normalizes dataset and returns its dimensionless copy """
    dsn = ds.copy()
    dsn['u'] = ds['u']*mm_scale/pix_scale
    dsn['v'] = ds['v']*mm_scale/pix_scale
    dsn['u'] = dsn['u'] / dt
    dsn['v'] = dsn['v'] / dt

    dsn['x'] = ds['x']*mm_scale/pix_scale / d # in mm, so it's now dimensionless
    dsn['y'] = ds['y']*mm_scale/pix_scale / d 


    # some convention for the cylinder case that we want to see left to right
    # with the cylinder on the left side at x=0, y=0
    # turn to the 
    
    # not in April 23, only in Feb. 15
    # in April we already used the under-channel mirror at 45 deg. 
    # dsn['x'] = dsn['x'].max() - dsn['x']

    # make y = 0 in the middle
    middle = dsn['y'].max()/2
    dsn['y'] = dsn['y'] - middle

    # turn the flow from left to right
    # Not in April 23
    # dsn['u'] = -1*dsn['u']

    # normalize the velocity by some average flow rate value
    dsn['u'] = dsn['u'] / U_theo
    dsn['v'] = dsn['v'] / U_theo
    
    
    dsn.attrs['dt'] = dt
    dsn.attrs['mm_scale'] = mm_scale
    dsn.attrs['pix_scale'] = pix_scale
    dsn.attrs['d'] = d
    dsn.attrs['U_theo'] = U_theo
    
    return dsn