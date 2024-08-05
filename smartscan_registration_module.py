import pyqrcode
import cv2

# In-Memory Storage for users
user_storage = []

# SmartScan Code Generation
def create_qr_code(user_name, user_email, user_gender, file_name):
    qr_data = f"{user_name},{user_email},{user_gender}"
    qr_code = pyqrcode.create(qr_data)
    qr_code.png(file_name, scale=8)
    print(f"QR code saved as {file_name}")

# Decode QR Code
def read_qr_code(file_path):
    image = cv2.imread(file_path)
    qr_detector = cv2.QRCodeDetector()
    qr_data, _, _ = qr_detector.detectAndDecode(image)
    return qr_data if qr_data else None

# Parse QR Code Data
def parse_qr_data(qr_data):
    name, email, gender = qr_data.split(',')
    return {"name": name, "email": email, "gender": gender}

# Register User from QR Code
def register_user_from_qr(file_path, create_fn, insert_fn, fetch_fn):
    qr_content = read_qr_code(file_path)
    if not qr_content:
        print("No data found in the QR code.")
        return

    user_info = parse_qr_data(qr_content)
    new_user = create_fn(user_info['name'], user_info['email'], user_info['gender'])
    insert_fn(new_user)