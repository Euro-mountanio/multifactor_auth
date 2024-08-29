from deepface import DeepFace
class recognition:
    def __init__(self):
        pass

    # check  if the image is a  database
    def recognise(self, image):
        self.image = image
        dfs = DeepFace.find(img_path=image, db_path="C:/workspace/my_db")
        return dfs
    # function to test if two images are of the same person
    def testRecognition(self, image1, image2):
        self.image1 = image1
        self.image2= image2
        dfs = DeepFace.verify(img1_path=image1, img2_path=image2)
        return dfs
    # analyse then image and get details like emotion, gender, age estimate and race
    def analyse(self, image_path):
        self.image_path = image_path
        objs = DeepFace.analyze(img_path= image_path,
                                actions=['age', 'gender', 'race', 'emotion']
                                )
        return objs

    def stream(self): 
        try:
            result = DeepFace.stream("face_database")
            return result
        except :
            result = " failed to stream "
            return result



