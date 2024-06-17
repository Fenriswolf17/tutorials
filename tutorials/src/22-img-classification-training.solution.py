from utils.get_image_from_web import grab_image
from ultralytics import YOLO  # pip install ultralytics needed
import cv2


# TODO retrieve multiple images by using tutorials/src/utils/duckduckgo_image_search.py


# TODO prepare images for training
# create folder structure as shown here: https://docs.ultralytics.com/datasets/classify/ with "train" and "test folder

# TODO train model
# base model needs to be downloaded first
def train_model(data_path, num_epochs):
    # TODO download base model from https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8s-cls.pt
    model = YOLO("./tutorials/data/models/yolov8s-cls.pt")
    results = model.train(data=data_path, epochs=num_epochs)
    return results


# TODO Test your new model
def test_model(image_descriptors, model_path):
    model = YOLO(model_path)
    index = 0
    for image_type in image_descriptors:
        query = image_type  # change to 1 for other category
        #TODO: find your own test images and adjust path
        img = cv2.imread(query+".jpg", cv2.IMREAD_COLOR)

        # detect objects in image
        results = model.predict(source=img, stream=True, show=True)  # detect objects in img
        # show results
        for result in results:
            print("Result for " + query + ": " + str(result.probs.data[index]))
        index += 1
        cv2.imshow("Query", img)
        cv2.waitKey(0)


def main():

    # define categories
    image_descriptors = ["bird", "forest"]

    # define data path
    data_path = './tutorials/data/myimages'
    # define number of training epochs
    num_epochs = 5
    # run the training process
    results = train_model(data_path, num_epochs)
    # show results
    print(results)

    # TODO: test the trained model manually (adjust path to best result)
    model_path = "./runs/classify/train4/weights/best.pt"  # obey number of training runs
    test_model(image_descriptors, model_path)


if __name__ == "__main__":
    main()
