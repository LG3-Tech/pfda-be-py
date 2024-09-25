from deepface import DeepFace

def verifyImages():
  result = DeepFace.verify(
    img1_path = "image/image1.jpg",
    img2_path = "image/image2.jpg"
  )

  return result['verified']
