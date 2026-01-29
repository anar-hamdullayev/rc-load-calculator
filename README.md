# Structural Load Calculator (RC Elements)

A Python-based engineering tool designed to automate the process of load analysis for Reinforced Concrete (RC) slabs and beams. This script calculates self-weights, applies safety factors (ACI 318), and determines the design moments for structural elements.

## Features

* **Slab Analysis:** Calculates self-weight based on thickness and adds superimposed dead loads (SDL) and live loads (LL).
* **Load Factoring:** Automatically applies standard safety factors: .
* **Beam Analysis:** Calculates the beam's own self-weight and integrates the distributed load coming from the slab.
* **Moment Calculation:** Computes the maximum design bending moment () for simply supported beams.
* **Interactive CLI:** Users can input real-time data for different project scenarios.

## Mathematical Formulas Used

The script follows the Limit State Design philosophy:

1. **Factored Unit Load ($w_u$):**

$$w_u = 1.2 \cdot (SelfWeight + SDL) + 1.6 \cdot LL$$

2. **Total Linear Load on Beam ($W_{total}$):**

$$W_{total} = (w_u \cdot TributaryWidth) + (BeamSelfWeight \cdot 1.2)$$

3. **Maximum Bending Moment ($M_u$):**

$$M_u = \frac{W_{total} \cdot L^2}{8}$$


## How to Run

1. Ensure you have Python installed.
2. Clone this repository:
git clone https://github.com/anar-hamdullayev/rc-load-calculator/blob/main/structural_calc.py


3. Navigate to the folder and run the script:
python structural_calc.py



## Example Test Case

<img width="384" height="541" alt="image" src="https://github.com/user-attachments/assets/5196697d-7c2d-4394-bd33-bdb9c9c916ac" />

---
To verify the script, you can use these typical residential values:

* **Slab Thickness:** 150 mm
* **Live Load:** 2.0 
* **Finishes (SDL):** 1.5 
* **Beam Dimensions:** 300mm x 600mm
* **Beam Span:** 6.0 m
* **Tributary Width:** 4.0 m


---
