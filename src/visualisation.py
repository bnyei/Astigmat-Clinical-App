import matplotlib.pyplot as plt


def graphical_plot(gm):

    fig, ax = plt.subplots()

    origin = [0, 0]

    ax.quiver(*origin, gm.H1, gm.V1, angles='xy', scale_units='xy', scale=1)
    ax.quiver(*origin, gm.H2, gm.V2, angles='xy', scale_units='xy', scale=1)
    ax.quiver(*origin, gm.Ht, gm.Vt, angles='xy', scale_units='xy', scale=1)

    # Labels
    ax.text(gm.H1, gm.V1, "Lens 1")
    ax.text(gm.H2, gm.V2, "Lens 2")
    ax.text(gm.Ht, gm.Vt, "Resultant")

    ax.axhline(0)
    ax.axvline(0)

    ax.set_xlabel("Horizontal Component")
    ax.set_ylabel("Vertical Component")
    ax.set_aspect('equal', adjustable='box')
    ax.grid(True)

    # Auto scaling
    max_val = max(
        abs(gm.Ht), abs(gm.Vt),
        0.25
    ) * 1.5

    ax.set_xlim(-max_val, max_val)
    ax.set_ylim(-max_val, max_val)

    return fig
