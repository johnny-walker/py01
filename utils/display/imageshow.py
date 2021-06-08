from matplotlib import pyplot as plt

class Plot:
    def show_diff(this, img, dst):
        plt.subplot(121), plt.imshow(img), plt.title('Image 1')
        plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(dst), plt.title('Image 2')
        plt.xticks([]), plt.yticks([])
        plt.show()
