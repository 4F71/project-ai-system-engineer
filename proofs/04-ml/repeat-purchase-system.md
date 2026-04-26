# Proof: End-to-End Repeat Purchase Prediction System

## What was built
An end-to-end ML system to predict repeat purchase behavior on a 3.4M-row transactional dataset.

The system covers the full ML lifecycle: exploratory analysis, feature design, validation strategy, model training, and evaluation, with decisions aligned to business impact.

---

## Evidence

### External (original project)
- Full implementation & experiments:  
  https://github.com/4F71/instacart-next-product-recommendation

- Detailed pipeline & evaluation docs:  
  https://github.com/4F71/instacart-next-product-recommendation/tree/main/docs

### Internal (this repository)
- Async interview (EN):  
  projects/capstone-a-ml-system/inscart-end-to-end/Async_Interview_1.md

- Async interview (TR):  
  projects/capstone-a-ml-system/inscart-end-to-end/Async_Interview_1_TR.md

---

## Key verified aspects
- EDA-driven feature engineering on large-scale transactional data
- User-based validation using GroupKFold to prevent leakage
- LightGBM model selection with business-aligned metrics
- Explicit trade-off decisions (complexity vs. interpretability, recall vs. precision)

## Results (snapshot)

The following metrics are taken from a held-out validation set and represent a fixed snapshot
of model performance for the repeat purchase prediction task.

### Visual evidence

- Confusion matrix (validation set):
  - proofs/03-ml/assets/confusion-matrix.png
  ![Confusion Matrix](assets/confusion-matrix.png)



### Classification report

| Class | Precision | Recall | F1-score | Support |
|------|-----------|--------|----------|---------|
| 0 (non-repeat) | 0.74 | 0.40 | 0.52 | 111,258 |
| 1 (repeat)     | 0.69 | 0.91 | 0.78 | 165,929 |

Overall:
- Accuracy: 0.70
- ROC-AUC: 0.7779

### Validation setup
- Binary classification (repeat vs. non-repeat)
- User-based GroupKFold validation
- Prevents user-level data leakage across folds

---

## Reproducibility note

This proof references a fully implemented external repository for end-to-end experiments.
Within this roadmap repository, reproducibility is supported by:
- explicitly documented validation strategy (user-based GroupKFold),
- recorded metric snapshots and visual evidence,
- linked communication artifacts that explain design decisions and trade-offs.

---

## Notes
This proof intentionally links to:
- an external, fully implemented project (code + experiments)
- internal communication artifacts (async interview answers)

Together, they demonstrate both **technical execution** and **system-level reasoning**, rather than isolated modeling.
