# `.hclo` (Human Clothing) Specification v1.0

The `.hclo` format is an open JSON/YAML specification designed to decouple 3D garments from fixed mesh topology. It enables dynamic vertex deformation and penetration prevention on top of the SOMA-X canonical base mesh.

---

## 1. Structural Overview

An `.hclo` asset package consists of two primary elements
1. **Geometry Mesh (`.obj` or asset)**: The base 3D garment topology fitted to the SOMA-X canonical rest pose.
2. **Configuration File (`.hclo`)**: The structural mapping metadata linking garment vertices to base human body vertex indices.

---

## 2. Configuration File Schema (`.hclo`)

```json
{
  "hclo_version": "1.0.0",
  "asset_name": "Standard T-Shirt",
  "canonical_mesh_version": "SOMA-X-v1",
  "barycentric_bindings": [
    {
      "garment_vert_id": 0,
      "target_face_id": 1420,
      "barycentric_weights": [0.45, 0.35, 0.20],
      "normal_offset": 0.003
    }
  ],
  "collision_rules": {
    "mask_body_vertices": true,
    "penetration_threshold": 0.001,
    "inflation_vector": [0.0, 0.002, 0.0]
  },
  "material_reference": "textures/tshirt_default.hcmat"
}
