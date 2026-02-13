from __future__ import annotations
import numpy as np

def l1_norm(v:np.ndarray) -> float:
    v=np.asarray(v,dtype=float)
    return float(np.sum(np.abs(v)))

def l2_norm(v:np.ndarray) -> float:
    v=np.asarray(v,dtype=float)
    return float(np.sqrt(np.sum(v*v)))

def is_unit_vector(v:np.ndarray,tol:float=1e-9) -> bool:
    return abs(l2_norm(v) -1.0) <=tol

def main() -> None:
    vectors = [
        np.array([3.0, 0.0]),
        np.array([1.0 / np.sqrt(2.0),1.0 / np.sqrt(2.0)]),
        np.array([1.0,-2.0,2.0]),
    ]

    tol = 1e-12
    print("norm demo(l1 vs l2)")

    for i,v in enumerate(vectors,start=1):
        l1 = l1_norm(v)
        l2 = l2_norm(v)

        assert(l1+tol) >= l2, f"L1 < L2 for v{i}: L1={l1}, L2={l2}"
        
        unit = is_unit_vector(v,tol=1e-9)

        print(f"v{i} = {v}")
        print(f" L1 ={l1:.12f}")
        print(f" L2 ={l2:.12f}")
        print(f"unit? = {unit}")
        print()

    print("done.")

if __name__ == "__main__":
    main()
        