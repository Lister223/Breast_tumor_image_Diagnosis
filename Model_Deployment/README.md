# 🩺🔬 Breast Cancer Pathology Image Classification API (Flask + ResNet50V2)

## 📖 專案介紹
本專案使用 **ResNet50V2** 深度學習模型來進行 **乳房病理腫瘤影像分類**，並透過 **Flask API 部署**，允許用戶上傳影像並獲取預測結果。  

### 📊 **功能**
- 🔍 **影像分類（Benign / Malignant）**：透過 **ResNet50V2** 模型進行乳房病理影像診斷。
- 📡 **Web API 部署**：基於 **Flask**，允許用戶透過網頁上傳影像並獲取診斷結果。
- 🖼️ **圖片預處理**：
  - 影像 **標準化（per_image_standardization）**
  - **對比度增強（adjust_contrast）**
  - **像素正規化（/255.0）**

---

## 🚀 **使用技術**
- **深度學習**：
  - ResNet50V2（遷移學習）
  - TensorFlow 2.x
  - NumPy
- **後端 API**：
  - Flask（提供 HTTP API）
  - Flask-CORS（解決跨域問題）
- **影像處理**：
  - Pillow（影像格式處理）
  - Base64（影像傳輸編碼）

---

## 📦 **環境與依賴**
請確保你的環境具備以下軟體：
- Python 3.8.20
- TensorFlow 2.10
- Numpy 1.22.0
- Flask & Flask-CORS
- Pillow（影像處理）

📌 **安裝依賴**
```bash
pip install -r requirements.txt
