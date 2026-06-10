from typing import Dict

class PromptEngineer:
    """Builds generation prompts from dynamic user trend/style input."""

    def build_prompt(self, target_prompt: str) -> Dict[str, str]:
        """Create positive and negative prompts based on dynamic user input from API."""
        
        # 1. Xử lý Input từ User (Được truyền vào qua biến target_prompt từ API)
        # Ép kiểu string, cắt khoảng trắng thừa và giới hạn 600 ký tự để tránh lỗi tràn VRAM
        sanitized_input = " ".join(str(target_prompt).split())[:600]
        
        # Nếu API truyền vào rỗng (User không nhập gì), gán một giá trị fallback an toàn
        if not sanitized_input:
            sanitized_input = "standard fashion garment, basic design"

        # 2. Base Quality Boosters (Từ khóa kiểm soát chất lượng đồ họa)
        # Bắt buộc phải giữ lại phần này. Nó không ép phong cách, mà ép con AI phải vẽ NÉT và CHÂN THỰC
        base_quality_prompt = (
            "high-end fashion product photography, sharp tailoring, realistic fabric texture, "
            "studio lighting, detailed garment construction, clean background, 8k resolution, highly detailed"
        )

        # 3. Negative Prompt (Từ khóa chống lỗi)
        # Dặn con AI tuyệt đối không được vẽ ra những thứ này
        negative_prompt = (
            "low quality, blurry, distorted garment, messy seams, bad anatomy, extra limbs, "
            "text, watermark, logo artifacts, cropped garment, duplicate clothing, cheap fabric, worst quality"
        )

        # 4. Trộn Data: Nối cái User muốn + Cấu hình ép chất lượng ảnh
        final_prompt = f"{sanitized_input}, {base_quality_prompt}"

        return {
            "prompt": final_prompt,
            "negative_prompt": negative_prompt,
        }