Deepfake Detection with MesoNet

This project uses the MesoNet model to detect deepfake images.
It includes the pretrained model weights (Meso4_DF.h5), the model architecture (classifiers.py), and preprocessing scripts.
A FastAPI backend will be integrated to provide an API for detecting REAL vs FAKE images.


---

⚡ How It Works

The model takes an input image

It processes and predicts whether the image is REAL or DEEPFAKE

It outputs a prediction score (1.0 = Real, 0.0 = Fake)



---

📂 Project Structure

Deepfake-Detection-MesoNet/
│── classifiers.py         # Defines the MesoNet model architecture
│── preprocess.py          # Image preprocessing before prediction
│── weights/
│   └── Meso4_DF.h5        # Pretrained model weights
│── backend/               # (Will contain FastAPI backend)
│── README.md              # Project documentation


---

🚀 Setup Instructions

⿡ Clone the Repository

git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>

⿢ Create a Virtual Environment & Install Dependencies

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

(The backend developer will add requirements.txt after setup)


---


🔮 Future Plans

Extend detection to video frames

Integrate with a browser extension

Deploy the backend to cloud hosting

Extend it to mobile app



---

🤝 Contributors

Devika V - Set up the MesoNet model and repo
Anagha Anurag - Frontend
Nimah Zayn - Backend & API integration with FastAPI
Meera Lakshman Rao - Documentation





---

📜 License

This project is open-source and available under the MIT License.



---
