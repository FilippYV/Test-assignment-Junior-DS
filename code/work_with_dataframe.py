import pandas as pd

from paths import path_to_dataset


def save_dataframe(dataframe: pd.DataFrame, filename: str) -> None:
    """
    Сохраняет DataFrame в CSV-файл.

    Параметры:
        dataframe (pd.DataFrame): DataFrame, который необходимо сохранить в файл.

    Возвращает:
        None
    """
    dataframe.to_csv(path_to_dataset(filename))


def save_data_to_dataframe(people_count: int, dataframe: pd.DataFrame) -> None:
    """
    Добавляет количество людей в DataFrame.

    Параметры:
        people_count (int): Количество людей, которое нужно сохранить.
        dataframe (pd.DataFrame): DataFrame, в который будет добавлено количество людей.

    Возвращает:
        None
    """
    dataframe.loc[len(dataframe), 'people_count'] = people_count
