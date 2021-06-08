import utils
import utils.blurs as brs
from utils.display.imageshow import Plot


if __name__ == '__main__':
    args = {}
    args['src'] = 'data/dog.jpeg'
    args['kernel_size'] = 19
    args['show'] = True
    
    plot = Plot()

    img1 = brs.filter2DBlur(args)
    img2 = brs.averageBlur(args)
    plot.show_diff(img1, img2)

    img1 = brs.gaussianBlur(args)    
    img2 = brs.medianBlur(args)

    plot.show_diff(img1, img2)