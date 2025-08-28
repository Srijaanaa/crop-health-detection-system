import os, shutil, random
from tqdm import tqdm

def split_data(SOURCE, TRAIN, VAL, split_size=0.8):
    for category in os.listdir(SOURCE):
        cat_path = os.path.join(SOURCE, category)
        if not os.path.isdir(cat_path): continue

        # Filter only valid image files
        imgs = [f for f in os.listdir(cat_path)
                if os.path.isfile(os.path.join(cat_path, f)) and f.lower().endswith(('.jpg', '.jpeg', '.png'))]

        if len(imgs) == 0:
            print(f"Skipping {category} (no valid images found)")
            continue

        random.shuffle(imgs)
        split_idx = int(len(imgs) * split_size)

        train_cat = os.path.join(TRAIN, category)
        val_cat = os.path.join(VAL, category)
        os.makedirs(train_cat, exist_ok=True)
        os.makedirs(val_cat, exist_ok=True)

        for img in tqdm(imgs[:split_idx], desc=f"Train: {category}"):
            shutil.copy(os.path.join(cat_path, img), os.path.join(train_cat, img))
        for img in tqdm(imgs[split_idx:], desc=f"Val: {category}"):
            shutil.copy(os.path.join(cat_path, img), os.path.join(val_cat, img))

# Paths
SOURCE = 'PlantVillage'
TRAIN = 'dataset/train'
VAL = 'dataset/val'
split_data(SOURCE, TRAIN, VAL)
