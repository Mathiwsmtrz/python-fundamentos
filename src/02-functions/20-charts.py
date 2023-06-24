import app.charts as myCharts

if __name__ == '__main__':
    labels = ['a', 'b']
    values = [100, 300]
    myCharts.generate_bar_chart(labels, values)
    myCharts.generate_pie_chart(labels, values)