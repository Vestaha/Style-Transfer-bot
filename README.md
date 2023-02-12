# Style-Transfer-bot 

Style-Transfer-bot - это итоговый проект по курсу Deep Learning School. В боте реализован перенос стиля с одного изображения на другое. Бот принимает 2 изображения одного размера: изображение, которое планируется видоизменять (content) и изображение, стиль которого будет применяться к первому (style). Для переноса стиля используется алгоритм из руководства PyTorch (https://pytorch.org/tutorials/advanced/neural_style_tutorial.html)

Информация о зависимостях находится в файле requirements.txt

Бот работает следующим образом:
1. Отправляются первое и второе изображение по отдельности

![image](https://user-images.githubusercontent.com/103606051/215318424-82eaeb94-9120-40c6-8e35-1fe366048b6b.png)

![image](https://user-images.githubusercontent.com/103606051/215318474-79384998-63bc-411c-b812-1d800be514ef.png)

2. По команде /continue начинается обработка

![image](https://user-images.githubusercontent.com/103606051/215318492-348c9c8d-c5bd-494d-8742-d48828313aed.png)

3. После обработки бот присылает итоговое изображение

![image](https://user-images.githubusercontent.com/103606051/215318526-e48682d7-1a3e-4e89-8be3-16c448f3d0c4.png)

UPD 12.02.2023:
Теперь бот может работать с изображениями разного размера
