from sahi.model import Yolov5DetectionModel
from sahi.predict import get_sliced_prediction, predict, get_prediction
from sahi.scripts.coco_evaluation import evaluate

model_path = 'D:/Project/sahi-main/models/train_slice_original/weights/best.pt'  # 目标检测模型权重
detection_model = Yolov5DetectionModel(
    model_path=model_path,
    confidence_threshold=0.1,
    device="cuda:0",  # cpu or 'cuda:0'
)


# 0.1-10,0.2-9
# 使用目标检测模型对文件夹内所有图片进行预测、验证
def tph_slice(
        model_path=model_path,  # 目标检测模型权重
        img_predict: bool = True,  # 目标检测预测，按照predict->eval->error_evaluate的顺序 依次进行,其中一项为True其他则为False
        eval: bool = False,  # 对检测 结果验证
        postprocess_type: str = "NMS",  # NMS/GREEDYNMM
        predict_name='TPH',  # predict文件夹命名,保存在runs/predict/name
        no_sliced_prediction: bool = False,  # 是否使用slice，使用则为false，用于predict结果过程
        no_standard_prediction: bool = False,  # 是否使用FI，使用则为false
        source='D:/Project/datasets/VisDrone/VisDrone2019-DET-test/',  # 图片文件夹上级目录
        dataset_json_path='D:/Project/datasets/VisDrone/VisDrone2019-DET-test/coco.json',  # coco的json文件
        result_json_path='D:/Project/sahi-main/runs/predict/TPH/result.json',
        # 在predict时设置为空在进行predict后会生成result.json在runs/predict/name用于eval和error_evaluate
        out_dir='D:/Project/sahi-main/runs/eval/',  # eval和error_eval的保存目录
        postprocess_match_threshold=0.5,  # 阈值
        auto_slice_size=True,  # 是否自动适应slice大小,不自动调节则固定切片宽、高值
        slice_height='',
        slice_width='',
        overlap_height_ratio=0.15,  # 重叠率默认0.1
        overlap_width_ratio=0.15,  # 重叠率默认0.1
):
    if img_predict:
        predict(
            source=source,
            detection_model=detection_model,
            model_path=model_path,
            dataset_json_path=dataset_json_path,
            postprocess_type=postprocess_type,
            auto_slice_size=auto_slice_size,
            postprocess_match_threshold=postprocess_match_threshold,
            slice_height=slice_height,
            slice_width=slice_width,
            name=predict_name,
            no_sliced_prediction=no_sliced_prediction,
            no_standard_prediction=no_standard_prediction,
            overlap_height_ratio=overlap_height_ratio,
            overlap_width_ratio=overlap_width_ratio
        )

    # evaluate
    if eval:
        evaluate(
            dataset_json_path=dataset_json_path,
            result_json_path=result_json_path,
            out_dir=out_dir,
        )


# 对单一图片测试
def test(  # 对单张图片测试先修改main里的内容
        no_slice_predict: bool = False,  # 是否使用slice（无slice）
        image='D:/Project/1.jpg',  # 需要test的图像
        export_dir="D:/Project/",  # 图片输出目录
        file_name='yolov5s+SAHI',  # 图片文件名
        auto_slice_size=True,
        postprocess_type: str = "NMS",  # NMS/GREEDYNMM
        model_path='D:/Project/sahi-main/models/yolov5s.pt',  # 使用的模型.pt文件
):
    # yolov5
    detection_model.model_path = model_path
    if no_slice_predict:
        result = get_prediction(image=image, detection_model=detection_model)
        result.export_visuals(export_dir=export_dir, file_name=file_name)

    # slice
    if not no_slice_predict:
        result = get_sliced_prediction(
            image=image,
            detection_model=detection_model,
            postprocess_type=postprocess_type,
            auto_slice_size=auto_slice_size,
            postprocess_match_threshold=0.5,
            slice_height=343,
            slice_width=343,
            overlap_height_ratio=0.1,
            overlap_width_ratio=0.1
        )
        result.export_visuals(export_dir=export_dir, file_name=file_name)


if __name__ == "__main__":
    tph_slice()
    # test()  #如果要对单张图片实验则使用test()
