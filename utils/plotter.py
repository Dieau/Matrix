import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from linear_algebra.vector import Vector
from linear_algebra.matrix import Matrix

class Plotter:
    @staticmethod
    def plot_vector(vectors, labels=None, colors=None, title="Vector Plot"):
        """Plot 2D or 3D vectors with distinct colors and dynamic plot size"""
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d' if len(vectors[0].data) == 3 else None)
        
        max_magnitude = max(max(abs(coord) for coord in vector.data) for vector in vectors)
        plot_limit = max_magnitude * 1.2
        
        for i, vector in enumerate(vectors):
            label = labels[i] if labels else f"Vector {i+1}"
            color = colors[i] if colors else None
            if len(vector.data) == 2:
                ax.quiver(0, 0, vector.data[0], vector.data[1], angles='xy', scale_units='xy', scale=1, label=label, color=color)
            elif len(vector.data) == 3:
                ax.quiver(0, 0, 0, vector.data[0], vector.data[1], vector.data[2], label=label, color=color)
            else:
                raise ValueError("Only 2D and 3D vectors can be plotted")
        
        ax.set_xlim([-plot_limit, plot_limit])
        ax.set_ylim([-plot_limit, plot_limit])
        if len(vectors[0].data) == 3:
            ax.set_zlim([-plot_limit, plot_limit])
        
        ax.set_title(title)
        ax.legend()
        fig.text(0.5, 0.01, "Press Enter to proceed...", ha="center", fontsize=10, color="gray")
        return fig
    
    @staticmethod
    def plot_angle_between_vectors(v1: Vector, v2: Vector, angle_cos: float, title="Angle Between Vectors"):
        """Plot two vectors and display the angle between them"""
        import numpy as np
        import matplotlib.pyplot as plt
        from matplotlib.patches import Arc

        angle = np.degrees(np.arccos(angle_cos))

        fig = plt.figure()
        ax = fig.add_subplot(111)
        
        ax.quiver(0, 0, v1.data[0], v1.data[1], angles='xy', scale_units='xy', scale=1, color='red', label="v1")
        ax.quiver(0, 0, v2.data[0], v2.data[1], angles='xy', scale_units='xy', scale=1, color='blue', label="v2")
        
        max_magnitude = max(max(abs(coord) for coord in v1.data), max(abs(coord) for coord in v2.data))
        plot_limit = max_magnitude * 1.2
        ax.set_xlim([-plot_limit, plot_limit])
        ax.set_ylim([-plot_limit, plot_limit])
        
        arc_radius = max_magnitude * 0.2
        arc = Arc((0, 0), 2 * arc_radius, 2 * arc_radius, theta1=0, theta2=angle, color="green", lw=2)
        ax.add_patch(arc)
        
        text_radius = arc_radius * 1.3
        angle_text_x = text_radius * np.cos(np.radians(angle / 2))
        angle_text_y = text_radius * np.sin(np.radians(angle / 2))
        ax.text(angle_text_x, angle_text_y, f"{angle:.2f}°", fontsize=12, color="green", ha="center")
        
        ax.set_title(title)
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.legend()
        fig.text(0.5, 0.01, "Press Enter to proceed...", ha="center", fontsize=10, color="gray")
        
        return fig

    @staticmethod
    def plot_matrix(matrix, title="Matrix Plot", max_value=None):
        """Plot a matrix as a 3D bar graph with fixed z-axis limits"""
        import numpy as np
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        
        rows, cols = len(matrix.data), len(matrix.data[0])
        xpos, ypos = np.meshgrid(np.arange(cols), np.arange(rows))
        xpos = xpos.flatten()
        ypos = ypos.flatten()
        zpos = np.zeros_like(xpos)
        
        dx = dy = np.ones_like(zpos) * 0.5
        dz = np.array(matrix.data).flatten()
        
        if max_value:
            dz = dz / max_value
        
        ax.bar3d(xpos, ypos, zpos, dx, dy, dz, shade=True)
        ax.set_title(title)
        ax.set_xlabel("Columns")
        ax.set_ylabel("Rows")
        ax.set_zlabel("Values")
        
        if max_value:
            ax.set_zlim(0, 1)
        else:
            ax.set_zlim(0, max(dz))
        
        return fig

    @staticmethod
    def wait_for_next(fig):
        """Wait for user to press Enter in the plot window to proceed"""
        def on_key(event):
            if event.key == "enter":
                plt.close(fig)

        fig.canvas.mpl_connect("key_press_event", on_key)
        plt.show()
        
    @staticmethod
    def plot_matrix_wireframe(matrix, title="Matrix Wireframe Plot"):
        """Plot a matrix as a 3D wireframe plot"""
        import numpy as np
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        
        rows, cols = len(matrix.data), len(matrix.data[0])
        
        x = np.arange(cols)
        y = np.arange(rows)
        X, Y = np.meshgrid(x, y)
        Z = np.array(matrix.data)
        
        ax.plot_wireframe(X, Y, Z, color='blue')
        
        ax.set_title(title)
        ax.set_xlabel("Columns")
        ax.set_ylabel("Rows")
        ax.set_zlabel("Values")
        
        fig.text(0.5, 0.01, "Press Enter to proceed...", ha="center", fontsize=10, color="gray")
        
        return fig