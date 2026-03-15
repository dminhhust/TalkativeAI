from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")


def clarity_score(transcript):

    sentences = transcript.split(".")

    if len(sentences) < 2:
        return 0.5

    embeddings = model.encode(sentences)

    sim = cosine_similarity([embeddings[0]], [embeddings[-1]])

    return float(sim[0][0])


def structure_score(transcript):

    words = len(transcript.split())

    if words < 20:
        return 0.4

    if words < 60:
        return 0.7

    return 0.9
