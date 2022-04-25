A **Focal Loss** function addresses ==class imbalance== during training in tasks like ==object detection==. Focal loss applies a modulating term to the cross-entropy loss in order to focus learning on hard misclassified examples. It is a dynamically scaled cross-entropy loss, where the scaling factor decays to zero as confidence in the correct class increases. Intuitively, this scaling factor can automatically down-weight the contribution of easy examples during training and rapidly focus the model on hard examples.

Formally, the Focal Loss adds a factor $(1−p_t)^\gamma$ to the standard cross entropy criterion. Setting $\gamma > 0$ reduces the relative loss for well-classified examples ($p_t>.5$), putting more focus on hard, misclassified examples. Here there is tunable _focusing_ parameter $γ≥0$.

$$
\text{FL}(p_t) = - (1 - p_t)^\gamma \log(p_t)
$$