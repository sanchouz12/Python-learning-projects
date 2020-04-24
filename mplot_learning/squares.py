import matplotlib.pyplot as plt

inputs = list(range(-10, 11))
squares = list(map(lambda x: x ** 2, inputs))

plt.plot(inputs, squares, linewidth = 1, c = "black")
plt.scatter(inputs, squares, s = 20, c = squares, cmap = plt.cm.seismic)
plt.axis([-20, 20, -200, 200])

plt.title("Squares", fontsize = 20)
plt.xlabel("Input", fontsize = 12)
plt.ylabel("Output", fontsize = 12)
plt.tick_params(axis = "both", labelsize = 12)

save = input(
    "Input 'save' to save the graph as image.\n"\
    "Input 'show' to show the graph in separate window\n"\
    "Input something else to exit.\n"\
    "=================================================\n"
)

if save == "save":
    plt.savefig("squares.png", bbox_inches = "tight")
elif save == "show":
    plt.show()
