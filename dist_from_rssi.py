from math import pow

# n = 4.31851
n = 4.0

def dist_from_rssi(rssi, n, A):
  # RSSI = -(A + 10 * n * log_10(d))
  # n = path loss exponent (between 2 and 4 usually)
  # A = RSSI at 1 meter
  # d = distance
  

  div = -((rssi - A) / (10 * n))

  d = pow(10, div)
  return d

if __name__ == '__main__':
  # rssis = [-65, -52, -72, -61] # 1, 0.5, 2, 0.8ish
  # expected_distances = [1.0, 0.5, 2.0, 0.8]

  # # galileo 1
  # A = -65 # get RSSI value at 1 meter
  # rssis = [-65, -88, -84]
  # expected_distances = [1.0, 3.81, 3.58]

  # galileo 4
  # A = -72
  # rssis = [-72, -85, -81]
  # expected_distances = [1.0, 3.51, 3.61]

  # galileo 2
  A = -80
  rssis = [-84, -80, -74]
  expected_distances = [3.78, 1.0, 3.43]
  for i in range(len(rssis)):
    print 'rssi: {}'.format(rssis[i])
    d = dist_from_rssi(rssis[i], n, A)
    error = ((d - expected_distances[i]) / expected_distances[i]) * 100
    print 'expected distance: {:.4f}'.format(expected_distances[i])
    print 'distance: {:.4f}'.format(d)
    print 'error: {:.4f} %'.format(error)
    print '---'
