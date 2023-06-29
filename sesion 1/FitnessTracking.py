import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# Make data
rng = np.random.default_rng()
xs = [20,50,320]
ys = [4120,52,305]
zs = [50,60,456]

# Plot
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.scatter(xs, ys, zs)

ax.set(xticklabels=[],
       yticklabels=[],
       zticklabels=[])

plt.show()
