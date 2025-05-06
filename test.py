import os
import random
from PIL import Image
from torch.utils.data import Dataset
from torchvision import transforms

class CycleGANDataset(Dataset):
    def __init__(self, root, transform=None):
        self.root = root
        self.transform = transform
        self.A_images = sorted(os.listdir(os.path.join(root, 'trainA')))
        self.B_images = sorted(os.listdir(os.path.join(root, 'trainB')))

    def __len__(self):
        return len(self.A_images)

    def __getitem__(self, idx):
        A_img = Image.open(os.path.join(self.root, 'trainA', self.A_images[idx]))
        B_img = Image.open(os.path.join(self.root, 'trainB', self.B_images[idx]))

        if self.transform:
            A_img = self.transform(A_img)
            B_img = self.transform(B_img)

        return A_img, B_img
