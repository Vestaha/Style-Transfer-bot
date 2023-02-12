from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import model
from PIL import Image
import size

# для работы бота нам нужен токен, который мы берем в @BotFather
with open('token.txt') as f:
    TOKEN = f.read().strip()

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

flag = True
content_flag = False
style_flag = False


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\n Отправь мне изображение, которое ты хочешь стилизовать")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Это бот для стилизации изображений. Отправь мне изображение, которое хоешь стилизовать "
                        "и изображение с выбранным стилем. Изображения должны быть одного размера.")


@dp.message_handler(content_types=['photo'])
async def photo_processing(message):
    global flag
    global content_flag
    global style_flag

    if flag:
        await message.photo[-1].download('content.jpg')
        await message.answer(text='Первое изображение получено.'
                                  'Отправь изображение, стиль которого ты хочешь применить к первому')
        flag = False
        content_flag = True  # Бот знает, что существует изображение для стиилизации


    else:
        await message.photo[-1].download('style.jpg')
        await message.answer(text='Я получил второе изображение, нажми /continue')
        flag = True
        style_flag = True  # Now the bot knows that the style image exists.

# FSM прочитать

@dp.message_handler(commands=['continue'])
async def contin(message: types.Message):

    if not (content_flag * style_flag):
        await message.answer(text="Ты ещё не загрузил оба изображения.")
        return

    await message.answer(text='Обработка началась и может занять некоторое время. '
                              'Подождите немного.',
                         reply_markup=types.ReplyKeyboardRemove())
    img_for_shape = Image.open('content.jpg')
    # Нужно для подгонки форм изображений и чтобы итоговое изображение соответствовало размеру исходного
    (width, height) = img_for_shape.size
    img_shape = (height, width)
    # Далее идёт пред- и пост- обработка изображений
    content_img = size.preprocess('content.jpg', img_shape)
    content_img = size.postprocess(content_img)
    content_img = model.image_loader(content_img, height)

    style_img = size.preprocess('style.jpg', img_shape)
    style_img = size.postprocess(style_img)
    style_img = model.image_loader(style_img, height)

    input_img = content_img.clone()

    output_image = model.run_style_transfer(model.cnn, model.cnn_normalization_mean, model.cnn_normalization_std,
                             content_img, style_img, input_img)
    output_pil = output_image.cpu().clone()  # клонируем тензор, чтобы не производить изменения внутри
    output_pil = output_pil.squeeze(0)
    output_pil = model.unloader(output_pil)
    output_pil.save('result.jpg')
    print(output_pil.size)
    with open('result.jpg', 'rb') as file:
        await message.answer_photo(file, caption='Done!')


if __name__ == '__main__':
    executor.start_polling(dp)
