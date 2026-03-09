import numpy as np
from typing import Tuple


def softmax(matrix: np.ndarray) -> np.ndarray:
    exp_values = np.exp(matrix - np.max(matrix, axis=-1, keepdims=True))
    return exp_values / np.sum(exp_values, axis=-1, keepdims=True)


def scaled_dot_product_attention(
    Q: np.ndarray,
    K: np.ndarray,
    V: np.ndarray
) -> np.ndarray:

    dk = K.shape[-1]

    attention_scores = np.matmul(Q, K.T)

    scaled_scores = attention_scores / np.sqrt(dk)

    attention_weights = softmax(scaled_scores)

    output = np.matmul(attention_weights, V)

    return output


if __name__ == "__main__":

    np.random.seed(42)

    Q = np.random.rand(3, 4)
    K = np.random.rand(3, 4)
    V = np.random.rand(3, 4)

    attention_output = scaled_dot_product_attention(Q, K, V)

    print("Attention Output:")
    print(attention_output)