import numpy as np

from tensorflow.keras.utils import load_img
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.vgg16 import decode_predictions

def verifyDocument(documentType):
  model = load_model('models/' + documentType)
  tf_document = load_img(
    'documents/document.jpeg',
    target_size=(180, 180),
  )
  document_array = img_to_array(tf_document)
  document_array = np.array([document_array])
  prediction = model.predict(document_array)

  document_class = np.argmax(prediction[0])

  if document_class != 0: return False

  return True