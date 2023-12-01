import pandas as pd
import altair as alt
import click
import seaborn as sns
import matplotlib.pyplot as plt

@click.command()
@click.argument('data')
@click.argument('columns') 
@click.option('--width', default=100, help='Width of the chart')
@click.option('--height', default=100, help='Height of the chart')
def create_repeated_scatter_chart(data, columns, width, height):
    """
    Create a repeated scatter chart using Altair.

    Parameters:
        - data: The DataFrame containing the data.
        - columns: The columns to repeat for the x-axis and y-axis.
        - width (int, optional): Width of the chart. Default is 100.
        - height (int, optional): Height of the chart. Default is 100.

    Returns:
        alt.Chart: Altair chart object.
    """
    alt.data_transformers.enable('vegafusion')

    chart = alt.Chart(data).mark_point(opacity=0.3, size=10).encode(
        alt.X(alt.repeat('row'), type='quantitative'),
        alt.Y(alt.repeat('column'), type='quantitative')
    ).properties(
        width=width,
        height=height
    ).repeat(
        column=columns,
        row=columns
    )

    return chart

@click.command()
@click.argument('file_path', type=click.Path(exists=True))
def eda_script(file_path):
    """
    Perform EDA by visualization.

    Parameters:
        - file_path (str): Path to the CSV file.

    Returns:
        None
    """
    # Load white wine dataset
    white_train = pd.read_csv(file_path, sep=';')

    # Display head of the dataset
    print("Head of the dataset:")
    print(white_train.head())

    # Visualize correlation
    print("\nCorrelation matrix:")
    print(white_train.corr())

    # Scatter Matrix
    columns_to_repeat = ['density', 'residual sugar', 'total sulfur dioxide', 'quality']
    chart = create_repeated_scatter_chart(white_train, columns_to_repeat)
    chart.save("scatter_matrix.html")  # Save the chart as an HTML file

    # Create a histogram for each column
    for column in white_train.columns:
        plt.figure(figsize=(8, 6))
        sns.histplot(white_train[column], kde=True, color='pink')
        plt.title(f'Distribution of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.show()

if __name__ == '__main__':
    eda_script()
