# Vision-Based Underwater Docking Station Detection and Pose Estimation for AUVs

![AUV Docking](https://img.shields.io/badge/Status-Completed-brightgreen)

A project focused on **automated underwater docking** using **deep learning** and **computer vision** techniques for Autonomous Underwater Vehicles (AUVs).

https://www.researchgate.net/publication/392590921_Vision-Based_Underwater_Docking_Station_Detection_and_Pose_Estimation_for_Autonomous_Underwater_Vehicles_AUVs

---

## 🔍 Overview

This project presents a robust vision-based system for the **detection of underwater docking stations** and **pose estimation** to facilitate accurate and safe docking of AUVs. Given the challenges of underwater environments—such as turbid water, low visibility, and light scattering—traditional docking methods prove inefficient and costly. Our work leverages modern **deep learning models (YOLOv8, RT-DETR)** and **pose estimation algorithms** to address these challenges effectively.

---

## 🎯 Objectives

- Detect underwater docking stations in low-visibility and turbid water conditions.
- Compare performance between **YOLOv8** and **Real-Time Detection Transformer (RT-DETR)** models.
- Estimate the pose of detected docking stations using calibrated vision systems.
- Enable autonomous navigation and docking for AUVs with minimal human intervention.

---

## 🧠 Core Technologies

- **Deep Learning Models**:
  - [YOLOv8](https://github.com/ultralytics/ultralytics)
  - [RT-DETR (Real-Time Detection Transformer)](https://github.com/IDEA-Research/RT-DETR)
- **Pose Estimation**:
  - OpenCV-based camera calibration and 3D pose extraction
  - Hough Circle Transform (HTC) and contour fitting for localization
- **Data Annotation**: Roboflow
- **Image Augmentation**: Flipping, rotation, noise injection, etc.

---

## 🛠️ Methodology

### Phase 1: Docking Station Detection

- **Data Collection**: 450 images of docking stations under varied underwater conditions.
- **Annotation & Preprocessing**: Roboflow used for bounding box labeling and augmentation.
- **Model Training**:
  - YOLOv8 and RT-DETR trained for 50 epochs.
  - Evaluated using metrics like mAP50, mAP50-95, and loss.

### Phase 2: Pose Estimation

- **Camera Calibration**: Using checkerboard pattern with OpenCV.
- **Pose Estimation**: Estimating 3D coordinates of the docking station via circle fitting and contour analysis.
- **Docking Logic**: Deriving spatial alignment and movement instructions for the AUV based on real-time image processing.

---

## 📊 Results

| Metric            | YOLOv8     | RT-DETR   |
|-------------------|------------|------------|
| Class Loss        | 0.43634    | **0.33573** |
| Precision         | **0.97916**| 0.913      |
| Recall            | 0.95901    | **1.000**   |
| mAP@0.5           | 0.97884    | **0.97886** |
| mAP@0.5:0.95      | **0.68281**| 0.65315    |

- **RT-DETR** demonstrated better classification accuracy and robustness under challenging conditions.

---

## 🧪 Key Features

- ✅ Detection in turbid, low-light water environments
- ✅ High-precision pose estimation with minimal data
- ✅ Support for real-time AUV navigation systems
- ✅ Fully annotated and augmented dataset (450+ images)

---

## 🧭 Applications

- Autonomous marine exploration
- Underwater pipeline and infrastructure maintenance
- Oceanographic research
- Robotic swarm docking systems

---


---

## 👨‍🔬 Contributors

- **Bishal Hazarika** – `200101034`  
- **Dhruba Jyoti Sarma** – `200101003`  
- Department of Electronics and Communication Engineering  
  Gauhati University, Assam, India

---

## 📌 Future Scope

- Integrate real-time feedback loop for closed-loop docking.
- Deploy model on embedded hardware (e.g., Jetson Nano).
- Extend system to multi-agent AUV coordination.
- Expand dataset with synthetic underwater imagery using simulation.

---

## 📄 License

This project was developed as part of the **B.Tech final year dissertation** and is intended for academic and research use. Licensing terms may vary based on deployment context.


