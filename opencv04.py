import cv2

def save_video(argv=None):
    if argv is not None:
        print(argv)
    print('OpenCV 版本:',cv2.__version__)
    '''
    cv2.VideoWriter() 
    第一個參數是指定輸出的檔名，例如：下列範例中的 output.avi，
    第二個參數為指定 FourCC，
    第三個參數為 fps 影像偵率，
    第四個參數為 frameSize 影像大小，
    最後參數代表是否要存彩色，否則就存灰階，預設為 true
    '''
    video = cv2.VideoCapture(argv)
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    out = cv2.VideoWriter('output/output.avi', fourcc, 30.0, (640,  480))  
    while (video.isOpened()):
        ret, frame = video.read()
        if ret == True:
            out.write(frame)
            cv2.imshow('frame', frame)

            key = cv2.waitKey(1)
            # ESC
            if key == 27:
                break

        else:
            break

    video.release()
    out.release()


if __name__ == '__main__':
    save_video('data/girls.mp4')