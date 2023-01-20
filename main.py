import package.function_csv as get_csv
import package.charts as chart

def run():
    """Get all data"""
    data = get_csv.read_csv("used_device_data.csv")

    """All data from the column i chosed"""
    column = get_csv.select_column(data, "os")
    labels = list(set(column))
    cantidad = ({label: column.count(label) for label in labels})
    values = list(cantidad.values())
    
    chart.generate_chart(labels, values)

if __name__ == "__main__":
    run()