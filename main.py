
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QLabel, QHBoxLayout, QPushButton, QListWidget, QVBoxLayout
import os
from PIL import Image, ImageFilter
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class ImageProcessor():
    def __init__(self):
        self.filename = None
        self.image = None
        self.dir = None
        self.save_dir = 'Modified/'
    def loadImage(self, filename):
        self.filename = filename
        file_path = os.path.join(workdir, filename)
        self.image = Image.open(file_path)
    def showImage(self, path):
        label.hide()
        pixmapimage = QPixmap(path)
        w, h = label.width(), label.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        label.setPixmap(pixmapimage)
        label.show()
    def do_bw(self):
        self.image = self.image.convert('L')
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    def saveImage(self):
        path = os.path.join(workdir, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)
    def do_flip(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_left(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_right(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_sharpen(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    

def showChosenImage():
    if listt.currentRow() >= 0:
        filename = listt.currentItem().text()
        workimage.loadImage(filename)
        image_path = os.path.join(workdir, workimage.filename)
        workimage.showImage(image_path)

    
    

    

def filter(files, extensions):
    result = []
    for file in files:
        for extension in extensions:
            if file.endswith(extension):
                result.append(file)
    return result
workdir = ''
def showFilenamesList():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
    extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    filenames = filter(os.listdir(workdir), extensions)
    listt.clear()
    listt.addItems(filenames)



app = QApplication([])
main_win = QWidget()
# main_win.setWindowTitle('Пустое окно')
 
label = QLabel('картинка')
qbox = QHBoxLayout()
lpush = QPushButton('лево')
rpush = QPushButton('право')
mpush = QPushButton('зеркало')
rezpush = QPushButton('резкость')
chpush = QPushButton('Ч/Б')
ppush = QPushButton('папка')
listt = QListWidget()
vbox = QVBoxLayout()
vvbox = QVBoxLayout()
vbox.addWidget(ppush)
vbox.addWidget(listt)
qbox.addWidget(lpush)
qbox.addWidget(rpush)
qbox.addWidget(mpush)
qbox.addWidget(rezpush)
qbox.addWidget(chpush)
vvbox.addWidget(label)
vvbox.addLayout(qbox)

qqbox = QHBoxLayout()
qqbox.addLayout(vbox)
qqbox.addLayout(vvbox)


workimage = ImageProcessor()


main_win.setLayout(qqbox)
listt.currentRowChanged.connect(showChosenImage)
chpush.clicked.connect(workimage.do_bw)
lpush.clicked.connect(workimage.do_left)
rpush.clicked.connect(workimage.do_right)
mpush.clicked.connect(workimage.do_flip)
rezpush.clicked.connect(workimage.do_sharpen)
ppush.clicked.connect(showFilenamesList)
main_win.show()
app.exec()