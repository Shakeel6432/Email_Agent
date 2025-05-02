import google.generativeai as genai

# Gemini API Key
genai.configure(api_key="AIzaSyABgbNzZNeDO_Kv50aISnBf-lbZWPRewqM")

# Model selection
model = genai.GenerativeModel('gemini-1.5-pro')  # You can change the version if needed

def generate_reply(client_reply):
    try:
        prompt = f"""
        You are a professional B2B agent. A client sent this email:

        "{client_reply}"

        Write a very polite and professional email response. Also, suggest scheduling a meeting to discuss further details.
        """

        response = model.generate_content(prompt)
        reply_content = response.text
        return reply_content

    except Exception as e:
        print(f"Error generating reply: {e}")
        return "Thank you for your response. I'd love to schedule a meeting to discuss further."
