# Human Recognition in Video

## Описание проекта

Этот проект предназначен для обнаружения и подсчета людей на видео с использованием технологий компьютерного зрения и
машинного обучения. Он позволяет загружать видеофайлы и получать статистику о количестве людей в кадре.

## Установка

### 1. Клонируйте репозиторий

Сначала клонируйте этот репозиторий на свой компьютер:

```bash
git clone https://github.com/FilippYV/Test-assignment-Junior-DS/tree/master
cd Test-assignment-Junior-DS
```

### 2. Создайте и активируйте виртуальное

#### Для Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Для Linux/MacOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Установите зависимости

Установите необходимые библиотеки, используя `pip`:

```
pip install -r requirements.txt
```

### 4. Скачайте веса нейросети

Скачайте файл с весами [`model_fast_rcnn.pth`](https://disk.yandex.ru/d/zG3mRljJcZzVtw) с яндекс диска, и поместите его
в папку `model_weight`:

```html
https://disk.yandex.ru/d/zG3mRljJcZzVtw
```

## Запуск проекта

Для запуска проекта используйте следующую команду, передавая необходимые аргументы:

```bash
python human_recognition.py --path path/to/video.mp4 --use_gpu True --threshold 0.5 --show_frame True
```

#### Параметры

* --path: Путь к видеофайлу (по умолчанию: static/raw_video/crowd.mp4).
* --use_gpu: Использовать GPU для обработки (по умолчанию: True).
* --threshold: Порог уверенности для обнаружения (по умолчанию: 0.5).
* --show_frame: Отображать каждый кадр во время обработки (по умолчанию: False).

