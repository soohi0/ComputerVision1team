made it in Colab.

## How To yolo-v3

0. mount
1. put imputImages in directory (/content/drive/MyDrive/ ..)
2. If you need modify path, do it
3. png images are read. if jpg, jpeg.., modify imgfiles 확장자

## How To pp-yolo
1. if you use in cpu environment, use this.
but if you use in gpu environment, please modify some code
```
!export CUDA_VISIBLE_DEVICES=0
!python tools/infer.py -c configs/ppyolo/ppyolo_r50vd_dcn_1x_coco.yml -o use_gpu=false weights=https://paddledet.bj.bcebos.com/models/ppyolo_r50vd_dcn_1x_coco.pdparams --infer_img=demo/road2.jpg
```
change this code to 
```
!export CUDA_VISIBLE_DEVICES=0
!python tools/infer.py -c configs/ppyolo/ppyolo_r50vd_dcn_1x_coco.yml -o use_gpu=true weights=https://paddledet.bj.bcebos.com/models/ppyolo_r50vd_dcn_1x_coco.pdparams --infer_img=demo/road2.jpg
```
2. you need to modify image file name which you will use.
```
!python tools/infer.py -c configs/ppyolo/ppyolo_r50vd_dcn_1x_coco.yml -o use_gpu=true weights=https://paddledet.bj.bcebos.com/models/ppyolo_r50vd_dcn_1x_coco.pdparams --infer_img=demo/road2.jpg # <- change this image name and put on this image on the directory same with this code.
```
