import os
import shutil

import torch

from paths import path_to_save_photo, check_paths


def recreate_cache_photo() -> None:
    """
    Восстанавливает кэш фотографий, удаляя старую директорию и создавая новую.

    Эта функция проверяет существование директории для кэшированных фотографий.
    Если директория существует, она удаляется вместе с содержимым. Затем
    создаётся новая пустая директория.

    Возвращает:
        None
    """
    check_paths()
    directory = path_to_save_photo()

    if os.path.exists(directory):
        shutil.rmtree(directory)

    os.makedirs(directory)


def check_gpu(use_gpu: bool) -> torch.device:
    """
    Проверяет доступность GPU и возвращает соответствующее устройство.

    Параметры:
        use_gpu (bool): Флаг, указывающий, использовать ли GPU для обработки.

    Возвращает:
        torch.device: Устройство для выполнения вычислений (CPU или GPU).
    """
    if use_gpu:
        if torch.cuda.is_available():
            return torch.device("cuda")
        elif torch.backends.mps.is_available():
            return torch.device("mps")
        else:
            return torch.device("cpu")
    else:
        return torch.device("cpu")
