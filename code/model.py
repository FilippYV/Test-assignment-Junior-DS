import torch

from paths import path_to_model_r_cnn


def get_model() -> torch.nn.Module:
    """
    Загружает и возвращает модель R-CNN из сохранённого файла.

    Возвращает:
        torch.nn.Module: Загруженная модель R-CNN.
    """
    model = torch.load(path_to_model_r_cnn())
    return model
