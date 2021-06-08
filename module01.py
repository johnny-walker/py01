import os
import utils
import utils.blurs as blrs
from utils.display.imageshow import Plot

if __name__ == '__main__':
    path = os.path.join(os.path.dirname(__file__), 'data/dog.jpeg')
    args = {}
    args['src'] = path
    args['kernel_size'] = 19
    args['show'] = True
    
    plot = Plot()

    img1 = utils.filter2DBlur(args)
    img2 = utils.averageBlur(args)
    plot.show_diff(img1, img2)

    img1 = blrs.gaussianBlur(args)    
    img2 = blrs.medianBlur(args)

    plot.show_diff(img1, img2)