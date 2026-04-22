import google.generativeai as genai

def summarize_meeting(transcript, api_key):
    """Dùng Gemini 1.5 Flash để tóm tắt và trích xuất Action Items"""
    
    # Cấu hình API Key cho Gemini
    genai.configure(api_key=api_key)
    
    # Khởi tạo model. Khuyên dùng bản flash cho project này vì nó nhanh và rẻ/miễn phí
    model = genai.GenerativeModel('gemini-2.5-flash')

    prompt = f"""
    Bạn là một thư ký điều hành xuất sắc. Dựa vào đoạn văn bản cuộc họp do hệ thống nhận diện giọng nói cung cấp, hãy thực hiện 3 nhiệm vụ:
    1. Tóm tắt nội dung cốt lõi của cuộc họp trong 3-5 câu.
    2. Liệt kê các quyết định quan trọng đã được thống nhất.
    3. Tạo một bảng danh sách các công việc cần làm (Action Items) kèm theo người phụ trách (nếu có nhắc đến).
    
    Hãy định dạng kết quả thật chuyên nghiệp, dễ đọc bằng Markdown (sử dụng in đậm, bullet point, bảng).

    Đây là bản ghi âm cuộc họp:
    ---
    {transcript}
    ---
    """

    import time
    # Gọi Gemini tạo kết quả với cơ chế thử lại nếu dính Rate Limit
    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            if "429" in str(e) and attempt < max_retries - 1:
                print(f"Đạt giới hạn gọi API bên Summarizer, bộ lọc đang nghỉ 20s... (Lần thử {attempt + 1}/{max_retries})")
                time.sleep(20)
            else:
                raise e
    
    return "Lỗi: Không thể tóm tắt do vượt quá giới hạn API."