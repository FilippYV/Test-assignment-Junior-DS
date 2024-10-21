import os

import cv2
import numpy
import pandas as pd
import torch
import torchvision
from tqdm import tqdm

from code.auxiliary_scripts import check_gpu, recreate_cache_photo
from code.bbox_annotation import applying_bbox_on_frame
from code.drawing_graphs import plot_people_count
from code.model import get_model
from code.work_with_dataframe import save_dataframe, save_data_to_dataframe
from code.work_with_video import get_path_video, save_new_video


def predict(frame: numpy.ndarray, model: torch.nn.Module, device: torch.device, threshold: float, show_frames: bool,
            dataframe: pd.DataFrame) -> None:
    """
    Выполняет предсказание количества людей на одном кадре.

    Эта функция обрабатывает кадр, применяет модель для распознавания людей и
    отображает ограничительные рамки (bounding boxes) на кадре.

    Параметры:
        frame: Кадр видео в формате BGR.
        model: Модель для распознавания объектов.
        device: Устройство (CPU или GPU), на котором выполняется модель.
        threshold (float): Порог уверенности для детекции людей.
        show_frames (bool): Показывать ли кадры с ограничительными рамками.
        dataframe: DataFrame для сохранения количества людей.

    Возвращает:
        None
    """
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    transform = torchvision.transforms.ToTensor()
    image_tensor = transform(image_rgb).unsqueeze(0).to(device)

    with torch.no_grad():
        predictions = model(image_tensor)

    boxes = predictions[0]['boxes']
    scores = predictions[0]['scores']
    labels = predictions[0]['labels']

    person_class = 1
    mask = (scores > threshold) & (labels == person_class)
    boxes = boxes[mask].cpu().numpy()
    scores = scores[mask].cpu().numpy()
    labels = labels[mask].cpu().numpy()

    people_count = len(boxes)

    save_data_to_dataframe(people_count, dataframe)

    applying_bbox_on_frame(frame, boxes, scores, labels, show_frames, people_count)


def human_recognition(path='static/crowd.mp4', use_gpu=True, threshold=0.5, show_frame=True) -> None:
    """
    Запускает процесс распознавания людей на видео.

    Эта функция инициализирует модель, читает видео, обрабатывает кадры и
    отображает количество людей на графике.

    Параметры:
        path (str): Путь к видеофайлу. По умолчанию 'static/crowd.mp4'.
        use_gpu (bool): Использовать ли GPU для обработки. По умолчанию True.
        threshold (float): Порог уверенности для детекции. По умолчанию 0.5.
        show_frame (bool): Отображать ли каждый кадр во время обработки. По умолчанию True.

    Возвращает:
        None
    """
    recreate_cache_photo()

    video_file = get_path_video(path)
    filename = os.path.basename(path).split('.')[0]

    model = get_model()
    model.eval()

    device = check_gpu(use_gpu)
    model.to(device)

    dataframe = pd.DataFrame(columns=['people_count'])

    total_frames = int(video_file.get(cv2.CAP_PROP_FRAME_COUNT))

    with torch.no_grad():
        for _ in tqdm(range(total_frames), desc="Обработка кадров", unit="кадр"):
            ret, frame = video_file.read()
            if not ret:
                break
            predict(frame, model, device, threshold, show_frame, dataframe)

    cv2.destroyAllWindows()
    video_file.release()

    plot_people_count(dataframe, filename)

    save_dataframe(dataframe, filename)

    save_new_video(path, filename)
