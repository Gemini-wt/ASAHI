from sahi.scripts.coco_error_analysis import analyse


def erorr_evaluate(
        erorr_evaluate: bool = True,
        dataset_json_path='D:/Project/datasets/VisDrone/VisDrone2019-DET-test/coco.json',  # coco的json文件
        result_json_path='D:/Project/sahi-main/runs/predict/TPH/result.json',
        out_dir: str = 'D:/Project/sahi-main/runs/error_eval/',
):
    #  error_evaluate
    if erorr_evaluate:
        analyse(
            dataset_json_path=dataset_json_path,
            result_json_path=result_json_path,
            out_dir=out_dir,
        )


if __name__ == '__main__':
    erorr_evaluate()
