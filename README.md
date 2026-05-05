# LOCCA: Manually Annotated CT Dataset of Lung LObes in COVID-19 and CAncer Patients

This repository contains medical image files, annotations, visualization scripts, and a tutorial to assist with data manipulation and analysis. The files are organized to support studies and experiments with biomedical imaging, particularly in lung computed tomography (CT). The associated article is available at:

> [Descriptor: Manually Annotated CT Dataset of Lung Lobes in COVID-19 and Cancer Patients (LOCCA)](https://ieeexplore.ieee.org/document/11029450)


### 🦠 COVID-19 Cases

| CT Scan | Lobar Mask |
|--------|------------|
| ![](images/covid_ct_1.png) | ![](images/covid_mask_1.png) |
| ![](images/covid_ct_2.png) | ![](images/covid_mask_2.png) |
| ![](images/covid_ct_3.png) | ![](images/covid_mask_3.png) |

---

### 🎗️ Lung Cancer Cases

| CT Scan | Lobar Mask |
|--------|------------|
| ![](images/cancer_ct_1.png) | ![](images/cancer_mask_1.png) |
| ![](images/cancer_ct_2.png) | ![](images/cancer_mask_2.png) |
| ![](images/cancer_ct_3.png) | ![](images/cancer_mask_3.png) |

---


The main formats used here are:

    NIfTI (.nii, .nii.gz): widely adopted format in neuroimaging and 3D medical imaging.

    NRRD (.nrrd): commonly used for storing medical annotations, such as manual segmentations.


---

# Manual annotations

Manual annotations of the pulmonary lobes (or manual segmentations) serve as precise anatomical references created by experts and have multiple important purposes, especially in clinical, academic, and artificial intelligence algorithm development contexts.

**🖋️ Manual segmentation of the lung lobes enables**

    - Ground truth for training and evaluating models
    - Clinical support in complex cases
    - Creation of publicly annotated datasets that serve as a basis for comparisons between algorithms performing automatic segmentation of lung lobes

**🫁 Automatic segmentation of the lung lobes enables**

    - Detailed anatomical assessment
    - Disease diagnosis and quantification
    - Support for artificial intelligence
    - Surgical and treatment planning
    - Facilitates comparison of scans over time, enabling tracking of disease progression or regression by lobe.
---

## LOCCA dataset location

The dataset can be downloaded directly via the following link:

> [LOCCA: Manually Annotated CT Dataset of Lung LObes in COVID-19 and CAncer Patients](https://redu.unicamp.br/dataset.xhtml?persistentId=doi:10.25824/redu/ORXJKS)

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
   - Includes plots, 2D/3D visualizations, and basic analyses using libraries such as `nibabel`, `matplotlib`, `numpy`, and `SimpleITK`.
   - All **.ipynb** (Jupyter Notebooks) files can be viewed directly in the browser via GitHub, without the need for download.

4. **Tutorial PDF**
   - Practical guide on how to use **ITK-Snap** to view and edit images and annotations.
   - Step-by-step instructions with screenshots.

---

## Recommended software for image manipulation

### 1. **ITK-Snap**
- Free software for semi-automatic segmentation and annotation of medical images.
- Supports `.nii.gz` and `.nrrd` files with overlay visualization.
- Website: [http://www.itksnap.org](http://www.itksnap.org).
- See the guide in this repository for instructions on how to use ITK-Snap for medical image manipulation.

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

## Instructions for Using the Script in a Python Environmen 

This script allows you to load and visualize 3D CT scans along with their corresponding annotations (e.g., segmentation masks). It is intended for medical imaging tasks using Python.

▶️ **How to Run the Script using the terminal**

```bash
python load_image_and_annotation.py -image data/images/patient_001.nii.gz --mask data/labels/patient_001.nrrd
```

---

## File Structure

```
📦 annotations_HCU.zip              # COVID-19 annotations
 ├── locca_covid_001_label.nrrd
 ├── locca_covid_002_label.nrrd
 ├── locca_covid_003_label.nrrd
     .
     .
     .
 └── locca_covid_030_label.nrrd

📦 annotations_Task06-Lung.zip       # Cancer annotations
 ├── lung_001_label.nrrd
 ├── lung_002_label.nrrd
 ├── lung_003_label.nrrd
     .
     .
     .
 └── lung_096_label.nrrd

📦 images_HCU.zip                    # Volumetric images of COVID-19
 ├── locca_covid_001.nii.gz
 ├── locca_covid_002.nii.gz
 ├── locca_covid_003.nii.gz
     .
     .
     .
 └── locca_covid_030.nii.gz

or

📦 images_HCU_part_1.zip                    # Volumetric images of COVID-19
 ├── locca_covid_001.nii.gz
 ├── locca_covid_002.nii.gz
 ├── locca_covid_003.nii.gz
     .
     .
     .
 └── locca_covid_006.nii.gz
 
📦 images_HCU_part_2.zip                    # Volumetric images of COVID-19
 ├── locca_covid_007.nii.gz
 ├── locca_covid_008.nii.gz
 ├── locca_covid_009.nii.gz
     .
     .
     .
 └── locca_covid_013.nii.gz
 
📦 images_HCU_part_3.zip                    # Volumetric images of COVID-19
 ├── locca_covid_014.nii.gz
 ├── locca_covid_015.nii.gz
 ├── locca_covid_016.nii.gz
     .
     .
     .
 └── locca_covid_018.nii.gz

📦 images_HCU_part_4.zip                    # Volumetric images of COVID-19
 ├── locca_covid_019.nii.gz
 ├── locca_covid_020.nii.gz
 ├── locca_covid_021.nii.gz
     .
     .
     .
 └── locca_covid_024.nii.gz

📦 images_HCU_part_5.zip                    # Volumetric images of COVID-19
 ├── locca_covid_025.nii.gz
 ├── locca_covid_026.nii.gz
 ├── locca_covid_027.nii.gz
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

# Comparative Analysis of Datasets with Manual Annotations of Pulmonary Lobes in CT Images

| Dataset                         | Cases with annotations           | Included Pathologies                 | Annotation Format | Image Format | Source |
|---------------------------------|:---------------------------:|:--------------------------------------:|:--------------------:|:-------------------:|:--------------------------------------------------------------------------------:|
| **LOCCA**                 | 60 | COVID-19 and cancer | NRRD | NIfTI | [LOCCA](https://github.com/MICLab-Unicamp/LOCCA) |
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

@ARTICLE{RibeiroLOCCA2025,
	author={Ribeiro, Jean A. and Carmo, Diedre S. Do and Reis, Fabiano and Magalhães, Ricardo S. and Dertkigil, Sergio S. J. and Appenzeller, Simone and Rittner, Leticia},
	journal={IEEE Data Descriptions}, 
	title={Descriptor: Manually Annotated CT Dataset of Lung Lobes in COVID-19 and Cancer Patients (LOCCA)}, 
	year={2025},
	volume={2},
	number={},
	pages={239-246},
	keywords={Lungs;Computed tomography;Annotations;Lung cancer;Biomedical imaging;Lesions;Image segmentation;Manuals;COVID-19;Three-dimensional displays;Cancer;computed tomography (CT) images;COVID-19;dataset;manual annotation for lung lobes},
	doi={10.1109/IEEEDATA.2025.3577999}
}
``` 

## 👉 Related works

``` 
@ARTICLE{CBEB2024,
	title = {Deep learning with probabilistic models for segmenting lung lobes on computed tomography images with severe abnormalities},
	author = {Jean Antonio Ribeiro and Diedre Santos do Carmo and Fabiano Reis and Leticia Rittner},
	journal = {CBEB 2024},
	pages = {1-6},
	year = {2024},
}

@ARTICLE{review2022,
	title = {{A Systematic Review of Automated Segmentation Methods and Public Datasets for the Lung and its Lobes and Findings on Computed Tomography Images}},
	author={Diedre Santos do Carmo and Jean Antonio Ribeiro and Sergio Dertkigil and Simone Appenzeller and Roberto Lotufo and Leticia Rittner},
	journal={Yearbook of Medical Informatics},
	volume={31},
	number={01},
	pages={277-295},
	year={2022},
	doi = {10.1055/s-0042-1742517}
}

``` 
