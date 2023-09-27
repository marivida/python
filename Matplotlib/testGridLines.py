# https://www.w3schools.com/python/matplotlib_grid.asp


# # With Pyplot, you can use the grid() function to add grid lines to the plot.
# # Example: Add grid lines to the plot:
# import numpy as np
# import matplotlib.pyplot as plt
# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
# plt.title("Sports Watch Data")
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")
# plt.plot(x, y)
# plt.grid()
# plt.show()


# # You can use the axis parameter in the grid() function to specify which grid lines to display.
# # Legal values are: 'x', 'y', and 'both'. Default value is 'both'.
# # Example: Display only grid lines for the x-axis:
# import numpy as np
# import matplotlib.pyplot as plt
# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
# plt.title("Sports Watch Data")
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")
# plt.plot(x, y)
# plt.grid(axis = 'x') # apenas linhas do eixo x, verticais. opções: x, y e both(default)
# plt.show()


# You can also set the line properties of the grid, like this: grid(color = 'color', linestyle = 'linestyle', linewidth = number).
# Example: Set the line properties of the grid:
import numpy as np
import matplotlib.pyplot as plt
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.plot(x, y)
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5) # linhas do frid verdes, tracejadas com largura 0.5
plt.show()