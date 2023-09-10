from sahi.slicing import slice_coco

slice_coco(
    coco_annotation_file_path='D:/Project/datasets/VisDrone/VisDrone2019-DET-val/coco_val.json',
    image_dir='D:/Project/datasets/VisDrone/VisDrone2019-DET-val/',
    output_coco_annotation_file_name='D:/Project/datasets/VisDrone/output_slice_val/coco.json',
    output_dir='D:/Project/datasets/VisDrone/output_slice_val/images/',
    overlap_width_ratio=0.15,
    overlap_height_ratio=0.15,
)
