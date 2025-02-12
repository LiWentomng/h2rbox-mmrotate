_base_ = ['../rotated_retinanet/rotated_retinanet_obb_r50_fpn_1x_dota_oc.py']

angle_version = 'oc'

model = dict(
    bbox_head=dict(assign_by_circumhbbox=angle_version),
    backbone=dict(
        frozen_stages=0,
        zero_init_residual=False,
        norm_cfg=dict(type='SyncBN', requires_grad=True),
        norm_eval=False,
        init_cfg=dict(
            type='Pretrained',
            checkpoint='/data/home/yangxue/wsl/work_dirs/moco_v2_200ep_pretrain.pth'))
    )

img_norm_cfg = dict(
    mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True)
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations', with_bbox=True),
    dict(type='RResize', img_scale=(1024, 1024)),
    dict(type='RRandomFlip', flip_ratio=0.5, version=angle_version),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='Pad', size_divisor=32),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_bboxes', 'gt_labels'])
]
data = dict(train=dict(pipeline=train_pipeline))
