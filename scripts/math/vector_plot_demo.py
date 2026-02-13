from __future__ import annotations
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt

def l2_norm(v:np.ndarray) -> float:
    v= np.asarray(v,dtype=float)
    return float(np.sqrt(np.sum(v*v)))

def main() -> None:

    vectors = [
        np.array([3.0, 4.0]),
        np.array([1.0,0.0]),
        np.array([-2.0 , 1.5]),
    ]
    
    norms = [l2_norm(v) for v in vectors]

    out_path = Path("proofs/02-math/assets/vectors-demo.png")
    out_path.parent.mkdir(parents=True , exist_ok=True)

    fig, ax = plt.subplots(figsize=(7,7))

    x = np.zeros(len(vectors))
    y = np.zeros(len(vectors))
    u = np.array([v[0] for v in vectors] , dtype=float)
    v = np.array([v[1] for v in vectors] , dtype=float)

    ax.quiver(x , y, u,v, angles = "xy", scale_units="xy", scale=1,width=0.008)
    max_extent = max(1.0,np.max(np.abs(np.concatenate([u,v])))) * 1.35
    ax.set_xlim(-max_extent,max_extent)
    ax.set_ylim(-max_extent,max_extent)
    ax.axhline(0,linewidth=1)
    ax.axvline(0,linewidth=1)
    ax.grid(True,alpha=0.3)
    ax.set_aspect("equal", adjustable="box")

    for i, (v, n) in enumerate(zip(vectors, norms), start=1):
        ax.text(
            v[0],
            v[1],
            f"v{i}=({v[0]:.1f}, {v[1]:.1f})\n||v{i}||2={n:.3f}",
            fontsize=9,
            ha="left",
            va="bottom",
        )

    ax.set_xlabel("x")
    ax.set_xlabel("y")
    ax.set_title("L2 Norm as Euclidean Length in R²")
    
    fig.tight_layout()
    fig.savefig(out_path, dpi=160)
    print(f"saved:{out_path.as_posix()}")
  
if __name__== "__main__":
    main()
              
                 