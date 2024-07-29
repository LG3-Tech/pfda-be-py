from deepface import DeepFace

def verifyImages():
  result = DeepFace.verify(
    img1_path = "images/image1.jpeg",
    img2_path = "images/image2.jpeg"
  )

  return result['verified']
