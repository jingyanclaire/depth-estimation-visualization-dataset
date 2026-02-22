import numpy as np
from pathlib import Path


def convert_kitti(depth: np.ndarray) -> np.ndarray:
    """
    KITTI: clip to [0, 80m]
    """
    depth = np.clip(depth, 0.0, 80.0)
    return depth.astype(np.float32)


def convert_nyu(depth: np.ndarray) -> np.ndarray:
    """
    NYU: store as (W, H)=(640,480)，converted to (H, W)=(480,640)
    """
    if depth.shape == (640, 480):
        depth = depth.T
    depth = np.clip(depth, 0.0, 10.0)
    return depth.astype(np.float32)


def convert_forest(depth: np.ndarray) -> np.ndarray:
    """
    ETH3D Forest
    """
    return depth.astype(np.float32)


CONVERTERS = {
    "kitti":  convert_kitti,
    "nyu":    convert_nyu,
    "forest": convert_forest,
}


def convert_storage(storage_dir: str, output_dir: str, dataset: str):
    """
    scan {storage_dir}/{image_identifier}/{model}.npy to {output_dir}/{image_identifier}/{model}.npy
    """
    assert dataset in CONVERTERS, f"unknown dataset: {dataset}"
    src_root = Path(storage_dir)
    dst_root = Path(output_dir)
    converter = CONVERTERS[dataset]

    converted = 0
    for img_dir in sorted(src_root.iterdir()):
        if not img_dir.is_dir():
            continue
        for npy_file in sorted(img_dir.glob("*.npy")):
            depth = np.load(npy_file)
            depth = converter(depth)
            dst = dst_root / img_dir.name / npy_file.name
            dst.parent.mkdir(parents=True, exist_ok=True)
            np.save(dst, depth)
            converted += 1

    print(f"[{dataset}] finished：{converted} npy to {dst_root}")


if __name__ == "__main__":
    # KITTI
    convert_storage(
        storage_dir="/mnt/root/Marigold/kitti_npy_storage",
        output_dir="/mnt/root/Marigold/kitti_npy_converted",
        dataset="kitti",
    )

    # NYU
    convert_storage(
        storage_dir="/mnt/root/Marigold/nyu_npy_storage",
        output_dir="/mnt/root/Marigold/nyu_npy_converted",
        dataset="nyu",
    )

    # ETH3D Forest
    convert_storage(
        storage_dir="/mnt/root/Marigold/forest_npy_storage",
        output_dir="/mnt/root/Marigold/forest_npy_converted",
        dataset="forest",
    )
