import csv
import io
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
embeddings1 = None
names1 = None

def get_best_match(name):
    global embeddings1
    global names1
    max_similarity = -np.inf
    best_match_index = None
    name_embedding = model.encode(name, convert_to_tensor=True)
    
    for index, emb in enumerate(embeddings1):
        sim = util.pytorch_cos_sim(name_embedding, emb)
        if sim > max_similarity:
            max_similarity = sim
            best_match_index = index
            
    return names1[best_match_index], max_similarity.item()

def process_uploaded_files(file1, file2):
    global embeddings1
    global names1
    
    file1_text = io.TextIOWrapper(file1, encoding='utf-8')
    file2_text = io.TextIOWrapper(file2, encoding='utf-8')
    
    with file1_text as f1:
        reader = csv.reader(f1, delimiter=',')
        file1_data = [(row[0], row[1]) for row in reader]
        names1 = [item[1] for item in file1_data]
        embeddings1 = model.encode(names1, convert_to_tensor=True)
    
    with file2_text as f2:
        reader = csv.reader(f2, delimiter=',')
        file2_data = [row[0] for row in reader]
    
    return file1_data, file2_data

def match_names(file1_data, file2_data):
    global embeddings1
    global names1
    
    matched_data = []
    for name in file2_data:
        best_match_name, similarity_score = get_best_match(name)
        matched_code = next((code for code, nm in file1_data if nm == best_match_name), None)
        matched_data.append([name, matched_code, best_match_name, similarity_score])
    
    return matched_data

def prepare_download(data):
    df = pd.DataFrame(data, columns=['Name from File2', 'Matched Code', 'Matched Name from File1', 'Similarity Score'])
    csv_data = df.to_csv(index=False)
    return csv_data
