# 🩺🔬 Breast Cancer Pathology Image Classification (ResNet50V2)

## 📖 專案介紹
本專案針對 **乳房病理腫瘤影像** 進行 **癌症性質預測**，使用 **深度學習模型** 進行分類，並最終達到 **98% 準確率**。

### 📊 目標
- **分類乳房病理腫瘤影像**，區分 **良性** 與 **惡性腫瘤**。
- **預測病理特徵**，幫助醫學影像分析與輔助診斷。
- **數據集來源**
https://www.kaggle.com/datasets/anaselmasry/breast-cancer-dataset/data
---

## 🚀 **使用技術**
### **🔹 圖像增強與預處理**
- **`ImageDataGenerator`**：進行 **隨機翻轉、裁剪、標準化與對比度調整**，提升模型泛化能力。

### **🔍 深度學習模型**
- **ResNet50V2 (遷移學習)**
  - 使用 **預訓練的 ResNet50V2** 作為特徵提取基礎，遷移學習提升效果。
  - 微調模型最後幾層以適應乳房病理影像分類。

### **🎯 優化策略**
- **SGD (Stochastic Gradient Descent) 優化器**
- **學習率調度器 (`ReduceLROnPlateau`)**
- **早停策略 (`EarlyStopping`)**

### **📈 模型評估**
- 使用 **混淆矩陣（Confusion Matrix）** 進行 **準確率、召回率、F1-score 分析**。
- 最終模型達到 **0.98 準確率**。

---

## 📦 **環境與依賴**
請確保你的環境具備以下軟體：
- Python 3.11
- Jupyter Notebook / Google Colab
- 主要使用的 Python 套件：
  ```bash
  pip install -r requirements.txt
