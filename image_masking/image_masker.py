import imageio
from skimage.transform import resize
import numpy as np
import matplotlib.pyplot as plt
from config import *


class ImageMasker:
    def __init__(self, image, mask, threshold=0.1):
        """
        This class expects an image in RGB format which can be easily converted to (1024x1024x3)
        Then it expects an mask in gray scale format which when converted to ndarray is (1024x1024)
        By default if the gray scale is 0.3 it will consider it as 1.0 and whitens (masks) it
        :param image:
        :param mask:
        :param threshold:
        """
        mask = imageio.imread(mask)
        image = resize(mask, (image_height, image_width), anti_aliasing=True)
        self.im = np.asarray(imageio.imread(image))
        try:
            rows, columns, channels = self.im.shape
            assert channels == 3
        except ValueError:
            print("Probably the input image is not in RGB format. Make sure it's in RGB")
            exit(1)
        mask_resized = resize(mask, (rows, columns), anti_aliasing=True)
        idx = (mask_resized <= threshold)
        for each_channel in range(channels):
            self.im[:, :, each_channel][idx] = 1.0
            self.im[:, :, each_channel][idx] = 1.0
            self.im[:, :, each_channel][idx] = 1.0

    def get_masked_image(self) -> np.ndarray:
        return self.im


if __name__ == "__main__":
    ImageMasker = ImageMasker('27.jpg', '00062_train.png')
    plt.imshow(ImageMasker.get_masked_image())
    plt.show()
