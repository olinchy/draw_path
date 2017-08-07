# import necessary module
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt


def draw3d(paths, msg):
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    ax.set_title('running path test in 3d: ' + msg)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

    for path in paths:
        ax.plot(path.x(), path.y(), path.z(), c=path.color())

    plt.show()


def draw2d(paths, msg):
    fig = plt.figure()
    ax = fig.gca()
    ax.set_title('running path test in 2d: ' + msg)

    for path in paths:
        ax.plot(path.x(), path.y(), color=path.color(), linewidth=2)
    plt.ylim()
    plt.show()
