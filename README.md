# LOCCA: Lung Lobes of COVID-19 and Cancer Patients Annotationed CT Dataset

This repository contains medical image files, annotations, visualization scripts, and a tutorial to assist with data manipulation and analysis. The files are organized to support studies and experiments with biomedical imaging, particularly in lung computed tomography (CT).

The main formats used here are:

    NIfTI (.nii, .nii.gz): widely adopted format in neuroimaging and 3D medical imaging.

    NRRD (.nrrd): commonly used for storing medical annotations, such as manual segmentations.

---

# Manual annotations of the pulmonary lobes

Manual annotations of the pulmonary lobes (or manual segmentations) serve as precise anatomical references created by experts and have multiple important purposes, especially in clinical, academic, and artificial intelligence algorithm development contexts.

**🖋️ Manual segmentation of the lung lobes enables**

    - Ground truth for training and evaluating models
    - Creation of public annotated datasets
    - Clinical support in complex cases

**🫁 Automatic segmentation of the lung lobes enables**

    - Detailed anatomical assessment
    - Disease diagnosis and quantification
    - Support for artificial intelligence
    - Surgical and treatment planning
    - Facilitates comparison of scans over time, enabling tracking of disease progression or regression by lobe.
---

## LOCCA dataset location

The dataset can be downloaded directly via the following link:

> [LOCCA](https://redu.unicamp.br/dataset.xhtml?persistentId=doi:10.25824/redu/ORXJKS)

## Repository Contents

1. **Compressed folder with annotations in NRRD format (`.nrrd`)**
   - Two compressed folder containing **segmented annotations** of the medical images.
   - Folder with files used to represent anatomical masks such as lung lobes.
   - Compatible with visualization and editing software like **ITK-Snap** and **3D Slicer**.

2. **Compressed folder with Volumetric Image in NIfTI format (`.nii.gz`)**
   - Folder containing the high-resolution CT volumes of the HCU dataset.
   - Widely used format in medical imaging, compatible with **NiBabel**, **3D Slicer**, **ITK-Snap**, among others.

3. **Compressed folder containing files and scripts**
   - Contains **Python scripts** with examples of loading, visualizing, and analyzing the images and annotations.
   - It also includes a guide on how to use the ITK-SNAP software.
   - Includes plots, 2D/3D visualizations, and basic analyses using libraries such as `nibabel`, `matplotlib`, `numpy`, `SimpleITK`, and `itk`.

4. **Tutorial PDF**
   - Practical guide on how to use **ITK-Snap** to view and edit images and annotations.
   - Step-by-step instructions with screenshots.

---

## Recommended Software

### 1. **ITK-Snap**
- Free software for semi-automatic segmentation and annotation of medical images.
- Supports `.nii.gz` and `.nrrd` files with overlay visualization.
- Website: [http://www.itksnap.org](http://www.itksnap.org)

### 2. **3D Slicer**
- Open-source platform for 3D visualization and analysis of medical data.
- Supports multiple formats including `.nrrd` and `.nii.gz`.
- Allows quantitative analysis, segmentation, and 3D rendering.
- Website: [https://www.slicer.org](https://www.slicer.org)

### 3. **Python (Jupyter Notebooks)**
- Interactive environment for developing and visualizing data using Python scripts.
- Useful libraries:
  - `nibabel`: to read `.nii.gz` files
  - `simpleitk` / `itk`: for medical image processing
  - `numpy`, `matplotlib`: for analysis and visualization
- Recommended tools: **JupyterLab** or **VS Code**

---

## Requirements to Run the Notebooks

Install the following packages using `pip` or `conda`:

```bash
pip install nibabel simpleitk numpy matplotlib jupyter pynrrd
```

Or with Conda:

```bash
conda install -c conda-forge nibabel simpleitk matplotlib jupyter pynrrd
```

---

## How to Visualize the Images

1. **In ITK-Snap**:
   - Load the `.nii.gz` file as the main image.
   - Load the `.nrrd` files as additional segmentations.
   - Use the PDF tutorial for detailed guidance.

2. **In 3D Slicer**:
   - Go to `Add Data` and select both the image and annotation files.
   - Use the segmentation and 3D visualization modules.

3. **In Jupyter Notebook**:
   - Run the provided notebook.
   - Visualize image slices and segmentations or generate basic 3D renderings.
   - The images and their annotations can also be read using NumPy, with Python code.

---

## File Structure

```
📦 annotations_HCU.zip              # Annotations for the HCU dataset
 ├── locca_covid_001_label.nrrd
 ├── locca_covid_002_label.nrrd
 ├── locca_covid_003_label.nrrd
     .
     .
     .
 └── locca_covid_030_label.nrrd

📦 annotations_Task06-Lung.zip       # Annotations for the Task06-Lung dataset
 ├── lung_001_label.nrrd
 ├── lung_002_label.nrrd
 ├── lung_003_label.nrrd
     .
     .
     .
 └── lung_096_label.nrrd

📦 images_HCU.zip                    # Volumetric images of the HCU dataset
 ├── locca_covid_001.nii.gz
 ├── locca_covid_002.nii.gz
 ├── locca_covid_003.nii.gz
     .
     .
     .
 └── locca_covid_030.nii.gz

📦 scripts.zip
 ├── 📁 images/                    # Folder containing the images generated by the scripts
 ├── 📁 input/                     # Folder containing input files for running the scripts
 ├── 📁 output_HCU/                # Folder containing output files generated during the execution of the scripts on the HCU dataset
 ├── 📁 output_Task06/             # Folder containing output files generated during the execution of the scripts on the Task06-Lung dataset
 ├── dataset_HCU.ipynb             # Jupyter Notebook with analysis scripts of the HCU dataset
 ├── dataset_Task06.ipynb          # Jupyter Notebook with analysis scripts of the Task06-Lung dataset
 ├── intensities_and_slices.ipynb  # Jupyter Notebook with analysis scripts of the HCU and Task06-Lung datasets
 ├── ITK-Snap_guide.pdf            # PDF tutorial for ITK-Snap usage
 └── load_image_and_annotation.py  # Script to load CT images and their annotations using the Python environment. The requirements are listed in the file header.
```

---

## Instructions for Using the Script

This script allows you to load and visualize 3D CT scans along with their corresponding annotations (e.g., segmentation masks). It is intended for medical imaging tasks using Python.

▶️ **How to Run the Script using the terminal**

```bash
python load_image_and_annotation.py -image data/images/patient_001.nii.gz --mask data/labels/patient_001.nrrd
```

🖼️ **ITK-Snap**

ITK-Snap is a free, open-source software for semi-automatic and manual segmentation of 3D medical images. It supports common formats like NIfTI, DICOM, MetaImage, among others, and allows visualization of volumetric images, creation of segmentation masks, and saving results for further analysis.

   - View ITK-Snap guide.pdf

---

# Comparative Analysis of Datasets with Manual Annotations of Pulmonary Lobes in CT Images

| Dataset                         | Cases with annotations           | Included Pathologies                 | Annotations Data Format | Image Data Format | Source |
|---------------------------------|:---------------------------:|:--------------------------------------:|:--------------------:|:-------------------:|:--------------------------------------------------------------------------------:|
| **LOCCA - HCU**                 | 30 | COVID-19 | NRRD | NIfTI | [LOCCA-HCU](https://github.com/MICLab-Unicamp/LOCCA) |
| **LOCCA - Cancer**              | 30 | Cancer   | NRRD | NIfTI | [LOCCA-Cancer](https://github.com/MICLab-Unicamp/LOCCA) and [MSD](http://medicaldecathlon.com) |
| **Hao Tang and Chupeng Zhang and Xiaohui Xie**  | 50 | Cancer | NIfTI | NIfTI | [LUNA16 Challenge](https://github.com/deep-voxel/automatic_pulmonary_lobe_segmentation_using_deep_learning) |

---

## LobePrior 

[LobePrior: Segmenting Lung Lobes on CT Images with Severe Pulmonary Abnormalities](https://github.com/MICLab-Unicamp/LobePrior)

This repository contains the implementation of LobePrior, a method for automated lung lobe segmentation in computed tomography (CT) scans, specifically designed to handle cases with severe pulmonary abnormalities.

Accurate lung and lobe segmentation plays a key role in the diagnosis and monitoring of pulmonary diseases, such as COVID-19-induced pneumonia and lung cancer. However, segmenting lung lobes remains a challenge due to the frequent invisibility or distortion of lobar fissures in abnormal cases. LobePrior addresses this issue by combining deep neural networks with probabilistic models to guide the segmentation process, even in the presence of incomplete or missing fissure information.

---

## License

This material is distributed for academic and research purposes only. Please check the usage terms of the included data and tools.

---

## Contact

Jean A. Ribeiro  
University of Campinas (Unicamp)  
Email: j265739@dac.unicamp.br

## Citation

``` 
@DATASET{redu_ORXJKS_2025,
	author = {Jean Antonio Ribeiro and Leticia Rittner and Diedre Santos do Carmo and Simone Appenzeller and Ricardo Siufi Magalhães and Sergio San Juan Dertkigil and Fabiano Reis},
	publisher = {Repositório de Dados de Pesquisa da Unicamp},
	title = {{LOCCA: Manual annotations for lung lobes in CT images of patients with cancer and COVID-19}},
	year = {2025},
	version = {V1},
	doi = {10.25824/redu/ORXJKS},
	url = {https://doi.org/10.25824/redu/ORXJKS}
}
``` 
