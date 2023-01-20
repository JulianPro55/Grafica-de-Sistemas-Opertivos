import matplotlib.pyplot as plt

def generate_chart(labelbs, values):

    fig, ax = plt.subplots()
    ax.bar(labelbs, values)
    plt.show()

def generate_pie_chart(labelbs, values):
    fix, ax = plt.subplots()
    ax.pie(values, labels = labelbs)
    ax.axis("equal")
    plt.show()