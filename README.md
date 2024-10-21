# Human Recognition in Video

## Описание проекта

Этот проект предназначен для обнаружения и подсчета людей на видео с использованием технологий компьютерного зрения и
машинного обучения. Он позволяет загружать видеофайлы и получать статистику о количестве людей в кадре.

## Пример робыты программы

![Пример работы программы](https://github.com/user-attachments/assets/6e46442a-7eda-422b-b696-2722bf86501c)
На кадре из видео как программа выполнять детекцию людей и их отрисовку.
[Полнове видео](https://disk.yandex.ru/i/Dpyoxp-vOJwRQA) можно скачать на яндекс диске.

График по полученным данным
![crowd](https://private-user-images.githubusercontent.com/102216221/378483596-69decea6-3ef7-4ecc-a5f5-0136d009d446.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Mjk1MjMzODksIm5iZiI6MTcyOTUyMzA4OSwicGF0aCI6Ii8xMDIyMTYyMjEvMzc4NDgzNTk2LTY5ZGVjZWE2LTNlZjctNGVjYy1hNWY1LTAxMzZkMDA5ZDQ0Ni5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQxMDIxJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MTAyMVQxNTA0NDlaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT01ZjgyMDk4ZDI3NmI3ZmJkODJhMmNlMGIyMDE1YzdmZDZmN2NmZThiNGJlMGY0NjY4OTY5YzhiNTU0MzIwODZiJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.dvgIzH03KAbYNG5YoOgIZ1MJt--FL8PEJXzN8JF9LGU)



## Установка

### 1. Клонируйте репозиторий

Сначала клонируйте этот репозиторий на свой компьютер:

```bash
git clone https://github.com/FilippYV/Test-assignment-Junior-DS/tree/master
cd Test-assignment-Junior-DS
```

### 2. Создайте и активируйте виртуальное окружение

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

#### 3.1 Учтите что, для вычисления на графическом процессоре, вам необходимо скачать, версию pytorch, которая поддерживает ваше устройстве. Скачать pytorch с поддержкой вашего gpu можно [тут](https://pytorch.org/get-started/locally/).

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

