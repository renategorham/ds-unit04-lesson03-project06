'''Data Maker
#*****************************************************************************
#Makes radnom data with outliers, based on a normal distribution
'''

import numpy as np 

def go(m = 10, n = 3, m_o = 5, n_o = 3, 
       mu_seed = 1.0, sd_seed = 0.5, dist_seed = 0.1, 
       out_diff = 3.0):
    '''Function to create a random data set with contaminated data. 
        'm' is the number of rows or data items.
        'n' is the number of columns of features in the data set.
        'm_o' is the number of outliers (or comtaminated points).
        'n_o' is the number of contamianted features.
        'mu_seed' is the seed location for the feature distributions.
        'sd_seed' is the seed scale for the feature distributions.
        'dist_seed' is the seed location for distribution variation.
        'out_diff' is the distance of outliers from non-contamianted features.'''
    in_loc = []
    in_scale = []
    out_loc = []
    out_scale = []

    if n >= n_o:
        #uncontaminated features
        for i in range(n):
            in_mu = mu_seed + (np.random.normal(dist_seed) * i)
            in_sd = np.abs(sd_seed / in_mu)

            in_loc.append(in_mu)
            in_scale.append(in_sd)

        #contaminated features where the number contaminated is equal
        #to the number of features
        for j in range(n_o):
            out_mu = mu_seed + out_diff + (np.random.normal(dist_seed) * j)
            out_sd = np.abs(sd_seed / out_mu)

            out_loc.append(out_mu)
            out_scale.append(out_sd)

        #contamianted features wheret he number contaminated is less 
        #than the total number of features
        for k in range(n - n_o):
            out_mu = in_loc[k]
            out_sd = np.abs(sd_seed / out_mu)

            out_loc.insert(k, out_mu)
            out_scale.insert(k, out_sd)
    
    else:
        print('The number of contamianted features must be less than'+
              ' the number of total features.')
    

    #create the distributions
    x_in = np.random.normal(loc=in_loc, scale=in_scale, size=[m,n])
    x_out = np.random.normal(loc=out_loc, scale=out_scale, size=[m_o,n])

    #create the labels
    y_in = np.zeros([m,1])
    y_out = np.ones([m_o,1])

    #stack the distributions on the labels
    y = np.vstack((y_in, y_out))
    x = np.vstack((x_in, x_out))

    return(x, y)