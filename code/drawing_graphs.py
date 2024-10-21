import pandas as pd
from matplotlib import pyplot as plt

from paths import path_to_graph


def plot_people_count(dataframe: pd.DataFrame, filename: str) -> None:
    """
    Строит график количества людей на основе данных из DataFrame.

    Эта функция принимает DataFrame, содержащий количество людей на каждом
    кадре, и строит график, отображающий изменения количества людей во
    времени. График сохраняется в виде PNG-файла.

    Параметры:
        dataframe (pd.DataFrame): DataFrame, содержащий столбец 'people_count'
                                   с количеством людей.

    Возвращает:
        None
    """
    plt.figure(figsize=(10, 5))

    plt.plot(dataframe.index, dataframe['people_count'], marker='o', linestyle='-')

    plt.title('People Count')
    plt.xlabel('Frame')
    plt.ylabel('Number of People')

    plt.xticks(rotation=45)
    plt.grid()
    plt.tight_layout()

    plt.savefig(path_to_graph(filename))
