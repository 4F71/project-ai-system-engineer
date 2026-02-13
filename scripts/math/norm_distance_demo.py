from __future__ import annotations

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

def main() -> None:

    x, y= 3.0, 2.0
    p = np.array([x,y], dtype=float)

    l1=abs(x) + abs(y)
    l2= float(np.linalg.norm(p))

    out_path = Path("proofs/02-math/assets/l1-vs-l2-path.png")
    out_path.parent.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(7, 7))

    ax.plot([0,x],[0,y], linewidth=2, label=f"L2 direct (len={l2:.3f})" )

    ax.plot([0, x], [0, 0], linewidth=2, label=f"L1 path part 1 (len={abs(x):.0f})")
    ax.plot([x, x], [0, y], linewidth=2, label=f"L1 path part 2 (len={abs(y):.0f})")                     
    
    ax.scatter([0,x], [0,y])
    ax.text(
        x,
        y,
        f"  P=({x:.0f},{y:.0f})\n  L1={l1:.0f}\n  L2={l2:.3f}",
        va="bottom",
    )

    ax.axhline(0,linewidth=1)
    ax.axvline(0,linewidth=1)
    ax.grid(True,alpha=0.3)
    ax.set_aspect("equal", adjustable="box")

    ax.set_xlim(-1, max(4, x + 1))
    ax.set_ylim(-1, max(4, y + 1))

    ax.set_xlabel("x")
    ax.set_xlabel("y")
    ax.set_title("L1 vs L2 distance intuition (grid path vs straight line)")
    ax.legend(loc="upper left", fontsize=9)

    fig.tight_layout()
    fig.savefig(out_path, dpi=160)
    print(f"saved:{out_path.as_posix()}")

if __name__ == "__main__":
    main()
          