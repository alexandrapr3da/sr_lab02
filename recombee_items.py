import pandas as pd
from recombee_api_client.api_client import RecombeeClient, Region
from recombee_api_client.api_requests import SetItemValues, Batch

# TODO 1: Configurare credentiale
DB_NAME = 'alexandrapr3da-prod'
PRIVATE_TOKEN = 'CGHpFcc5emDfdJtWZTCcA5LIIeYthMtzTgK1SnqXoBjGv8OM7CMS4GeCcRpikT3H'
REGION = Region.EU_WEST

client = RecombeeClient(DB_NAME, PRIVATE_TOKEN, region=REGION)
PATH_DATASET = 'books.csv'

def send_items():
    df = pd.read_csv(PATH_DATASET)
    
    # Rezolvarea warning-ului galben: curatam coloanele numerice separat de cele de tip text
    df['published_year'] = df['published_year'].fillna(0).astype(int)
    df['num_pages'] = df['num_pages'].fillna(0).astype(int)
    df['average_rating'] = df['average_rating'].fillna(0.0).astype(float)
    
    text_cols = ['title', 'authors', 'categories', 'description', 'thumbnail']
    df[text_cols] = df[text_cols].fillna('')

    print(f"Se trimit {len(df)} item-uri in Recombee...")
    requests = []
    
    # Procesare rapida si mapare corecta (fara erori de dictionar)
    for row in df.to_dict('records'):
        item_id = str(row['isbn13'])
        
        properties = {
            "title": str(row['title']),
            "authors": str(row['authors']),
            "categories": str(row['categories']),
            "published_year": int(row['published_year']),
            "average_rating": float(row['average_rating']),
            "num_pages": int(row['num_pages']),
            "description": str(row['description']),
        }
        
        requests.append(SetItemValues(item_id, properties, cascade_create=True))
        
        # Trimitere in pachete de 100
        if len(requests) == 100:
            client.send(Batch(requests))
            requests = []
            
    # Trimitere rest ramas
    if requests:
        client.send(Batch(requests))
        
    print("Toate item-urile au fost trimise cu succes!")

if __name__ == "__main__":
    send_items()