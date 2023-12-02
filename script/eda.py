import pandas as pd
import altair as alt
import click
import seaborn as sns
import matplotlib.pyplot as plt
import os

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
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Load white wine dataset
    white_train = pd.read_csv(file_path, sep=',')

    # Display head of the dataset
    print("Head of the dataset:")
    print(white_train.head())

    # Visualize correlation and save it as a table
    print("\nCorrelation matrix:")
    correlation_matrix = white_train.corr()
    print(correlation_matrix)

    # Save correlation matrix as a CSV file
    correlation_path = os.path.join(script_dir, '..', 'results', 'tables', 'correlation_matrix.csv')
    os.makedirs(os.path.dirname(correlation_path), exist_ok=True)
    correlation_matrix.to_csv(correlation_path, index=True)

    # Scatter Matrix
    columns_to_repeat = ['density', 'residual sugar', 'total sulfur dioxide', 'quality']
    chart = create_repeated_scatter_chart(white_train, columns_to_repeat, width=100, height=100)
    # scatter_matrix_path = os.path.join(script_dir, '..', 'results', 'figures', 'scatter_matrix.html')
    scatter_matrix_path = os.path.join(script_dir, '..', 'results', 'figures', 'scatter_matrix.png')
    os.makedirs(os.path.dirname(scatter_matrix_path), exist_ok=True)
    chart.save(scatter_matrix_path)

    # Create a histogram for each column
    for column in white_train.columns:
        plt.figure(figsize=(8, 6))
        sns.histplot(white_train[column], kde=True, color='pink')
        plt.title(f'Distribution of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')

        # Save the histogram as a PNG file
        histogram_path = os.path.join(script_dir, '..', 'results', 'figures', f'histogram_{column}.png')
        os.makedirs(os.path.dirname(histogram_path), exist_ok=True)
        plt.savefig(histogram_path)
        plt.show()

if __name__ == '__main__':
    eda_script()

# In terminal, set current working directory as the root of git repo:
# python script/eda.py data/Processed/white_train.csv
