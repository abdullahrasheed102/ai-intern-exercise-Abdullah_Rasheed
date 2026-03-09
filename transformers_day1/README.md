## 1. What is Generative AI?

Generative AI is a type of artificial intelligence that can create new content such as text, images, audio, video, or code. Instead of only analyzing existing data like traditional machine learning models, generative models learn patterns in data and then generate new outputs that are similar to the training data.

Traditional machine learning models usually perform tasks such as classification or prediction. For example, a model might classify emails as spam or not spam, or predict house prices based on past data. These models map inputs to outputs but do not create entirely new data.

Generative AI models, especially Large Language Models (LLMs), learn the probability distribution of data and generate new samples from it. For example, a language model learns patterns in text and predicts the next word in a sequence. By repeatedly predicting words, it can generate full paragraphs or articles.

Some common generative model architectures include Transformers, GANs (Generative Adversarial Networks), and Variational Autoencoders.

### Real-World Applications

1. **Text Generation**  
   Tools like chatbots and writing assistants generate articles, emails, and conversations.

2. **Image Generation**  
   Models can create realistic images from text descriptions, useful in design, marketing, and entertainment.

3. **Code Generation**  
   AI tools help developers generate code, debug programs, and automate repetitive programming tasks.

## 2. Self-Attention Explained

Consider the sentence:

"The cat sat on the mat"

Self-attention allows each word in the sentence to look at other words and determine how important they are for understanding the meaning.

### Query (Q), Key (K), and Value (V)

Each word is converted into three vectors:

- **Query (Q)** – represents what the word is searching for.
- **Key (K)** – represents what the word contains.
- **Value (V)** – represents the information the word provides.

To calculate attention, we compare the Query of one word with the Keys of all other words. This gives attention scores that indicate how much each word should focus on the others.

### Why do we scale by √d_k?

The dot product between Query and Key can become very large when the dimension of the vectors is high. Large values can cause the softmax function to produce extremely small gradients.

To prevent this, we divide by √d_k (square root of the key dimension). This keeps the values stable and improves training.

### Why apply Softmax?

Softmax converts attention scores into probabilities between 0 and 1. This allows the model to assign weights to different words, showing how important each word is.

### What problem does attention solve that RNNs struggled with?

RNNs process words sequentially, which makes it difficult to capture long-range dependencies in long sentences.

Self-attention solves this problem because every word can directly attend to every other word in the sentence. This allows the model to understand relationships between distant words much more effectively.

## 3. Encoder vs Decoder Comparison

| Component | Encoder | Decoder |
|----------|---------|---------|
| Purpose | Understands the input sequence | Generates the output sequence |
| Self-Attention | Yes | Yes |
| Masked Attention | No | Yes |
| Cross-Attention | No | Yes |

### Masked Attention
Masked attention prevents the decoder from looking at future tokens during training. This ensures the model predicts the next word using only previous words.

### Cross-Attention
Cross-attention allows the decoder to focus on the encoder's output representations. This helps the model use information from the input sequence while generating the output.

### When Each is Used
The encoder is used to process and understand the input data. The decoder is used when generating sequences such as translation, text generation, or summarization.

## 4. Vision Transformers (ViT)

Vision Transformers apply the transformer architecture to images instead of text.

### Image Patches

Instead of processing the entire image at once, the image is divided into small fixed-size patches, for example 16×16 pixels. Each patch acts like a “word” in a sentence.

### Patches to Tokens

Each patch is flattened into a vector and then passed through a linear layer to convert it into an embedding vector. These embeddings become tokens that the transformer can process.

### Positional Embeddings

Transformers do not naturally understand order or position. In images, spatial location is important. Positional embeddings are added to each patch embedding to provide information about where the patch appears in the image.

### Difference from CNNs

CNNs use convolution filters to detect local patterns such as edges and textures. They process images using sliding windows and hierarchical feature extraction.

Vision Transformers treat the image as a sequence of patches and use attention mechanisms to capture global relationships between different parts of the image. This allows the model to learn long-range dependencies across the entire image.