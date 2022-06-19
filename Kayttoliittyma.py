import tkinter as tk
import grafiikka as gf
from tkinter import Checkbutton, filedialog, ttk
from idlelib.tooltip import Hovertip

themes = [
        'default',
        'Solarize_Light2',
        '_classic_test_patch',
        'bmh',
        'classic',
        'dark_background',
        'fast',
        'fivethirtyeight',
        'ggplot',
        'grayscale',
        'seaborn',
        'seaborn-bright',
        'seaborn-colorblind',
        'seaborn-dark',
        'seaborn-dark-palette',
        'seaborn-darkgrid',
        'seaborn-deep',
        'seaborn-muted',
        'seaborn-notebook',
        'seaborn-paper',
        'seaborn-pastel',
        'seaborn-poster',
        'seaborn-talk',
        'seaborn-ticks',
        'seaborn-white',
        'seaborn-whitegrid',
        'tableau-colorblind10',
        'xkcd(cartoon)']

histogramSize = ['2', '3', '4']

def mainWindow():
    """Main window creation function"""
    root.title('Antin iso muna')
    toolbar = tk.Frame(root)
    toolbar.grid(row=0, column=0, sticky="w")

    # Toolbar mode label and buttons
    modeLabel = tk.Label(toolbar, text="Modes")
    modeLabel.grid(row=0, column=0, sticky="w")
    barButton = tk.Button(toolbar, text="Bar", command=barGraph)
    barButton.grid(row=0, column=1, sticky="w")
    plotButton = tk.Button(toolbar, text="Plot", command=plotGraph)
    plotButton.grid(row=0, column=2, sticky="w")

def barGraph():
    """Bar graph creation function"""
    startFrame = tk.Frame(root)
    startFrame.grid(row=1, column=0, columnspan=10, sticky="w")

    """Bar graph creation options"""
    # Hostogram selection
    histogramValue = tk.IntVar()

    histogramLabel = tk.Label(startFrame, text="Histogram")
    histogramLabel.grid(row=0, column=0, sticky="w")
    histogramBox = Checkbutton(startFrame, variable=histogramValue, onvalue=1, offvalue=0)
    histogramBox.grid(row=0, column=1, sticky="w")
    histogramCombo = ttk.Combobox(startFrame, value=["2", "3", "4"], width=3)
    histogramCombo.current(0)
    histogramCombo.grid(row=0, column=2)
    Hovertip(histogramLabel, "Grouped bar")
    Hovertip(histogramCombo, "Number of bars (2-4)")

    # Element creation option
    numOfElemLabel = tk.Label(startFrame, text="Number of elements*")
    numOfElemLabel.grid(row=1, column=0, columnspan=5, sticky="w")
    numOfElemBox = tk.Entry(startFrame, width=4)
    numOfElemBox.grid(row=1, column=5, padx=10, sticky="w")
    Hovertip(numOfElemLabel, "How many enements are in graph")

    # Button for creating graph settings
    numOfElemButton = tk.Button(startFrame, text="Create", command=lambda:createElements(int(numOfElemBox.get()), histogramValue.get(), histogramCombo.get()))
    numOfElemButton.grid(row=2, column=0, padx=5, pady=5, sticky="w")

def plotGraph():
    pass

def openFile():
    """Selecting opening file"""
    filetypes = (
        ('csv and txt files', '*.csv' and '*.txt'),
        ('All files', '*.*'))
    filename = filedialog.askopenfilename(initialdir = '/', title = 'Select file', filetypes=filetypes)

    fileTextArea.delete(1.0,"end")
    fileTextArea.insert(1.0, filename)

def createElements(elements, histogram, histogramNum):
    """Creating number of elements"""

    # Arrays for names and values
    entryNames = []
    entryValues1 = []
    entryValues2 = []
    entryValues3 = []
    entryValues4 = []

    # Frame for graph names and values
    elementFrame1 = tk.Frame(root)
    elementFrame1.grid(row=2, column=0, columnspan=50, sticky="w")

    # Name and value
    nameLabel = tk.Label(elementFrame1, text="Name")
    nameLabel.grid(row=0, column=1)
    valueLabel = tk.Label(elementFrame1, text="Value*")
    valueLabel.grid(row=0, column=2, padx=10)

    # If histogram, create another column for second values
    if histogram and histogramNum == "2":
        value2Label = tk.Label(elementFrame1, text="Value*")
        value2Label.grid(row=0, column=3, padx=10)

    elif histogram and histogramNum == "3":
        value2Label = tk.Label(elementFrame1, text="Value*")
        value2Label.grid(row=0, column=3, padx=10)
        value3Label = tk.Label(elementFrame1, text="Value*")
        value3Label.grid(row=0, column=4, padx=10)

    elif histogram and histogramNum == "4":
        value2Label = tk.Label(elementFrame1, text="Value*")
        value2Label.grid(row=0, column=3, padx=10)
        value3Label = tk.Label(elementFrame1, text="Value*")
        value3Label.grid(row=0, column=4, padx=10)
        value4Label = tk.Label(elementFrame1, text="Value*")
        value4Label.grid(row=0, column=5, padx=10)


    # Create given number of entries
    for i in range(elements):
        label = tk.Label(elementFrame1, text=f"Element {i+1}")
        label.grid(row=i+1, column=0, padx=10, sticky="w")

        nameEntry = tk.Entry(elementFrame1, width=15)
        nameEntry.grid(row=i+1, column=1, sticky="w")
        entryNames.append(nameEntry)

        valueEntry = tk.Entry(elementFrame1, width=7)
        valueEntry.grid(row=i+1, column=2, padx=5, sticky="w")
        entryValues1.append(valueEntry)

        if histogram and histogramNum == "2" or histogram == "":
            valueEntry2 = tk.Entry(elementFrame1, width=7)
            valueEntry2.grid(row=i+1, column=3, padx=5, sticky="w")
            entryValues2.append(valueEntry2)

        elif histogram and histogramNum == "3":
            valueEntry2 = tk.Entry(elementFrame1, width=7)
            valueEntry2.grid(row=i+1, column=3, padx=5, sticky="w")
            entryValues2.append(valueEntry2)
            valueEntry3 = tk.Entry(elementFrame1, width=7)
            valueEntry3.grid(row=i+1, column=4, padx=5, sticky="w")
            entryValues3.append(valueEntry3)

        elif histogram and histogramNum == "4":
            valueEntry2 = tk.Entry(elementFrame1, width=7)
            valueEntry2.grid(row=i+1, column=3, padx=5, sticky="w")
            entryValues2.append(valueEntry2)
            valueEntry3 = tk.Entry(elementFrame1, width=7)
            valueEntry3.grid(row=i+1, column=4, padx=5, sticky="w")
            entryValues3.append(valueEntry3)
            valueEntry4 = tk.Entry(elementFrame1, width=7)
            valueEntry4.grid(row=i+1, column=5, padx=5, sticky="w")
            entryValues4.append(valueEntry4)

    # Create new frame for titles and labels
    elementFrame2 = tk.Frame(root)
    elementFrame2.grid(row=3, column=0, pady=5)

    # Title label and entry
    titleLabel = tk.Label(elementFrame2, text="Title: ")
    titleLabel.grid(row=0, column=0, padx=5)
    titleEntry = tk.Entry(elementFrame2, width=15)
    titleEntry.grid(row=0, column=1)
    Hovertip(titleLabel, "Graph title")

    # Y label and entry
    yLabel = tk.Label(elementFrame2, text="Y label: ")
    yLabel.grid(row=1, column=0, padx=5)
    yEntry = tk.Entry(elementFrame2, width=15)
    yEntry.grid(row=1, column=1)
    Hovertip(yLabel, "Y axis label")

    # X label and entry
    xLabel = tk.Label(elementFrame2, text="X label: ")
    xLabel.grid(row=2, column=0, padx=5)
    xEntry = tk.Entry(elementFrame2, width=15)
    xEntry.grid(row=2, column=1)
    Hovertip(xLabel, "X axis label")

    # Histogram bar labels
    barLabel1 = tk.Label(elementFrame2, text="Bar label: ")
    barEntry1 = tk.Entry(elementFrame2, width=15)
    Hovertip(barLabel1, "First column label")
    barLabel2 = tk.Label(elementFrame2, text="Bar label: ")
    barEntry2 = tk.Entry(elementFrame2, width=15)
    Hovertip(barLabel2, "Second column label")
    barLabel3 = tk.Label(elementFrame2, text="Bar label: ")
    barEntry3 = tk.Entry(elementFrame2, width=15)
    Hovertip(barLabel3, "Third column label")
    barLabel4 = tk.Label(elementFrame2, text="Bar label: ")
    barEntry4 = tk.Entry(elementFrame2, width=15)
    Hovertip(barLabel4, "Fourth column label")

    # If histogram = true, bar labels are shown
    if histogram and histogramNum == "2":
        barLabel1.grid(row=3, column=0)
        barEntry1.grid(row=3, column=1)
        barLabel2.grid(row=4, column=0)
        barEntry2.grid(row=4, column=1)

    elif histogram and histogramNum == "3":
        barLabel1.grid(row=3, column=0)
        barEntry1.grid(row=3, column=1)
        barLabel2.grid(row=4, column=0)
        barEntry2.grid(row=4, column=1)
        barLabel3.grid(row=5, column=0)
        barEntry3.grid(row=5, column=1)

    elif histogram and histogramNum == "4":
        barLabel1.grid(row=3, column=0)
        barEntry1.grid(row=3, column=1)
        barLabel2.grid(row=4, column=0)
        barEntry2.grid(row=4, column=1)
        barLabel3.grid(row=5, column=0)
        barEntry3.grid(row=5, column=1)
        barLabel4.grid(row=6, column=0)
        barEntry4.grid(row=6, column=1)

    # Theme selection
    selectTheme = tk.StringVar(elementFrame1)
    selectTheme.set(themes[0])

    themeLabel = tk.Label(elementFrame2, text="Theme: ")
    themeLabel.grid(row=7, column=0)
    theme = ttk.Combobox(elementFrame2, value=themes, width=20)
    theme.current(0)
    theme.grid(row=7, column=1, pady = 5)
    Hovertip(themeLabel, "Theme of bars")

    # Advanced settings
    # Advanced settings frame
    advancedFrame = tk.LabelFrame(elementFrame2, text="Advanced Settings")
    advancedFrame.grid(row=8, column=0, columnspan=100, padx=10, sticky="nsew")

    # Bar width setting
    widthLabel = tk.Label(advancedFrame, text="Widht: ")
    widthLabel.grid(row=0, column=0)
    widthEntry = tk.Entry(advancedFrame, width=10)
    widthEntry.grid(row=0, column=1, padx=5)
    Hovertip(widthLabel, "Width of bars")

    # Grid setting
    gridValue = tk.IntVar()
    gridLabel = tk.Label(advancedFrame, text="Grid")
    gridLabel.grid(row=1, column=0, sticky="w")
    gridCheck = Checkbutton(advancedFrame, variable=gridValue, onvalue=1, offvalue=0)
    gridCheck.grid(row=1, column=1, sticky="w")
    Hovertip(gridLabel, "Show grids on graph (some themes have automatically grids)")

    # Change rotation

    # Reverse setting
    reverseValue = tk.IntVar()
    reverseLabel = tk.Label(advancedFrame, text="Reverse")
    reverseLabel.grid(row=2, column=0, sticky="w")
    reverseCheck = Checkbutton(advancedFrame, variable=reverseValue, onvalue=1, offvalue=0)
    reverseCheck.grid(row=2, column=0)
    Hovertip(reverseLabel, "Reverse graph")

    # Button for creating a new graph
    showButton = tk.Button(elementFrame2, text="Draw bars", command=lambda:gf.drawBars(entryNames, entryValues1, entryValues2, entryValues3, entryValues4, titleEntry, xEntry, yEntry, barEntry1, barEntry2, barEntry3, barEntry4, theme.get(), widthEntry.get(), gridValue.get(), reverseValue.get()))
    showButton.grid(row=10, column=0, padx=10, pady=10)

def main():
    global root
    root = tk.Tk()
    mainWindow()
    barGraph()
    tk.mainloop()

if __name__ == "__main__":
    main()
"""
# Filepath text area and openfile button
filePathLabel = tk.Label(root, text = 'File path:', pady = 5)
filePathLabel.grid(row = 0, column = 0)
fileTextArea = tk.Text(root, height = 1, width = 20)
fileTextArea.grid(row = 0, column = 1, columnspan = 3, sticky='EW')
openfile = tk.Button(root, text='Open File', command=openFile)
openfile.grid(row = 0, column = 4)

# File separator
separatorLabel = tk.Label(root, text='Separator:', pady = 5)
separatorLabel.grid(row = 2, column = 0)
separatorTip = Hovertip(separatorLabel, "What is separator of the file")
separatorTextArea = tk.Text(root, height = 1, width = 5)
separatorTextArea.insert(1.0, ",")
separatorTextArea.grid(row = 2, column = 1)

# Skip header
headerLabel = tk.Label(root, text='Skip header:', pady = 5)
headerLabel.grid(row = 3, column = 0)
Checkbutton(root).grid(row = 3, column = 1)
"""