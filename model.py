import tensorflow as tf
import numpy as np


RESNET_model = tf.keras.models.load_model('model')

def predict(x):
    ##轉換圖片為張量
    image = x.resize((460, 460))
    image = tf.keras.preprocessing.image.img_to_array(image)

    ##圖片處理
    #圖片通道處理
    image = tf.expand_dims(image, axis=0)
    #像素質正規化
    image = tf.image.per_image_standardization(image)
    image = image /255.0
    #對比度處理
    image = tf.image.adjust_contrast(image,2)

    ##模型預測
    pred = RESNET_model.predict(image)
    ##預測結果轉換為標籤
    pred = np.argmax(pred, axis=1)
    result = 'Benign' if pred == [0] else 'Malignant'
    return(result)
