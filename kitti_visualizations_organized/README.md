# KITTI Visualizations Organized by Image

This directory contains visualizations from multiple models organized by the original image.

## Structure

Each subdirectory is named after the base image identifier:
`{sequence}_{image}/`

Inside each directory, you'll find visualizations from different models:
- `{model_id}.png` - Visualization from each model

## Models Included

- dav2-vitb-kitti
- dav2-vitb-kitti-median
- zoedepth-k
- zoedepth-k-d1-60
- dav1-vits-kitti

## Statistics

- Total images: 148
- Models per image: 5
- Total visualizations: 740

## Organization Mode

Files were organized using: copy

## Example

```
2011_09_26_drive_0002_sync_0000000069/
├── dav2-vitb-kitti.png
├── dav2-vitb-kitti-median.png
├── zoedepth-k.png
├── zoedepth-k-d1.png
└── dav1-vits-kitti.png
```

## Usage

You can now easily compare different models' predictions for the same image by:
1. Opening all PNG files in a directory
2. Using image viewers that support side-by-side comparison
3. Writing scripts to generate comparison visualizations

## Metadata

See `organization_mapping.json` for complete file mappings.
