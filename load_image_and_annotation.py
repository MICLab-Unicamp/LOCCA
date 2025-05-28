import os
import argparse
import nibabel as nib
import nrrd
import numpy as np
import matplotlib.pyplot as plt

'''
Requirements
	pip install nibabel pynrrd numpy matplotlib
'''

import os
import argparse
import nibabel as nib
import nrrd
import numpy as np
import matplotlib.pyplot as plt

def load_nifti(path):
    img = nib.load(path)
    return img.get_fdata(), img.affine

def load_nrrd(path):
    data, header = nrrd.read(path)
    return data, header

def visualize_slice(image, mask=None, slice_index=None):
    if slice_index is None:
        slice_index = image.shape[2] // 2

    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(image[:, :, slice_index], cmap='gray')
    plt.title('CT Image')
    plt.axis('off')

    if mask is not None:
        plt.subplot(1, 2, 2)
        plt.imshow(image[:, :, slice_index], cmap='gray')
        plt.imshow(mask[:, :, slice_index], cmap='jet', alpha=0.5)
        plt.title('Segmentation Mask')
        plt.axis('off')

    plt.tight_layout()
    plt.show()

def main(image_path, mask_path=None):
    print(f"Loading image: {image_path}")
    image, _ = load_nifti(image_path)

    mask = None
    if mask_path and os.path.exists(mask_path):
        print(f"Loading mask: {mask_path}")
        mask, _ = load_nrrd(mask_path)
        if image.shape != mask.shape:
            print("⚠️ Warning: Image and mask have different dimensions!")

    visualize_slice(image, mask)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Viewer for NIfTI images and NRRD masks.")
    parser.add_argument('-i', '--image', type=str, required=True, help='Path to the NIfTI image (.nii.gz)')
    parser.add_argument('-m', '--mask', type=str, help='(Optional) Path to the NRRD mask (.nrrd)')

    args = parser.parse_args()
    main(args.image, args.mask)
