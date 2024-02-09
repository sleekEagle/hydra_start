import hydra
from omegaconf import DictConfig, OmegaConf
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


def get_struct(cube_conf):
    width=cube_conf.width
    height=cube_conf.height
    length=cube_conf.length

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
    
    return faces


def plot_cuboid(cube_conf1,cube_conf2):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    faces1=get_struct(cube_conf1)
    faces2=get_struct(cube_conf2)

    # Plot the cuboid
    ax.add_collection3d(Poly3DCollection(faces1, facecolors='cyan', linewidths=1, edgecolors='r', alpha=0.5))
    ax.add_collection3d(Poly3DCollection(faces2, facecolors='red', linewidths=1, edgecolors='b', alpha=0.5))

    # Set labels and title
    ax.set_xlabel('width')
    ax.set_ylabel('length')
    ax.set_zlabel('height')
    ax.set_title('Cuboid Plot')

    plt.show()


def calc_volume(conf):
    cube_conf1=conf.cube1 
    cube_conf2=conf.cube2 

    width1=cube_conf1.width
    height1=cube_conf1.height
    length1=cube_conf1.length
    width2=cube_conf2.width
    height2=cube_conf2.height
    length2=cube_conf2.length
    plot=conf.plot

    vol1=width1*length1*height1
    vol2=width2*length2*height2

    print(f"Volume1 is {vol1:.3f}")
    print(f"Volume2 is {vol2:.3f}")

    if plot:
        plot_cuboid(cube_conf1,cube_conf2)


@hydra.main(version_base=None, config_path="conf", config_name="config")
def my_app(conf : DictConfig) -> None:
    print(OmegaConf.to_yaml(conf))
    calc_volume(conf)

if __name__ == "__main__":
    my_app()