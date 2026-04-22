# 🎙️ AI Meeting Summarizer & Action Item Extractor

Một ứng dụng web đơn giản được xây dựng bằng **Streamlit** và **Google Gemini AI** giúp tự động hóa việc tóm tắt biên bản cuộc họp. Người dùng chỉ cần tải lên một file ghi âm cuộc họp, AI sẽ tự động nhận diện giọng nói, chuyển đổi thành văn bản (Speech-to-Text), sau đó tóm tắt nội dung chính, trích xuất các quyết định và tạo một danh sách công việc (Action Items).

## 🌟 Tính năng
- **Hỗ trợ Audio Menu**: Tải lên các file âm thanh với định dạng phổ biến như `.mp3`, `.wav`, `.m4a`.
- **Nhận diện giọng nói (Speech-to-Text)**: Nghe và chuyển đổi âm thanh sang phụ đề văn bản nhanh chóng bằng API của mô hình `gemini-2.5-flash`.
- **Phân tích siêu tốc**: Tóm tắt nội dung cốt lõi của cuộc họp một cách súc tích.
- **Trích xuất công việc**: Tự động liệt kê các Quyết định và phân công Action Items vào một bảng thông minh.
- **Tự động thử lại (Retry & Rate Limit Bypass)**: Tích hợp sẵn cơ chế ngủ đông giúp ứng dụng hoàn thành tác vụ ngay cả khi dùng API key hệ miễn phí (Free Tier) có số lần Request thấp.

## 🚀 Công nghệ sử dụng
- **Giao diện Web**: [Streamlit](https://streamlit.io/)
- **AI Engine**: [Google Gemini (2.5 Flash)](https://aistudio.google.com/)
- **Xử lý Audio**: `pydub`
- **Ngôn ngữ**: Python 3.x

## ⚙️ Hướng dẫn cài đặt

### 1. Yêu cầu hệ thống (Prerequisites)
- Đã cài đặt **Python 3.8+**.
- Đã cài đặt **FFmpeg** trên máy (Bắt buộc phải có FFmpeg để thư viện `pydub` chia tách file âm thanh).

### 2. Cài đặt dự án
Clone kho lưu trữ này về máy:
```bash
git clone https://github.com/tranducthien2701/meeting-summarizer.git
cd meeting-summarizer
```

Tạo và kích hoạt môi trường ảo (Virtual Environment):
```bash
# Trên Windows
python -m venv venv
venv\Scripts\activate

# Trên macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

Cài đặt các gói thư viện phụ thuộc:
```bash
pip install -r requirements.txt
```

### 3. Cấu hình Biến môi trường (API Key)
Tạo một file `.env` ở thư mục gốc của dự án và thêm key Gemini của bạn vào:
```env
GEMINI_API_KEY=your_google_gemini_api_key_here
```

## ▶️ Hướng dẫn sử dụng
Đảm bảo bạn đang ở môi trường ảo `venv`. Sau đó, gõ lệnh sau để mở giao diện Web gốc:
```bash
streamlit run app.py
```
Hệ thống sẽ chạy và mở một tab trên trình duyệt web ở địa chỉ `http://localhost:8501`. Việc của bạn chỉ là Upload audio và chờ AI nhận diện.

## 📂 Tổng quan mã nguồn
```text
meeting-summarizer/
├── app.py                  # File chính khởi chạy giao diện Web (Streamlit)
├── utils/                  # Chức năng AI và logic 
│   ├── audio_utils.py      # Xử lý cắt/tách âm thanh (pydub)
│   ├── transcriber.py      # Gọi Google Gemini xử lý Audio -> Text
│   └── summarizer.py       # Gọi Google Gemini tóm tắt & xuất Action Items
├── .env                    # Biến môi trường chứa GEMINI_API_KEY
├── .gitignore              # Chặn các file rác đẩy lên GitHub
└── requirements.txt        # Danh sách thư viện Python
```
