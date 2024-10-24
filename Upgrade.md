# Выводы по результатам работы программы

Программа успешно распознает людей на видео с помощью нейросетевой архитектуры **FastR-CNN**, выделяя их с помощью *
*bounding boxes** и считая количество. Она сохраняет данные в `dataframe` для дальнейшего анализа. Программа может быть
расширена для более специфических задач.

---

## Анализ качества распознавания

- **Точность распознавания** зависит от предварительно обученных весов, которые использует Fast R-CNN. Использование
  готовых весов обеспечивает хорошую начальную производительность
- **Скорость работы** программы при использовании Fast R-CNN приемлема для оффлайн обработки, но может быть недостаточно
  быстрой для задач реального времени.

---

## Предложения по дальнейшему улучшению

### 1. Дообучение модели (Fine-Tuning)

- Модель Fast R-CNN использует готовые веса, которые обучены на широком наборе классов объектов. Для улучшения точности
  можно **дообучить модель**, используя специализированные датасеты с фокусом на задачу распознавания людей. Это поможет
  лучше распознавать людей в различных условиях и исключить лишние классы объектов.
- Например, можно оставить в модели только один класс ("человек"), что улучшит как точность распознавания, так и
  скорость предсказания.

### 2. Использование других архитектур

- **YOLO (You Only Look Once)** — это более быстрая и эффективная архитектура для задач распознавания объектов. Она
  обеспечивает гораздо **более высокую скорость обработки кадров**, что особенно важно для задач реального времени.
- Однако для использования YOLO в коммерческих целях требуется соответствующая **лицензия**.

### 3. Подсчет уникальных людей

- Чтобы улучшить анализ потока людей, можно добавить механизм **отслеживания уникальных объектов** (например, с помощью
  трекеров или алгоритмов идентификации), чтобы не просто считать людей на каждом кадре, а также учитывать уникальные
  идентификаторы объектов в течение видео.

### 4. Анализ и визуализация данных

- На основе сохраненных данных можно проводить более глубокий анализ, включая визуализацию динамики изменения количества
  людей во времени, что может быть полезным для анализа пассажиропотоков или управления в реальном времени.

---

## Заключение

Программа представляет собой **базовый вариант (baseline)**, которая способна выполнять поставленную ей задачу.
Дальнейшее улучшение
возможно через дообучение модели, использование более быстрых архитектур и добавление новых функциональных возможностей,
таких как подсчет уникальных людей.
