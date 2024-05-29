import matplotlib.pyplot as plt

def generate_bar_chart(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig("pie.png")
    plt.close()

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels = labels)
    plt.savefig("pie.png")
    plt.close()


if __name__ == '__main__':
    labels = ['A', 'B', 'C']
    values = [200, 34, 120]
    generate_pie_chart(labels, values)