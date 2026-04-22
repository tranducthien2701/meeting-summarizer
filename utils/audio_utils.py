import os
import tempfile
from pydub import AudioSegment

def process_audio(uploaded_file):
    """Lưu file tạm và cắt nhỏ nếu dung lượng > 24MB"""
    # Tạo thư mục tạm để lưu file
    temp_dir = tempfile.mkdtemp()
    temp_file_path = os.path.join(temp_dir, uploaded_file.name)

    # Lưu file từ Streamlit xuống ổ cứng
    with open(temp_file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Kiểm tra dung lượng (giới hạn 24MB để an toàn)
    file_size = os.path.getsize(temp_file_path)
    chunk_paths = []
    MAX_SIZE = 24 * 1024 * 1024 # 24 MB

    if file_size > MAX_SIZE:
        audio = AudioSegment.from_file(temp_file_path)
        chunk_length_ms = 10 * 60 * 1000 # Cắt mỗi đoạn 10 phút
        chunks = [audio[i:i + chunk_length_ms] for i in range(0, len(audio), chunk_length_ms)]

        for i, chunk in enumerate(chunks):
            chunk_path = os.path.join(temp_dir, f"chunk_{i}.mp3")
            chunk.export(chunk_path, format="mp3")
            chunk_paths.append(chunk_path)
    else:
        chunk_paths.append(temp_file_path)

    return chunk_paths