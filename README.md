### Dataset Type Conversion

[coco-to-yolo.ipynb](coco-to-yolo.ipynb) contains code to convert JSON labels from [AIHub](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=71399) into YOLO text format.

- [house.json](house.json) : json object for matching class labels
- [house.yaml](house.yaml) : YAML file for Ultralytics HUB
- [htp.yaml](htp.yaml) : YAML file for HTP integrated version model

### How to train with Ultralytics
https://github.com/ultralytics/hub#1-create-a-dataset

### Result

Detection model based on YOLOv8n, pretrained on COCO 2017 dataset.

_Total-YOLOv8s, Total-YOLOv8m, Total-YOLOv8l is in progress._

| Model                                                                    | size<br><sup>(pixels) | mAP<sup>val<br>50 | mAP<sup>val<br>50-95 | Precision | Recall |
|--------------------------------------------------------------------------| --------------------- |-------------------|----------------------|-----------|--------| 
| [House](https://hub.ultralytics.com/models/GHxiQZJ0ZdMwnzpKuFGx)         | 640                   | **98.4**          | 91.2                 | 96.7      | 96.4   |
| [Tree](https://hub.ultralytics.com/models/Q4l6NK6huEkCVILp7QZu)          | 640                   | **98.2**          | 87.2                 | 96.7      | 95.6   |
| [PersonMale](https://hub.ultralytics.com/models/lBsj1qEmqUmVgf47gssJ)    | 640                   | **98.5**          | 84.7                 | 97.7      | 96.9   |
| [PersonFemale](https://hub.ultralytics.com/models/VmvvwkqZq7ShyaWfIKN9)  | 640                   | **98.5**          | 84.7                 | 97.9      | 96.8   |
| [Total-YOLOv8n](https://hub.ultralytics.com/models/JRzV3V15T2MWjq8oAP5T) | 640                   | **98.2**          | 87.0                 | 96.7      | 95.9   |
| [Total-YOLOv8s](https://hub.ultralytics.com/models/AsGy4VyYXfo4d7zlI6it) | 640                   | **98.5**          | 88.7                 | 97.3      | 96.7   |
| [Total-YOLOv8m](https://hub.ultralytics.com/models/c4NJ0r6F4gGXcrSnu80g) | 640                   | **98.7**          | 89.4                 | 97.4      | 97.1   |
| [Total-YOLOv8l](https://hub.ultralytics.com/models/U1x2TxEJOYkBW4QlkDqI) | 640                   | **98.7**          | 89.7                 | 97.5      | 97.1   |

#### Example - Total-YOLOv8n
- input
  - ![ex1.jpg](examples%2Fex1.jpg)
  - ![ex2.jpg](examples%2Fex2.jpg)
- output
  - ![htp-total-yolov8n-ex1.png](examples%2Fhtp-total-yolov8n-ex1.png)
  - ![htp-total-yolov8n-ex2.png](examples%2Fhtp-total-yolov8n-ex2.png)

<details><summary>YOLOv8 Detection models</summary>

See [Detection Docs](https://docs.ultralytics.com/tasks/detect/) for usage examples with these models.

| Model                                                                                | size<br><sup>(pixels) | mAP<sup>val<br>50-95 | Speed<br><sup>CPU ONNX<br>(ms) | Speed<br><sup>A100 TensorRT<br>(ms) | params<br><sup>(M) | FLOPs<br><sup>(B) |
| ------------------------------------------------------------------------------------ | --------------------- | -------------------- | ------------------------------ | ----------------------------------- | ------------------ | ----------------- |
| [YOLOv8n](https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt) | 640                   | 37.3                 | 80.4                           | 0.99                                | 3.2                | 8.7               |
| [YOLOv8s](https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8s.pt) | 640                   | 44.9                 | 128.4                          | 1.20                                | 11.2               | 28.6              |
| [YOLOv8m](https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8m.pt) | 640                   | 50.2                 | 234.7                          | 1.83                                | 25.9               | 78.9              |
| [YOLOv8l](https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8l.pt) | 640                   | 52.9                 | 375.2                          | 2.39                                | 43.7               | 165.2             |
| [YOLOv8x](https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8x.pt) | 640                   | 53.9                 | 479.1                          | 3.53                                | 68.2               | 257.8             |

- **mAP<sup>val</sup>** values are for single-model single-scale on [COCO val2017](http://cocodataset.org) dataset.
  <br>Reproduce by `yolo val detect data=coco.yaml device=0`
- **Speed** averaged over COCO val images using an [Amazon EC2 P4d](https://aws.amazon.com/ec2/instance-types/p4/) instance.
  <br>Reproduce by `yolo val detect data=coco128.yaml batch=1 device=0|cpu`
</details>
