import google.generativeai as genai
import time

def transcribe_audio(chunk_paths, api_key):
    """Chuyển đổi từng đoạn audio thành text và ghép lại bằng Gemini 1.5 Flash"""
    genai.configure(api_key=api_key)
    full_transcript = ""
    
    # Sử dụng model Gemini 2.5 Flash hỗ trợ đầu vào âm thanh
    model = genai.GenerativeModel('gemini-2.5-flash')

    for chunk_path in chunk_paths:
        # Tải file âm thanh lên server của Gemini
        audio_file = genai.upload_file(path=chunk_path)
        
        # Đợi file xử lý xong trên server
        while audio_file.state.name == "PROCESSING":
            time.sleep(2)
            audio_file = genai.get_file(audio_file.name)
            
        if audio_file.state.name == "FAILED":
            continue
            
        # Yêu cầu chuyển đổi giọng nói thành văn bản
        prompt = "Hãy chuyển đổi nội dung âm thanh này thành văn bản chính xác nhất. Không cần thêm bất kỳ lời bình luận hay giải thích nào."
        response = model.generate_content([prompt, audio_file])
        
        if response.text:
            full_transcript += response.text + " "
            
        # Xóa file tạm trên server
        genai.delete_file(audio_file.name)

    return full_transcript.strip()