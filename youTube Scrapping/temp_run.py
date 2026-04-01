import logging, re
from youtube_transcript_api import YouTubeTranscriptApi
from sentence_transformers import SentenceTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import nltk
from nltk.tokenize import sent_tokenize

logging.getLogger('transformers').setLevel(logging.ERROR)
logging.getLogger('sentence_transformers').setLevel(logging.ERROR)

nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)

def get_video_id(url):
    if 'youtu.be/' in url:
        return url.split('youtu.be/')[-1].split('?')[0]
    if 'v=' in url:
        return url.split('v=')[-1].split('&')[0]
    if '/watch/' in url:
        return url.split('/watch/')[-1].split('?')[0]
    return url.strip()


def get_transcript(video_id):
    api = YouTubeTranscriptApi()
    pref = ['en', 'en-US', 'en-GB', 'en-IN']
    try:
        transcript_data = api.fetch(video_id, languages=pref)
    except Exception as err1:
        try:
            transcripts = api.list(video_id)
            try:
                transcript = transcripts.find_transcript(pref)
            except Exception:
                transcript = transcripts.find_generated_transcript(pref)
            if transcript.language_code not in pref:
                transcript = transcript.translate('en')
            transcript_data = transcript.fetch()
        except Exception as err2:
            raise RuntimeError(f'Could not fetch transcript for {video_id}: {err1} | {err2}')

    if isinstance(transcript_data, dict) and 'snippets' in transcript_data:
        return ' '.join([item['text'] for item in transcript_data['snippets']])
    return ' '.join([item.get('text', '') if isinstance(item, dict) else str(item) for item in transcript_data])


def summarize_text(text, max_sentences=8):
    if not text or not text.strip():
        return ''
    content = re.sub(r'\s+', ' ', text.replace('\n', ' ')).strip()
    sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+', content) if s.strip()]
    if len(sentences) <= max_sentences:
        return ' '.join(sentences)
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(sentences, convert_to_tensor=True).cpu().numpy()
    centroid = np.mean(embeddings, axis=0).reshape(1, -1)
    sims = cosine_similarity(centroid, embeddings)[0]
    top_idx = sorted(np.argsort(sims)[::-1][:max_sentences])
    return ' '.join(sentences[i] for i in top_idx)


def extract_key_points(text, num_points=5):
    sentences = [s.strip() for s in text.replace('\n', ' ').split('.') if s.strip()]
    if not sentences:
        return []
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(sentences)
    base = np.mean(embeddings, axis=0).reshape(1, -1)
    scores = cosine_similarity(embeddings, base)[:,0]
    ranked = sorted(zip(scores, sentences), reverse=True)
    return [s for _, s in ranked[:num_points]]


def extract_topics(text, n_topics=5):
    if not text or not text.strip():
        return []
    vec = TfidfVectorizer(stop_words='english', ngram_range=(1,2), max_features=1000)
    X = vec.fit_transform([text])
    words = vec.get_feature_names_out()
    scores = X.toarray()[0]
    idx = np.argsort(scores)[::-1][:n_topics]
    return [words[i] for i in idx]


def generate_smart_notes(transcript, summary, topics):
    sentences = sent_tokenize(transcript)
    notes = '📘 SMART NOTES\n' + '='*40 + '\n\n'
    notes += '🎯 Topic:\n' + ', '.join(topics[:3]) + '\n\n'
    notes += '🧠 Summary:\n' + summary.strip() + '\n\n'
    notes += '📌 Key Concepts:\n'
    for i, s in enumerate(sorted(sentences, key=len, reverse=True)[:5], 1):
        notes += f'{i}. {s.strip()}\n'
    notes += '\n⚡ Quick Revision:\n'
    for t in topics:
        notes += f'- {t}\n'
    return notes

link = 'https://youtu.be/CrEhGIBCAPU?si=XOKRH_qpxry0-K7-'
vid = get_video_id(link)
print('video id', vid)
transcript = get_transcript(vid)
print('Transcript length', len(transcript))
summary = summarize_text(transcript)
key_points = extract_key_points(transcript)
topics = extract_topics(transcript)
notes = generate_smart_notes(transcript, summary, topics)
print(notes)
