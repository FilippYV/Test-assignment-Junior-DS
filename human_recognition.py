import argparse

from code.predicton import human_recognition


def main() -> None:
    """
    Запускает процесс распознавания людей на видео.

    Эта функция создает парсер аргументов командной строки для получения параметров.

    Параметры:
        --path (str): Путь к видеофайлу. По умолчанию 'static/raw_video/crowd.mp4'.
        --use_gpu (bool): Использовать ли GPU для обработки. По умолчанию True.
        --threshold (float): Порог уверенности для детекции. По умолчанию 0.5.
        --show_frame (bool): Отображать ли каждый кадр во время обработки. По умолчанию True.

    Возвращает:
        None
    """
    parser = argparse.ArgumentParser(description='Human recognition in video.')
    parser.add_argument('--path', type=str, required=True, help='Path to video file')
    parser.add_argument('--use_gpu', type=bool, default=True, help='Use GPU for processing')
    parser.add_argument('--threshold', type=float, default=0.5, help='Confidence threshold for detection')
    parser.add_argument('--show_frame', type=bool, default=False, help='Display each frame during processing')

    args = parser.parse_args()

    human_recognition(path=args.path, use_gpu=args.use_gpu, threshold=args.threshold, show_frame=args.show_frame)


if __name__ == '__main__':
    main()
