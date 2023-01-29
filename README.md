# Style-Transfer-bot - это итоговый проект по курсу Deep Learning School. В боте реализован перенос стиля с одного изображения на другое. Бот принимает 2 изображения одного размера: изображение, которое планируется видоизменять (content) и изображение, стиль которого будет применяться к первому (style). Для переноса стиля используется алгоритм из руководства PyTorch (https://pytorch.org/tutorials/advanced/neural_style_tutorial.html)

Requirements:
aiogram==2.24
aiohttp==3.8.3
aiosignal==1.3.1
async-timeout==4.0.2
attrs==22.2.0
Babel==2.9.1
certifi==2022.12.7
charset-normalizer==2.1.1
contourpy==1.0.7
cycler==0.11.0
fonttools==4.38.0
frozenlist==1.3.3
idna==3.4
kiwisolver==1.4.4
magic-filter==1.0.9
matplotlib==3.6.3
multidict==6.0.4
numpy==1.24.1
packaging==23.0
Pillow==9.4.0
pyparsing==3.0.9
pyTelegramBotAPI==4.9.0
python-dateutil==2.8.2
pytz==2022.7.1
requests==2.28.2
six==1.16.0
torch==1.13.1+cu117
torchaudio==0.13.1
torchvision==0.14.1
typing_extensions==4.4.0
urllib3==1.26.14
yarl==1.8.2

Бот работает следующим образом:
1. Отправляются первое и второе изображение по отдельности
![image](https://user-images.githubusercontent.com/103606051/215318424-82eaeb94-9120-40c6-8e35-1fe366048b6b.png)
![image](https://user-images.githubusercontent.com/103606051/215318474-79384998-63bc-411c-b812-1d800be514ef.png)

2. По команде /continue начинается обработка
![image](https://user-images.githubusercontent.com/103606051/215318492-348c9c8d-c5bd-494d-8742-d48828313aed.png)

3. После обработки бот присылает итоговое изображение
![image](https://user-images.githubusercontent.com/103606051/215318526-e48682d7-1a3e-4e89-8be3-16c448f3d0c4.png)



