**The following answers are based on an end-to-end ML system built to predict repeat purchase behavior in an e-commerce setting. This work was designed not only to focus on model performance, but also to demonstrate how an ML system can be approached end-to-end together with data flow, validation strategy, and business context.**  
**The complete project, including data pipelines and experimental details, is available in the repository below:**  
`https://github.com/4F71/instacart-next-product-recommendation`

## QUESTION

### SHORT:/

Describe an AI system you have recently built end-to-end.  
Focus on the problem definition, system architecture, technical decisions, and one trade-off you consciously accepted.

### LONG:/

Describe an AI system you have recently built end-to-end.

Please focus especially on:
- Problem definition: What did you solve and why was it important?
- System architecture: Core components and data flow (high level)
- Technical decisions:
  - Model selection
  - RAG / retrieval approach
  - Agent usage (if any)
  - Evaluation or validation strategy
- A trade-off or constraint: A limitation you consciously accepted and why

Assume the reader is a senior AI engineer.  
Keep the answer structured, clear, and defensible.

---

## ANSWER

### LONG:/

I developed an end-to-end machine learning system to predict **repeat purchase behavior** using a transactional dataset containing 3.4 million rows.

The primary goal of this project was to evaluate how effectively I could approach a large-scale, production-oriented ML problem within a domain I was already familiar with. From a business perspective, the system aimed to support inventory planning and personalization by identifying users with a high likelihood of repeat purchases.

I started the project with a detailed **exploratory data analysis (EDA)** phase. Insights derived from user purchasing patterns, product popularity, and temporal behavior directly shaped my feature engineering decisions and formed the backbone of the system.

Before moving into modeling, I established a baseline benchmark. Given the scale and tabular nature of the dataset, I chose **LightGBM** as the primary model. Training speed, memory efficiency, and robustness on large-scale tabular data were the key factors behind this decision.

The final model achieved an **F1 score of 0.78** and a **recall of 0.91**. I prioritized recall because missing users with true repeat purchase potential would be more costly than generating false positives. Model performance was evaluated using validation splits created with user-based GroupKFold, and results were interpreted not only through metrics but also in the context of business objectives.

The main trade-off I consciously accepted was not performing extensive threshold optimization. Since the default threshold already aligned well with recall-oriented business requirements, I assessed that the added complexity of further optimization would not provide meaningful additional value for the current objectives.

---

### SHORT:/

I built an end-to-end ML system to predict repeat purchase behavior on a dataset with 3.4 million rows. I applied EDA-driven feature engineering and selected LightGBM for its scalability. The model achieved 0.78 F1 and 0.91 recall, aligning well with recall-oriented business goals. I consciously limited threshold optimization due to diminishing returns.

---

### System Architecture (High Level)

- Data source → transactional purchase tables  
- Ingestion & memory handling → batch loading and optimization  
- Analysis → EDA-driven feature decisions  
- Feature generation → batch feature pipeline  
- Model training → LightGBM (with Optuna tuning)  
- Validation → GroupKFold with leakage checks  
- Output → repeat purchase probability scores  

> Detailed pipeline implementation and experimental results are documented here:  
> https://github.com/4F71/instacart-next-product-recommendation/blob/main/docs/final_report.md

---

## Clarification / Depth Questions

- What were the most impactful insights from your EDA, and how did they influence feature design?
- How did you define and label repeat purchase behavior?
- Did you encounter any data leakage risks, and how did you mitigate them?

>I derived behavior-based insights primarily from the `Orders` table. Observations such as peak ordering hours, preferred days of the week, and recurring monthly purchase patterns provided the strongest signals during EDA. Based on these findings, I focused on features that captured temporal behavior, as they contributed more effectively to model performance.

>Through product- and department-level analysis, I observed that users often repeated purchases within specific product groups. By examining the `Aisle` and `Department` tables, I found that users focused on staple grocery items were more likely to exhibit repeat purchase behavior. This led me to apply category-based feature engineering to enable more controlled and meaningful learning.

>While reviewing feature importance plots, I noticed that variables such as “user order count” were dominating model decisions. Further inspection revealed that this was caused by the target order being implicitly included in the training data. Recognizing this as a data leakage risk, I removed features that were directly correlated with the target or leaked future information.

---

## Modeling & Decision Questions

- Which models did you consider besides LightGBM, and why did you eliminate them?
- Was there class imbalance, and how did you handle it?
- In which business scenario would precision be more important than recall?

>I benchmarked Logistic Regression and XGBoost before selecting LightGBM. Given the dataset size of approximately 3.4 million rows, training speed and memory efficiency were critical. LightGBM provided a better balance between performance and computational cost, leading me to select it as the final model.

>The class distribution was approximately 60–40, indicating mild imbalance. Since this was not a severe imbalance scenario, I avoided aggressive sampling techniques. Instead, I relied on threshold and metric-based evaluation to preserve the model’s natural separation capability.

>In an e-commerce context, failing to identify a user who would actually repurchase results in direct revenue loss. Therefore, false negatives were more costly than false positives, and recall was prioritized. However, in scenarios involving high campaign costs or the risk of over-notifying users, precision would become more critical.

---

## Evaluation & Metrics Questions

- Which metrics did you track besides F1 and recall?
- How did you split your validation data?
- How did you assess the cost of false positives with a recall of 0.91?

>In addition to F1 and recall, I monitored precision and ROC-AUC. F1 helped assess overall balance, while ROC-AUC provided insight into the model’s ability to separate positive and negative classes. Evaluating these metrics together prevented over-reliance on a single performance indicator.

>I used user-based GroupKFold instead of a random split for validation. EDA showed that up to 60% of users exhibited loyalty and regular shopping cycles between 7 and 30 days. Splitting a user’s orders across training and test sets would cause the model to memorize user behavior. User-based separation allowed me to evaluate performance on completely unseen users more realistically.

>When achieving 0.91 recall, I evaluated the cost of false positives from a business perspective. Recommending an incorrect product was less costly than missing a genuine repeat purchase opportunity. By keeping precision at an acceptable level, I found that high recall provided a meaningful business-aligned balance.

---

## Trade-off & Production Questions

- What would you change first if you were to productionize this system?
- How would you detect data or concept drift over time?
- Which features would be risky for real-time inference, and why?

>If I were to productionize this system, my first priority would be clarifying the feature generation process. Some features computed in batch during training would not be reproducible in the same way at inference time. Before focusing on the model, I would identify which features are safe and sustainable in a production environment.

>To detect data or concept drift, I would focus on monitoring input feature distributions rather than model performance alone. Shifts in core behavioral features could provide early warning signals before performance degradation becomes visible. Simple statistical checks would be sufficient in the initial stages.

>In a real-time inference scenario, features relying on long historical aggregations or large time windows would be risky. Such features can introduce latency and data consistency issues. I would therefore favor features based on shorter time windows that are faster to compute and less sensitive to delay.

---

## System Thinking Questions

- How would the architecture change if this system moved from batch to near-real-time?
- How would downstream systems consume the model output?
- What do you consider the most fragile part of the system?

>If this system moved from batch to near-real-time, the most significant architectural change would occur in the feature generation layer. Features computed in batch during training would need to be decomposed into smaller, faster-to-compute components at inference time. The primary challenge would be redesigning data flow and ensuring feature consistency rather than modifying the model itself.

>I would expect downstream systems to consume model outputs as probability scores rather than binary decisions. These scores could feed into campaign triggering, ranking, or prioritization systems, allowing the model to function as a decision-support component instead of a single decision-maker.

>The most fragile part of the system is its reliance on user behavior–driven features. Changes in shopping habits or promotional dynamics could gradually erode model performance without immediate failure. For this reason, behavioral features would require continuous monitoring over time.

---

## Reflection Questions

- What would you do differently if you rebuilt this system today?
- How did this project change your approach to ML problems?
- Under what conditions might this system produce misleading outputs?

>If I were to rebuild this system today, I would simplify the feature set earlier in the process. Initially, I experimented with a broader set of features, but later observed that some of them provided limited contribution. Earlier simplification would have reduced development time and potential risks.

>This project shifted my approach to ML problems toward a more system-oriented perspective. It reinforced that model performance alone is insufficient, and that validation strategy, data leakage prevention, and business context are equally critical components.

>This system may produce misleading outputs when user behavior changes abruptly or when historical data no longer represents future patterns. High campaign activity, seasonal effects, or changes in data collection processes could invalidate learned relationships.
