# **PDF Merger**

🚀 **PDF Merger** は、複数の PDF ファイルを結合し、ページ番号を自動追加する GUI アプリケーションです。

---

## **📌 主な機能**
- ✅ **複数の PDF ファイルを結合**
- ✅ **ページ番号の自動追加**
- ✅ **ドラッグ & ドロップでファイルを追加**
- ✅ **進捗バー付きで処理状況を表示**

---

## **📥 インストール**
### **🔧 必要なライブラリ**
本アプリを使用するには、以下の Python ライブラリが必要です。

```bash
pip install tkinterdnd2 PyPDF2 reportlab
```

また、`tkinterdnd2` は OS によって追加のセットアップが必要になる場合があります。

---

## **🚀 使い方**
### **1️⃣ アプリを起動**
```bash
python PDFMerger.py
```

### **2️⃣ PDF ファイルを追加**
- **[Select PDFs]** ボタンをクリックし、結合したい PDF を選択
- または **ドラッグ & ドロップ** で PDF を追加

### **3️⃣ PDF を結合**
- **[Concat]** ボタンをクリックすると、選択した PDF が結合されます
- 結合後、**ページ番号が自動追加** されます

### **4️⃣ 保存**
- 保存先を選択し、結合後の PDF を保存

---
## **🏃‍♂️‍➡️　Pyinstallerによるexe化
win11環境でexe化可能なことは確認済み。ターミナル上で以下コマンドを実行。
```
pyinstaller src/PDFMerger.py --onefile -icon ./icon/icon.png
```

---

## **📂 ファイル構成**
```
PDFMerger/
├── PDFMerger.py   # メインスクリプト
├── README.md       # このファイル
```

---

## **⚠️ 注意点**
1. **結合する PDF の順番** はリスト内の並び順に依存します。
2. **ページ番号の追加** は、結合後の PDF 全体に適用されます。
3. **ファイル名に日本語** を含むと、環境によってはエラーが発生する可能性があります。

---

## **📜 ライセンス**
MIT License © 2025 Your Name / Your Organization

---

## **📩 お問い合わせ**
バグ報告や機能追加のリクエストは、GitHub の **Issues** に投稿してください！
🚀 Happy Merging! 🚀



