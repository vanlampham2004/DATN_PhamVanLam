import cv2
from skimage.metrics import structural_similarity as ssim

def compare_images(img1_path, img2_path):
    img1 = cv2.imread(img1_path, 0)
    img2 = cv2.imread(img2_path, 0)

    if img1 is None or img2 is None:
        print("Image not found")
        return 0

    # resize ảnh 2 về ảnh 1
    img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

    score, diff = ssim(img1, img2, full=True)

    print(f"SSIM Score: {score}")
    return score