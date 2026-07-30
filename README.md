🧬 Human Creator
> **Premium Parametric Full-Body Character Engine for Blender**

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Blender](https://img.shields.io/badge/Blender-4.2%2B-orange.svg)](https://www.blender.org/)
[![Framework](https://img.shields.io/badge/Base%20Framework-SOMA--X%20(Apache%202.0)-green.svg)](https://github.com/NVIDIA)

Human Creator is an open-source, high-density, community-driven Blender add-on designed to provide a modern, accessible alternative to legacy character rigging and mesh generation systems. This engine consolidates hyper-realistic full-body anatomy generation into a single canonical mesh topology powered by NVIDIA’s SOMA-X framework (Apache License 2.0).

To ensure maximum performance, absolute animation stability, and lightweight processing, the add-on completely removes facial expressions to focus exclusively on hyper-fidelity body features, automated skeletal proportions, an independent parametric clothing ecosystem, and production-ready rigging pipelines.

As a **Public Good**, Human Creator is built to be entirely free, transparent, and extendable by the global independent developer and creator community.

---

## 🌟 Core Feature Synthesis

Human Creator merges the best architectural components of leading character software into a single, unified open workflow:

* **Parametric Depth (inspired by MPFB 2):** Preserves the massive, ultra-granular slider matrix for micro-anatomical fine-tuning across every distinct muscle group, bone structure, and physical proportion.
* **Structural Stability (inspired by GNM):** Integrates localized volume preservation matrices. Shifting macro proportions (like weight or muscle mass) will not trigger mesh tearing, unnatural joint stretching, or volume loss.
* **Production Utility (inspired by Human Generator):** Adapts a seamless, artist-friendly generation pipeline including automated starter rigs, one-click asset initialization layers, and an integrated open asset management architecture.
* **Pipeline & Detailing Power (inspired by CC4):** Integrates advanced demographic/ancestry morph blending, non-destructive mesh editing pipelines, surface detailing arrays, and automated clothing collision mechanics.

---

## ⚙️ Technical Architecture

### 1. Native Mixamo Rigging & Retargeting Matrix
The base canonical mesh and internal rig are pre-built to natively match Mixamo’s structural skeletal bone naming conventions and hierarchy (e.g., `Hips`, `Spine`, `LeftUpLeg`).
* **Procedural Joint Snapping:** When a character's height, age, or BMI is modified via UI sliders, the open-source Procedural Linear Blend Skinning (LBS) engine instantly recalculates and snaps bone origins to the new physical dimensions.
* **One-Click Ingestion:** An automated rest-pose alignment tool handles local-to-global matrix transformations to inject external Mixamo animation keyframes directly onto custom characters without breaking skeletal proportions.

### 2. Advanced Ancestry & Demographic Population Blending
Using the structural capabilities of SOMA-X, the engine maps population-wide phenotypic variations. This allows users to blend and fine-tune regional anatomical profiles directly via slider vectors without changing base topology.
* **Regional/Ethnic Tuning Controls:** Granular sliders map localized physical traits associated with distinct global ancestries (e.g., Middle Eastern/Arab, East Asian, Ashkenazi/Jewish, Sub-Saharan African, South Asian, European).
* **Anatomical Integrity:** Dynamically adapts underlying skeletal structure, skull ratios, nasal bridges, orbital depths, and pelvic angles globally, preventing the unnatural "stretched mesh" look of standard vertex shifts.

### 3. The `.hclo` & `.hcmat` Parametric Asset Pipeline
The open `.hclo` (Human Clothing) system decouples clothing assets from rigid shapes:
* **Barycentric Vertex Mapping:** Open `.hclo` configuration files map garment vertex coordinates directly to matching target vertex IDs on the base canonical human mesh.
* **Dynamic Morph Scaling & Penetration Control:** Reads `.hclo` structural rules to deform, scale, and offset clothing vertices in real-time, completely eliminating clipping and mesh penetration.
* **The `.hcmat` Texture Ecosystem:** Standardized JSON texture map descriptor for `.hclo` garments. Automatically maps and links PBR material channels (Albedo, Roughness, Normal, Metallic, Ambient Occlusion) within Cycles and EEVEE Shader Nodes.

### 4. Procedural Melanin & Ancestry Skin Shader Engine
Human Creator includes an advanced node-based procedural skin shader system tailored for global phenotypic accuracy:
* **Base Phenotype Profiles:** Automatically drives subsurface scattering (SSS), melanin levels, carotene distribution, and dermal hemoglobin maps based on the selected demographic/ancestry vector mixtures.
* **Micro-Slider Fine Tuning:** Allows manual overriding and micro-adjustment of epidermal glossiness, pores/wrinkle bump scales, vascularity visibility, and localized flush/redness via standard Blender UI panels.

### 5. Pure Python & Lightweight Footprint
The entire framework operates transparently under a single, unified codebase. It avoids bloated deep learning runtime requirements, running purely on bundled NumPy and `h5py` matrix parsers. This keeps the total add-on installation package **well under 200MB**.

---

## 🎨 Front-End UI Layout

The UI panel offers a clean, minimalist presentation while preserving hyper-granular slider density:

1. **Character Spawning Layer:** Dedicated initialization routine (`Spawn SOMA Character`) drawing the base canonical mesh and building active update loops.
2. **Global Demographics Tab:** Semantic sliders for Target Age, Precise Height (cm), Body Mass Index (BMI), and Muscle Definition Profiles.
3. **Ancestry & Population Tab:** Multi-directional slider mixtures to dial in localized phenotype characteristics.
4. **Hyper-Granular Fine-Tuning Tabs:**
   * **[Head & Face]:** Eye socket depth, nose bridge width, jaw squareness, cheekbone prominence, skull height.
   * **[Torso & Chest]:** Shoulder-to-hip ratios, chest width, waist circumference, spine curvature.
   * **[Limbs & Extremities]:** Independent length, thickness, and muscle mass sliders for forearms, biceps, thighs, calves, hands, and feet.
5. **Procedural Shader Tab:** Granular skin controls for Melanin, Hemoglobin, Subsurface Radius, Roughness, and Surface Pore Scale.
6. **Anatomical Vector Tab:** Direct statistical vector parameters (PCA $\beta$ vectors) for technical artists.
7. **Animation & Assets Interface:** Dedicated panels for one-click Mixamo animation mapping and `.hclo`/`.hcmat` asset execution.

---

## 📜 Licensing & Funding

Human Creator is fully open-source and released under the **GNU General Public License v3 (GPL v3)** to align with the Blender ecosystem.

* **EVM Web3 Wallet (MetaMask / Grants Support on Polygon network):** `0xFE91250Df713De395Ed43a793794d27E8B3EDe90`

---
