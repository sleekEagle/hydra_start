import hydra
from omegaconf import DictConfig, OmegaConf
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


def plot_cuboid(length, width, height):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Define the eight vertices of the cuboid
    vertices = [(0, 0, 0),
                (length, 0, 0),
                (length, width, 0),
                (0, width, 0),
                (0, 0, height),
                (length, 0, height),
                (length, width, height),
                (0, width, height)]

    # Define the six faces of the cuboid
    faces = [[vertices[j] for j in [0, 1, 2, 3]],
             [vertices[j] for j in [4, 5, 6, 7]], 
             [vertices[j] for j in [0, 3, 7, 4]],
             [vertices[j] for j in [1, 2, 6, 5]],
             [vertices[j] for j in [0, 1, 5, 4]],
             [vertices[j] for j in [2, 3, 7, 6]]]

    # Plot the cuboid
    ax.add_collection3d(Poly3DCollection(faces, facecolors='cyan', linewidths=1, edgecolors='r', alpha=0.5))

    # Set labels and title
    ax.set_xlabel('width')
    ax.set_ylabel('length')
    ax.set_zlabel('height')
    ax.set_title('Cuboid Plot')

    plt.show()


def calc_volume(width,length,height,plot):
    vol=width*length*height
    print(f"Volume is {vol:.3f}")
    if plot:
        plot_cuboid(width,length,height)


@hydra.main(version_base=None, config_path="conf", config_name="config")
def my_app(conf : DictConfig) -> None:
    print(OmegaConf.to_yaml(conf))
    calc_volume(conf.width,conf.length,conf.height,conf.plot)

if __name__ == "__main__":
    my_app()