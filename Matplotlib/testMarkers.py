# lista com todos os markers: https://www.w3schools.com/python/matplotlib_markers.asp


# # You can use the keyword argument marker to emphasize each point with a specified marker:
# # Example: Mark each point with a circle:
# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([3, 8, 1, 10])
# # plt.plot(ypoints, marker = 'o') # bolinha
# plt.plot(ypoints, marker = '*') #estrelinha
# plt.show()


# '''You can also use the shortcut string notation parameter to specify the marker.
# This parameter is also called fmt, and is written with this syntax:
# marker|line|color'''
# # Example: Mark each point with a circle:
# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([3, 8, 1, 10])
# # plt.plot(ypoints, 'o:r') # circulos nas pontas com linha pontilhada vermelha
# # plt.plot(ypoints, '.-b') # pontos nas pontas com linha solida azu
# plt.plot(ypoints, 'v--g') # triangulos nas pontas com linha tracejada verde
# plt.show()


# # You can use the keyword argument markersize or the shorter version, ms to set the size of the markers:
# # Example: Set the size of the markers to 20:
# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, marker = 'o', ms = 20)
# plt.show()


# # You can use the keyword argument markeredgecolor or the shorter mec to set the color of the edge of the markers:
# # Example: Set the EDGE color to red:
# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
# plt.show()


# #You can use the keyword argument markerfacecolor or the shorter mfc to set the color inside the edge of the markers:
# # Example: Set the FACE color to red:
# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')
# plt.show()


# # Use both the mec and mfc arguments to color the entire marker:
# # Example: Set the color of both the edge and the face to red:
# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r', mfc = 'r')
# plt.show()


'''You can also use Hexadecimal color values:
Example: Mark each point with a beautiful green color:'''
import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, marker = 'o', ms = 20, mec = '#4CAF50', mfc = '#4CAF50')
# Or any of the 140 supported color names.
plt.plot(ypoints, marker = 'o', ms = 20, mec = 'hotpink', mfc = 'hotpink')
plt.show()