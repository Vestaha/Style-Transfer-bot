import torch
import torchvision.transforms as transforms
from PIL import Image


rgb_mean = torch.tensor([0.485, 0.456, 0.406])
rgb_std = torch.tensor([0.229, 0.224, 0.225])


def preprocess(img, image_shape):
    img = Image.open(img)
    transformation = transforms.Compose([
        transforms.Resize(image_shape),
        transforms.ToTensor(),
        transforms.Normalize(mean=rgb_mean, std=rgb_std)])
    print(img.size)
    return transformation(img).unsqueeze(0)


def postprocess(img):
    img = img[0].to(rgb_std.device)
    img = torch.clamp(img.permute(1, 2, 0) * rgb_std + rgb_mean, 0, 1)
    return transforms.ToPILImage()(img.permute(2, 0, 1))