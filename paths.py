import os
from pathlib import Path


def get_project_root() -> Path:
    """
    Возвращает корневую директорию проекта.

    Возвращает:
        Path: Путь к корневой директории проекта.
    """
    return Path(__file__).parent


def check_path(path: str) -> bool:
    """
    Проверяет, существует ли заданный путь.

    Параметры:
        path (str): Путь к файлу или директории.

    Исключения:
        FileNotFoundError: Если файл или директория не существуют.

    Возвращает:
        bool: True, если путь существует, иначе False.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Файл или директория '{path}' не существуют")
    return True


def path_to_save_photo() -> str:
    """
    Получает путь, по которому следует сохранять фотографии.

    Возвращает:
        str: Путь к директории 'static/cache_photo'.
    """
    return os.path.join(get_project_root(), 'static/cache_photo')


def path_to_model_r_cnn() -> str:
    """
    Получает путь к весам модели R-CNN.

    Возвращает:
        str: Путь к файлу 'model_weight/model_fast_rcnn.pth'.
    """
    return os.path.join(get_project_root(), 'model_weight/model_fast_rcnn.pth')


def save_frame_without_bbox(name_frame) -> str:
    """
    Генерирует путь для сохранения кадра без ограничивающего прямоугольника.

    Параметры:
        name_frame: Имя кадра, который нужно сохранить.

    Возвращает:
        str: Полный путь для сохранения кадра в формате JPEG.
    """
    return os.path.join(path_to_save_photo(), str(name_frame) + '.jpg')


def path_to_dataset(filename: str) -> str:
    """
    Формирует путь к CSV-файлу в директории с данными.

    Параметры:
        filename (str): Имя файла без расширения.

    Возвращает:
        str: Полный путь к CSV-файлу.
    """
    return os.path.join(get_project_root(), f'static/dataset/{filename}.csv')


def path_to_graph(filename) -> str:
    """
    Формирует путь к PNG-файлу в директории с графиками.

    Параметры:
        filename (str): Имя файла без расширения.

    Возвращает:
        str: Полный путь к PNG-файлу.
    """
    return os.path.join(get_project_root(), f'static/graph/{filename}.png')


def path_to_save_new_video(name_video) -> str:
    """
    Генерирует путь для сохранения нового видеофайла.

    Параметры:
        name_video: Имя видео, которое нужно сохранить.

    Возвращает:
        str: Полный путь для сохранения видео.
    """
    return os.path.join(get_project_root(), f'static/video/{name_video}.mp4')


def check_paths():
    os.makedirs(os.path.join(get_project_root(), f'static'), exist_ok=True)
    os.makedirs(os.path.join(get_project_root(), f'static/cache_photo'), exist_ok=True)
    os.makedirs(os.path.join(get_project_root(), f'static/dataset'), exist_ok=True)
    os.makedirs(os.path.join(get_project_root(), f'static/graph'), exist_ok=True)
    os.makedirs(os.path.join(get_project_root(), f'static/raw_video'), exist_ok=True)
    os.makedirs(os.path.join(get_project_root(), f'static/video'), exist_ok=True)
