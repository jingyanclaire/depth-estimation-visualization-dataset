# Depth Estimation Visualization Dataset
depth estimation datasets including Eth3d(forest), NYU, KITTI

This structure enables easy side-by-side model comparison for the same scene.

## Datasets Covered

### 1. **KITTI** (Outdoor Driving)
- Scene type: Outdoor urban driving scenarios
- Depth range: 0-80m
- Use case: Autonomous driving applications

### 2. **NYU Depth V2** (Indoor)
- Scene type: Indoor environments
- Depth range: 0-10m
- Use case: Indoor robotics and AR/VR

### 3. **ETH3D Forest** (Outdoor Nature)
- Scene type: Forest environments
- Depth range: 0-80m
- Use case: Outdoor navigation and environmental monitoring

### Organized Visualizations
Images grouped by source image, containing visualizations from multiple models:
```
{image_identifier}/
├── model_a.png
├── model_b.png
├── model_c.png
└── model_d.png
```

## Models Included

- **Depth Anything V1** (ViT-B, ViT-L)
- **Depth Anything V2** (ViT-B)
- **ZoeDepth** (NK variant)
- **Marigold** (Diffusion-based)

## Evaluation Metrics

All models are evaluated using standard depth estimation metrics:
- **δ1**
- RMSE, RMSE_log
- Absolute Relative Error (AbsRel)
- Square Relative Error (SqRel)

## Visualization Format

Each visualization includes:
- RGB input image
- Predicted depth map (aligned)
- Ground truth depth
- Error map
- Metrics overlay (δ1 score, category, depth ranges)
