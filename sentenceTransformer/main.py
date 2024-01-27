from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

sentences = ['Lets have a drink', 'Do you want to go for a drink?']

model = SentenceTransformer('thenlper/gte-small')
embeddings = model.encode(sentences)
print(cos_sim(embeddings[0], embeddings[1]))
