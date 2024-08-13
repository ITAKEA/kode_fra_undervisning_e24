
def draw_line(f):
    import matplotlib.pyplot as plt
    import numpy as np

    x = np.linspace(-10, 10, 100)
    y = f(x)

    fig, ax = plt.subplots()

    ax.plot(x, y)

    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')

    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    plt.xticks(range(-10, 11, 2))
    plt.yticks(range(-40, 61, 10))

    plt.grid(True)
    plt.show()


def draw_vector(vector):
    """
        param: vector of datatype list, with x and y values
    """
    import matplotlib.pyplot as plt
    import numpy as np
    # Create a figure and axis
    fig, ax = plt.subplots()

    # Define the origin of the vector
    origin = [0, 0]

    # Plot the origin
    ax.scatter(origin[0], origin[1])

    # Plot the vector
    ax.quiver(origin[0], origin[1], vector[0], vector[1], angles='xy', scale_units='xy', scale=1, color='r')

    # Set the limits of the plot to the size of the vector
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)

    # Set the aspect ratio to 'equal' to ensure the vector is drawn correctly
    ax.set_aspect('equal')

    # Move the x and y axis to go through the origin
    ax.spines['left'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('center')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    # Show the plot
    plt.show()


def draw_3d_vector(vector):
    import matplotlib.pyplot as plt
    #from mpl_toolkits.mplot3d import Axes3D
    import numpy as np

    # Create a figure and a 3D axis
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Define the origin of the vector
    origin = [0, 0, 0]

    # Plot the origin
    ax.scatter(origin[0], origin[1], origin[2])

    # Plot the vector
    ax.quiver(origin[0], origin[1], origin[2], vector[0], vector[1], vector[2], color='r')

    # Set the limits of the plot to the size of the vector
    ax.set_xlim(-6, 6)
    ax.set_ylim(-6, 6)
    ax.set_zlim(-6, 6)

    # Create grids for x, y, and z axes
    ax.grid(True)

    # Show the x, y, and z axes
    ax.xaxis.set_tick_params(labelsize=10)
    ax.yaxis.set_tick_params(labelsize=10)
    ax.zaxis.set_tick_params(labelsize=10)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Plot lines through the origin
    ax.plot([0, 0], [0, 0], [-6, 6], color='k', lw=0.5)  # z-axis
    ax.plot([-6, 6], [0, 0], [0, 0], color='k', lw=0.5)  # x-axis
    ax.plot([0, 0], [-6, 6], [0, 0], color='k', lw=0.5)  # y-axis

    # Show the plot
    plt.show()