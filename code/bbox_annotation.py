import time

import cv2

from paths import save_frame_without_bbox


def applying_bbox_on_frame(frame, boxes, scores, labels, show_frames, people_count):
    """
    Наносит ограничительные рамки на кадр и отображает информацию о детекции.

    Эта функция обводит обнаруженные объекты на кадре ограничительными рамками,
    добавляет текст с информацией о классе и уверенности, а также сохраняет
    обработанный кадр в файл.

    Параметры:
        frame: Кадр видео, на котором будут нанесены ограничительные рамки.
        boxes: Список ограничительных рамок (bounding boxes) для объектов.
        scores: Список уверенности (confidence scores) для объектов.
        labels: Список меток классов для объектов.
        show_frames (bool): Показывать ли кадры с нанесёнными ограничительными рамками.
        people_count (int): Количество людей, обнаруженных на кадре.

    Возвращает:
        None
    """
    for i, box in enumerate(boxes):
        x1, y1, x2, y2 = map(int, box)
        label = labels[i]
        score = scores[i]

        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)

        text = f"Class: {label}, Score: {score:.2f}"
        cv2.putText(frame, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    count_text = f"People count: {people_count}"
    cv2.putText(frame, count_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imwrite(f"{save_frame_without_bbox(time.time())}", frame)

    if show_frames:
        cv2.imshow("Predictions", frame)
        cv2.waitKey(1)
