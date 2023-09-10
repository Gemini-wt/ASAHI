<div align="center">
<h1>
  ASAHI: Adaptive Slicing-Aided Hyper Inference for Small Object Detection in High-Resolution Remote Sensing Images
  
</h1>

<h4>
    <img width="700" alt="teaser" src="https://github.com/Gemini-wt/ASAHI/blob/e72677bbf86e558eb40edad74e58f684f9caa65e/show/tph%2Bsahi.png">
</h4>
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


### Command
```
Test:
python test.py
```




### Error Analysis Plots & Evaluation

<img width="700" alt="ASAHI-fiftyone" src="https://github.com/Gemini-wt/ASAHI/blob/e72677bbf86e558eb40edad74e58f684f9caa65e/show/evaluate.png">


### Interactive Visualization & Inspection

<img width="700"  src="https://github.com/Gemini-wt/ASAHI/blob/6e315492129022d1271910bf391f147ab1095dca/show/0000216_00520_d_0000001.png">
<img width="700"  src="https://github.com/Gemini-wt/ASAHI/blob/6e315492129022d1271910bf391f147ab1095dca/show/0000271_05401_d_0000399.png">
<img width="700"  src="https://github.com/Gemini-wt/ASAHI/blob/6e315492129022d1271910bf391f147ab1095dca/show/0000287_02001_d_0000769.png">
<img width="700"  src="https://github.com/Gemini-wt/ASAHI/blob/6e315492129022d1271910bf391f147ab1095dca/show/0000287_03401_d_0000776.png">
<img width="700"  src="https://github.com/Gemini-wt/ASAHI/blob/6e315492129022d1271910bf391f147ab1095dca/show/3.png">
<img width="700"  src="https://github.com/Gemini-wt/ASAHI/blob/6e315492129022d1271910bf391f147ab1095dca/show/5555.png">
<img width="700"  src="https://github.com/Gemini-wt/ASAHI/blob/c5468c44d4255f90def092158f15a8cbb6f2eb76/show/xview%400.5x.png">


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



