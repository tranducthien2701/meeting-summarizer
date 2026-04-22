import streamlit as st
import os
from dotenv import load_dotenv
from utils.audio_utils import process_audio
from utils.transcriber import transcribe_audio
from utils.summarizer import summarize_meeting

# Load biến môi trường từ file .env
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Cấu hình trang UI
st.set_page_config(page_title="AI Meeting Summarizer", page_icon="🎙️", layout="wide")

st.title("🎙️ AI Meeting Summarizer & Action Item Extractor")
st.markdown("Dự án cá nhân hỗ trợ tự động hóa việc viết biên bản cuộc họp. Upload file audio, AI sẽ làm phần còn lại!")

# Khung nhập API Key dự phòng (Nếu nhà tuyển dụng muốn dùng Key của họ)
if not GEMINI_API_KEY:
    GEMINI_API_KEY = st.sidebar.text_input("Nhập GEMINI API Key của bạn để trải nghiệm:", type="password")
    if not GEMINI_API_KEY:
        st.warning("⚠️ Vui lòng cấu hình API Key trong file .env hoặc nhập ở thanh bên trái để sử dụng.")
        st.stop()

# Khu vực Upload file
uploaded_file = st.file_uploader("Tải lên file âm thanh (Hỗ trợ: mp3, wav, m4a)", type=["mp3", "wav", "m4a"])

if uploaded_file is not None:
    if st.button("🚀 Bắt đầu Phân tích", type="primary"):
        
        # Tạo thanh trạng thái để UI chuyên nghiệp hơn
        with st.status("AI đang xử lý dữ liệu cuộc họp...", expanded=True) as status:
            try:
                st.write("⏳ 1. Đang kiểm tra và xử lý file âm thanh...")
                chunk_paths = process_audio(uploaded_file)

                st.write("🎙️ 2. Đang nhận diện giọng nói thành văn bản (Gemini AI)...")
                transcript = transcribe_audio(chunk_paths, GEMINI_API_KEY)

                st.write("🧠 3. Đang phân tích ngữ nghĩa và trích xuất công việc (Gemini AI)...")
                summary = summarize_meeting(transcript, GEMINI_API_KEY) # Truyền Key của Gemini vào đây

                status.update(label="Tuyệt vời! Đã hoàn tất phân tích.", state="complete", expanded=False)

                # Hiển thị kết quả chia thành 2 Tabs
                tab1, tab2 = st.tabs(["📋 Tóm tắt & Quyết định", "📝 Toàn bộ Bản dịch (Transcript)"])

                with tab1:
                    st.markdown(summary)

                with tab2:
                    st.text_area("Văn bản thô (Có thể copy):", value=transcript, height=400)

            except Exception as e:
                status.update(label="Đã xảy ra lỗi hệ thống!", state="error")
                st.error(f"Chi tiết lỗi: {e}")