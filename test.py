"""
Predict an image using maskrcnn

"""
import cv2
import argparse
from detectron2.config import get_cfg
from detectron2.engine import DefaultPredictor
from detectron2 import model_zoo
from detectron2.utils.visualizer import Visualizer, ColorMode
from detectron2.data import MetadataCatalog
from detectron2.data.detection_utils import read_image

def main():
    # input arguments
    parser = argparse.ArgumentParser(description="Simple Mask R-CNN Inference")
    parser.add_argument("--image", required=True, help="Input image file path")
    args = parser.parse_args()
    img_path = args.image

    # build config
    cfg = get_cfg()
    cfg.merge_from_file(model_zoo.get_config_file(
        "COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml"
    ))
    cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url(
        "COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml"
    )
    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5  # confidence threshold
    cfg.MODEL.DEVICE = "cuda"   # or "cpu"

    # define predictor
    predictor = DefaultPredictor(cfg)

    # load image
    image = read_image(img_path, format="BGR")

    # inference
    outputs = predictor(image)

    # visualization
    metadata = MetadataCatalog.get(cfg.DATASETS.TRAIN[0])
    v = Visualizer(image[:, :, ::-1], metadata=metadata, instance_mode=ColorMode.IMAGE)
    out = v.draw_instance_predictions(outputs["instances"].to("cpu"))
    result = out.get_image()[:, :, ::-1]

    # show result 
    cv2.namedWindow("Detection Result", cv2.WINDOW_NORMAL)
    cv2.imshow("Detection Result", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # save result 
    cv2.imwrite("test_result.jpg", result)
    print("Saved detection result to test_result.jpg")

if __name__ == "__main__":
    main()
