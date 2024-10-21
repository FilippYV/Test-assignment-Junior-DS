import pandas as pd
from matplotlib import pyplot as plt

from paths import path_to_graph


def plot_people_count(dataframe: pd.DataFrame, filename: str) -> None:
    """
    Строит график количества людей на основе данных из DataFrame.

    Параметры:
        dataframe (pd.DataFrame): DataFrame с данными.
        filename (str): Имя файла для сохранения графика.

    Возвращает:
        None
    """
    plt.style.use('ggplot')

    plt.figure(figsize=(12, 6))

    plt.plot(dataframe.index, dataframe['people_count'], marker='o', linestyle='-', color='royalblue',
             linewidth=2, markersize=6, markerfacecolor='orange', markeredgewidth=2)

    plt.title('People Count Over Time', fontsize=18, fontweight='bold')
    plt.xlabel('Frame', fontsize=14, fontweight='bold')
    plt.ylabel('Number of People', fontsize=14, fontweight='bold')

    plt.xticks(rotation=45, fontsize=12)
    plt.yticks(fontsize=12)

    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()

    plt.savefig(path_to_graph(filename), dpi=300)
    # plt.show()
