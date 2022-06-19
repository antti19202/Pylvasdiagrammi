import numpy as np
import matplotlib.pyplot as plt

def drawBars(entryNames, entryValues1, entryValues2, entryValues3, entryValues4, titleEntry, xEntry, yEntry, barEntry1, barEntry2, barEntry3, barEntry4, inputTheme, inputWidth, grid, reversed):
    """Getting given values and creating graph"""
    names = []
    values1 = []
    values2 = []
    values3 = []
    values4 = []

    # Getting all names from entries
    for name in entryNames:
        names.append(name.get())

    # Getting all values from entries
    for value in entryValues1:
        values1.append(float(value.get()))
    if len(entryValues2) > 0:
        for value in entryValues2:
            values2.append(float(value.get()))
    if len(entryValues3) > 0:
        for value in entryValues3:
            values3.append(float(value.get()))
    if len(entryValues4) > 0:
        for value in entryValues4:
            values4.append(float(value.get()))

    # Reverse all values
    if reversed:
        names.reverse()
        values1.reverse()
        values2.reverse()
        values3.reverse()
        values4.reverse()

    # Cheackig whits theme were picked
    selectedTheme = theme(inputTheme)
    if selectedTheme == 'xkcd(cartoon)':
        plt.xkcd()
    else:
        plt.style.use(selectedTheme)

    # Setting singel bar graph
    if len(values2) == 0:
        plt.bar(names, values1)

        # Giving title and labels to graph
        plt.title(titleEntry.get())
        plt.xlabel(xEntry.get())
        plt.ylabel(yEntry.get())

        # Setting grid to graph
        if grid == 1:
            plt.grid(True)

        # Showing graph
        plt.show()

    elif len(values4) != 0:
        x = np.arange(len(names))

        if inputWidth == "":
            width = 0.20
        else:
            width = float(inputWidth)

        fig, ax = plt.subplots()
        rects1 = ax.bar(x-width*2+width/2, values1, width, label=barEntry1.get())
        rects2 = ax.bar(x-width/2, values2, width, label=barEntry2.get())
        rects3 = ax.bar(x+width/2, values3, width, label=barEntry3.get())
        rects4 = ax.bar(x+width*2-width/2, values4, width, label=barEntry4.get())

        ax.set_ylabel(yEntry.get())
        ax.set_xlabel(xEntry.get())
        ax.set_title(titleEntry.get())
        ax.set_xticks(x)
        ax.set_xticklabels(names)
        ax.legend()

        ax.bar_label(rects1, padding=3)
        ax.bar_label(rects2, padding=3)
        ax.bar_label(rects3, padding=3)
        ax.bar_label(rects4, padding=3)

        fig.tight_layout()

        # Setting grid to graph
        if grid == 1:
            plt.grid(True)

        plt.show()

    elif len(values3) != 0:
        x = np.arange(len(names))

        if inputWidth == "":
            width = 0.20
        else:
            width = float(inputWidth)

        fig, ax = plt.subplots()
        rects1 = ax.bar(x - width, values1, width, label=barEntry1.get())
        rects2 = ax.bar(x, values2, width, label=barEntry2.get())
        rects3 = ax.bar(x + width, values3, width, label=barEntry3.get())

        ax.set_ylabel(yEntry.get())
        ax.set_xlabel(xEntry.get())
        ax.set_title(titleEntry.get())
        ax.set_xticks(x)
        ax.set_xticklabels(names)
        ax.legend()

        ax.bar_label(rects1, padding=3)
        ax.bar_label(rects2, padding=3)
        ax.bar_label(rects3, padding=3)

        fig.tight_layout()

        # Setting grid to graph
        if grid == 1:
            plt.grid(True)

        plt.show()

    # Setting grouped bar graph with two groups
    elif len(values2) != 0:
        x = np.arange(len(names))

        if inputWidth == "":
            width = 0.35
        else:
            width = float(inputWidth)

        fig, ax = plt.subplots()
        rects1 = ax.bar(x - width/2, values1, width, label=barEntry1.get())
        rects2 = ax.bar(x + width/2, values2, width, label=barEntry2.get())

        ax.set_ylabel(yEntry.get())
        ax.set_xlabel(xEntry.get())
        ax.set_title(titleEntry.get())
        ax.set_xticks(x)
        ax.set_xticklabels(names)
        ax.legend()

        ax.bar_label(rects1, padding=3)
        ax.bar_label(rects2, padding=3)

        fig.tight_layout()

        # Setting grid to graph
        if grid == 1:
            plt.grid(True)

        plt.show()

def theme(theme):
    if theme == "default":
        return "default";
    elif theme == "Solarize_Light2":
        return "Solarize_Light2";
    elif theme == "_classic_test_patch":
        return "_classic_test_patch"
    elif theme == "bmh":
        return "bmh"
    elif theme == "classic":
        return "classic"
    elif theme == "dark_background":
        return "dark_background"
    elif theme == "fast":
        return "fast"
    elif theme == "fivethirtyeight":
        return "fivethirtyeight"
    elif theme == "ggplot":
        return "ggplot"
    elif theme == "grayscale":
        return "grayscale"
    elif theme == "seaborn":
        return "seaborn"
    elif theme == "seaborn-bright":
        return "seaborn-bright"
    elif theme == "seaborn-colorblind":
        return "seaborn-colorblind"
    elif theme == "seaborn-dark":
        return "seaborn-dark"
    elif theme == "seaborn-dark-palette":
        return "seaborn-dark-palette"
    elif theme == "seaborn-darkgrid":
        return "seaborn-darkgrid"
    elif theme == "seaborn-deep":
        return "seaborn-deep"
    elif theme == "seaborn-muted":
        return "seaborn-muted"
    elif theme == "seaborn-notebook":
        return "seaborn-notebook"
    elif theme == "seaborn-paper":
        return "seaborn-paper"
    elif theme == "seaborn-pastel":
        return "seaborn-pastel"
    elif theme == "seaborn-poster":
        return "seaborn-poster"
    elif theme == "seaborn-talk":
        return "seaborn-talk"
    elif theme == "seaborn-ticks":
        return "seaborn-ticks"
    elif theme == "seaborn-white":
        return "seaborn-white"
    elif theme == "seaborn-whitegrid":
        return "seaborn-whitegrid"
    elif theme == "tableau-colorblind10":
        return "tableau-colorblind10"
    elif theme == "xkcd(cartoon)":
        return "xkcd(cartoon)"