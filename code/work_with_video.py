import glob
import os

import cv2

from paths import check_path, path_to_save_new_video, path_to_save_photo


def video_initialization(users_path: str) -> bool:
    """
    Инициализирует видеопоток из заданного пути.

    Параметры:
        users_path (str): Путь к видеофайлу.

    Возвращает:
        bool: True, если видео успешно открыто, иначе вызывает ValueError.

    Исключения:
        ValueError: Если видеофайл не может быть открыт.
    """
    cap = cv2.VideoCapture(users_path)
    if cap.isOpened():
        return True
    else:
        raise ValueError(f'Некорректное видео')


def get_file_name_from_path(path: str) -> str:
    """
        Извлекает имя файла из заданного пути.

        Параметры:
            path (str): Путь к файлу.

        Возвращает:
            str: Имя файла без пути.
        """
    return os.path.basename(path)


def get_path_video(path: str) -> cv2.VideoCapture:
    """
    Получает объект VideoCapture для указанного видеофайла.

    Параметры:
        path (str): Путь к видеофайлу.

    Возвращает:
        cv2.VideoCapture: Объект VideoCapture, если видеофайл корректен, иначе None.

    Исключения:
        FileNotFoundError: Если файл не существует.
    """
    if check_path(path):
        if video_initialization(path):
            return cv2.VideoCapture(path)


def save_new_video(path: str, name_new_video: str) -> None:
    """
        Сохраняет новое видео, используя кадры из директории.

        Параметры:
            path (str): Путь к исходному видеофайлу.

        Возвращает:
            None
        """
    old_video = cv2.VideoCapture(path)
    width = int(old_video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(old_video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = old_video.get(cv2.CAP_PROP_FPS)
    old_video.release()

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(path_to_save_new_video(name_new_video), fourcc, fps, (width, height))

    frame_files = sorted(glob.glob(os.path.join(path_to_save_photo(), '*.jpg')))  # Измените на нужный формат файлов

    for frame_file in frame_files:
        frame = cv2.imread(frame_file)  # Чтение кадра

        if frame is None:
            print(f"Ошибка чтения кадра: {frame_file}")
            continue

        frame = cv2.resize(frame, (width, height))

        out.write(frame)

    out.release()
