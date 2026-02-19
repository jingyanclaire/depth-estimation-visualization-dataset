# ETH3D Forest Visualizations Organized by Image

This directory contains visualizations from multiple models organized by the original image.

## Structure

Each subdirectory is named after the base image identifier:
`{camera}_{timestamp}/`

Inside each directory, you'll find visualizations from different models:
- `{model_id}.png` - Visualization from each model

## Models Included

- marigold
- depth-anything-v1-vitl
- zoedepth-nk
- depth-anything-v2-vitb

## Statistics

- Total images: 147
- Models per image: up to 4
- Total visualizations: 588

## Organization Mode

Files were organized using: copy

## Example

```
cam0_1474982922066603972/
├── marigold.png
├── depth-anything-v1-vitl.png
├── zoedepth-nk.png
└── depth-anything-v2-vitb.png
```

## Usage

You can now easily compare different models' predictions for the same image by:
1. Opening all PNG files in a directory
2. Using image viewers that support side-by-side comparison
3. Writing scripts to generate comparison visualizations

## Metadata

See `organization_mapping.json` for complete file mappings.
