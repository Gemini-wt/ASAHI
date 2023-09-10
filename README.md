<div align="center">
<h1>
  ASAHI: Adaptive Slicing-Aided Hyper Inference for Small Object Detection in High-Resolution Remote Sensing Images
</h1>


<h4>
    <img width="700" alt="teaser" src="https://raw.githubusercontent.com/obss/sahi/main/resources/sliced_inference.gif">
</h4>

[![Paper](https://img.shields.io/badge/Paper-arxiv-white)](https://www.mdpi.com/2072-4292/15/5/1249/pdf?version=1677547894)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/release/python-390/)
</div>

## <div align="center">Overview</div>

Object detection and instance segmentation are by far the most important fields of applications in Computer Vision. However, detection of small objects and inference on large images are still major issues in practical usage. Here comes the SAHI to help developers overcome these real-world problems with many vision utilities.

| Command  | Description  |
|---|---|
| [predict](https://github.com/obss/sahi/blob/main/docs/cli.md#predict-command-usage)  | perform sliced/standard video/image prediction using any [yolov5](https://github.com/ultralytics/yolov5)/[mmdet](https://github.com/open-mmlab/mmdetection)/[detectron2](https://github.com/facebookresearch/detectron2)/[huggingface](https://huggingface.co/models?pipeline_tag=object-detection&sort=downloads) model |
| [predict-fiftyone](https://github.com/obss/sahi/blob/main/docs/cli.md#predict-fiftyone-command-usage)  | perform sliced/standard prediction using any [yolov5](https://github.com/ultralytics/yolov5)/[mmdet](https://github.com/open-mmlab/mmdetection)/[detectron2](https://github.com/facebookresearch/detectron2)/[huggingface](https://huggingface.co/models?pipeline_tag=object-detection&sort=downloads) model and explore results in [fiftyone app](https://github.com/voxel51/fiftyone) |
| [coco slice](https://github.com/obss/sahi/blob/main/docs/cli.md#coco-slice-command-usage)  | automatically slice COCO annotation and image files |
| [coco fiftyone](https://github.com/obss/sahi/blob/main/docs/cli.md#coco-fiftyone-command-usage)  | explore multiple prediction results on your COCO dataset with [fiftyone ui](https://github.com/voxel51/fiftyone) ordered by number of misdetections |
| [coco evaluate](https://github.com/obss/sahi/blob/main/docs/cli.md#coco-evaluate-command-usage)  | evaluate classwise COCO AP and AR for given predictions and ground truth |
| [coco analyse](https://github.com/obss/sahi/blob/main/docs/cli.md#coco-analyse-command-usage)  | calcualate and export many error analysis plots |
| [coco yolov5](https://github.com/obss/sahi/blob/main/docs/cli.md#coco-yolov5-command-usage)  | automatically convert any COCO dataset to [yolov5](https://github.com/ultralytics/yolov5) format |


### Installation
From pip:
```
pip install -r requrirements.txt
pip install opencv-python==4.6.0.66
```


<details closed>
<summary>
<big><b>Installation details:</b></big>
</summary>

- Install `sahi` using pip:

```console
pip install sahi
```

- On Windows, `Shapely` needs to be installed via Conda:

```console
conda install -c conda-forge shapely
```

- Install your desired version of pytorch and torchvision:

```console
conda install pytorch=1.10.2 torchvision=0.11.3 cudatoolkit=11.3 -c pytorch
```
  
- Install your desired detection framework (yolov5):

```console
pip install yolov5==6.1.3
```

- Install your desired detection framework (mmdet):

```console
pip install mmcv-full==1.5.3 -f https://download.openmmlab.com/mmcv/dist/cu113/torch1.10.0/index.html
```

```console
pip install mmdet==2.25.0
```

- Install your desired detection framework (detectron2):

```console
pip install detectron2 -f https://dl.fbaipublicfiles.com/detectron2/wheels/cu113/torch1.10/index.html
```

- Install your desired detection framework (huggingface):

```console
pip install transformers timm
```

</details>

### Framework Agnostic Sliced/Standard Prediction

<img width="700" alt="sahi-predict" src="https://user-images.githubusercontent.com/34196005/149310540-e32f504c-6c9e-4691-8afd-59f3a1a457f0.gif">

Find detailed info on `sahi predict` command at [cli.md](docs/cli.md#predict-command-usage).

Find detailed info on video inference at [video inference tutorial](https://github.com/obss/sahi/issues/457).

Find detailed info on image/dataset slicing utilities at [slicing.md](docs/slicing.md).

### Error Analysis Plots & Evaluation

<img width="700" alt="sahi-analyse" src="https://user-images.githubusercontent.com/34196005/149537858-22b2e274-04e8-4e10-8139-6bdcea32feab.gif">

Find detailed info at [Error Analysis Plots & Evaluation](https://github.com/obss/sahi/issues/356).

### Interactive Visualization & Inspection

<img width="700" alt="sahi-fiftyone" src="https://user-images.githubusercontent.com/34196005/149321540-e6ddd5f3-36dc-4267-8574-a985dd0c6578.gif">

Find detailed info at [Interactive Result Visualization and Inspection](https://github.com/obss/sahi/issues/357).

### Other utilities

Find detailed info on COCO utilities (yolov5 conversion, slicing, subsampling, filtering, merging, splitting) at [coco.md](docs/coco.md).

Find detailed info on MOT utilities (ground truth dataset creation, exporting tracker metrics in mot challenge format) at [mot.md](docs/mot.md).

## <div align="center">Citation</div>

If you use this package in your work, please cite it as:
```
@article{Zhang2023AdaptiveSH,
  title={Adaptive Slicing-Aided Hyper Inference for Small Object Detection in High-Resolution Remote Sensing Images},
  author={Hao Zhang and Chuanyan Hao and Wanru Song and Bo Jiang and Baozhu Li},
  journal={Remote. Sens.},
  year={2023},
  volume={15},
  pages={1249},
  url={https://api.semanticscholar.org/CorpusID:257247854}
}
```



