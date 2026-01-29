import math

class StructuralElement:
    """Base class for structural elements."""
    def __init__(self, name):
        self.name = name
        # Unit weight of concrete (kN/m3)
        self.CONCRETE_DENSITY = 25.0 

class Slab(StructuralElement):
    """Class to calculate loads for a reinforced concrete slab."""
    def __init__(self, name, thickness_mm, live_load_kn_m2, finish_load_kn_m2):
        super().__init__(name)
        self.thickness = thickness_mm / 1000.0  # Convert mm to m
        self.live_load = live_load_kn_m2
        self.finish_load = finish_load_kn_m2

    def calculate_dead_load(self):
        """Calculates self-weight of the slab (kN/m2)."""
        return self.thickness * self.CONCRETE_DENSITY

    def get_total_factored_load(self, dl_factor=1.2, ll_factor=1.6):
        """Returns total design load: Wu = 1.2(DL + SDL) + 1.6(LL)"""
        dead_load = self.calculate_dead_load() + self.finish_load
        return (dead_load * dl_factor) + (self.live_load * ll_factor)

class Beam(StructuralElement):
    """Class to calculate distributed loads and moments on a beam."""
    def __init__(self, name, width_mm, depth_mm, span_m):
        super().__init__(name)
        self.width = width_mm / 1000.0
        self.depth = depth_mm / 1000.0
        self.span = span_m

    def calculate_total_load(self, slab_unit_load, trib_width, dl_factor=1.2):
        """Calculates factored linear load on beam (kN/m)."""
        beam_sw = (self.width * self.depth * self.CONCRETE_DENSITY) * dl_factor
        slab_contrib = slab_unit_load * trib_width
        return beam_sw + slab_contrib

def get_float_input(prompt):
    """Helper function to ensure valid numeric input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Please enter a valid numerical value!")

def main():
    print("========================================")
    print("   STRUCTURAL LOAD CALCULATOR (RC)      ")
    print("========================================")
    
    # 1. Slab Data Input
    print("\n[1] ENTER SLAB PARAMETERS:")
    h_s = get_float_input("Slab thickness (mm): ")
    q_l = get_float_input("Live load (kN/m2): ")
    q_f = get_float_input("Superimposed Dead Load/Finishes (kN/m2): ")
    
    slab = Slab("UserSlab", h_s, q_l, q_f)
    w_u_slab = slab.get_total_factored_load()
    
    print(f"\n>> Calculated Slab Design Load (Wu): {w_u_slab:.2f} kN/m2")

    # 2. Beam Data Input
    print("\n" + "-"*40)
    print("[2] ENTER BEAM PARAMETERS:")
    b = get_float_input("Beam width (mm): ")
    h_b = get_float_input("Beam depth (mm): ")
    L = get_float_input("Beam span length (m): ")
    trib = get_float_input("Tributary width from slab (m): ")

    beam = Beam("UserBeam", b, h_b, L)
    w_u_beam = beam.calculate_total_load(w_u_slab, trib)
    
    # Simple Moment Calculation (wL^2 / 8)
    m_u = (w_u_beam * (L**2)) / 8

    # Final Output
    print("\n" + "="*40)
    print("          ANALYSIS RESULTS              ")
    print("="*40)
    print(f"Total Factored Load on Beam (Wu): {w_u_beam:.2f} kN/m")
    print(f"Maximum Design Moment (Mu):       {m_u:.2f} kNm")
    print("="*40)
    print("\nCalculation complete.")

if __name__ == "__main__":
    main()