import matplotlib.pyplot as plt
import numpy as np

dim3_physically_contigous = np.array([64140])

dmin_3_physically_contigous = sum(dim3_physically_contigous)

dim3_regular = np.array([46518])

dmin_3_regular = sum(dim3_regular)

dim6_contigous = np.array([int(x) for x in """159185
       95485""".replace('       ',',').replace('\n','').split(",")])

dim_6_contigous = sum(dim6_contigous)

dim6_regular = np.array([int(x) for x in """137015
       89117""".replace('       ',',').replace('\n','').split(",")])

dim_6_regular = sum(dim6_regular)

dim40_contigous = np.array([int(x) for x in """140262
      156781
      156217
      155686
      139859
      80438""".replace('      ',',').replace('\n','').split(",")])

dim_40_contigous = sum(dim40_contigous)

dim40_regular = np.array([int(x) for x in """121530
      144628
      154478
      143992
      148316
      86682""".replace('      ',',').replace('\n','').split(",")])

dim_40_regular = sum(dim40_regular)

# dimentions = ("3-dementions", "6-dementions", "40-dementions")
# comparitors = {
#     'FAT-Pointer based range address': (dmin_3_physically_contigous, dim_6_contigous, dim_40_contigous),
#     'System Allocator': (dmin_3_regular, dim_6_regular, dim_40_regular),
# }

# x = np.arange(len(dimentions))  # the label locations
# width = 0.25  # the width of the bars
# multiplier = 0

# fig, ax = plt.subplots(layout='constrained')

# for attribute, measurement in comparitors.items():
#     offset = width * multiplier
#     rects = ax.bar(x + offset, measurement, width, label=attribute)
#     ax.bar_label(rects, padding=3)
#     multiplier += 1

# # Add some text for labels, title and custom x-axis tick labels, etc.
# ax.set_ylabel('DTLB L1 reads')
# ax.set_title('L1D_TLB')
# ax.set_xticks(x + width, dimentions)
# ax.legend(loc='upper left', ncols=2)
# ax.set_ylim(0, 250)

# plt.show()

# Sample data
categories = ['Size Small', 'Size Medium', 'Size Large']
group_1 = [dmin_3_physically_contigous, dim_6_contigous, dim_40_contigous]
group_2 = [dmin_3_regular, dim_6_regular, dim_40_regular]

# Number of categories
n = len(categories)

# Create a bar width
bar_width = 0.25

# Create an array with the positions of the bars on the x-axis
r1 = np.arange(n)
r2 = [x + bar_width for x in r1]
# r3 = [x + bar_width for x in r2]

# Create the grouped bar graph
plt.bar(r1, group_1, color='b', width=bar_width, edgecolor='grey', label='FAT-Pointer based range based addresses')
plt.bar(r2, group_2, color='g', width=bar_width, edgecolor='grey', label='System memory allocator')
# plt.bar(r3, group_3, color='r', width=bar_width, edgecolor='grey', label='Group 3')

# Add xticks on the middle of the grouped bars
plt.xlabel('Size of Histogram COZ', fontweight='bold')
plt.xticks([r + bar_width for r in range(n)], categories)

# Add labels and title
plt.ylabel('DTLB L2 reads', fontweight='bold')
plt.title('Sum of DTLB L2 reads')

# Add a legend
plt.legend()

# Show the plot
# plt.show()
plt.savefig('l2-tlb-Histogram.png')