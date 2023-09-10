<div align="center">
<h1>
  ASAHI: Adaptive Slicing-Aided Hyper Inference for Small Object Detection in High-Resolution Remote Sensing Images
</h1>


<h4>
  This is the official repository for ASAHI.

Project page: https://www.mdpi.com/2072-4292/15/5/1249#metrics
</h4>

[![Paper](https://img.shields.io/badge/Paper-arxiv-white)](https://www.mdpi.com/2072-4292/15/5/1249/pdf?version=1677547894)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/release/python-390/)
</div>


### Installation
From pip:
```
pip install -r requrirements.txt
pip install opencv-python==4.6.0.66
pip install torch==1.10.1 torchvision==0.11.2 torchaudio==0.10.1
```

From conda:
```
conda install opencv-python==4.6.0.66
conda install pytorch==1.10.1 torchvision==0.11.2 torchaudio==0.10.1 cudatoolkit=11.3 -c pytorch -c conda-forge
```


### Framework Agnostic Sliced/Standard Prediction
```
Test:
python test.py
```




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



