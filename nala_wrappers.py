import requests
import time
import json


class NalaGeminiWrapper:
    """
    Wrapper for NALA API Gemini endpoint to adapt it to LangChain model interface.
    """

    def __init__(self, api_key: str, model: str = "gemini-3-pro-preview"):
        self.api_key = api_key
        self.base_url = "https://nala.ntu.edu.sg/api/llm/"
        self.model = model
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/xml",
        }

    def invoke(self, system_prompt: str, user_text: str, max_retries: int = 5):
        """
        Constructs the XML payload with text.
        """
        # Escape XML special characters in text
        safe_user_text: str = (
            user_text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        )
        safe_system: str = (
            system_prompt.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
        )

        # Build the Prompt Content
        full_prompt = safe_user_text

        xml_payload = f"""
        <llm_request>
            <model>{self.model}</model>
            <system_prompt>{safe_system}</system_prompt>
            <hyperparameters>
                <temperature>0</temperature>
                <top_k>5</top_k>
            </hyperparameters>
            <user_prompt>{full_prompt}</user_prompt>
        </llm_request>
        """

        for attempt in range(max_retries):
            try:
                # 60s timeout for large image uploads
                response = requests.post(
                    self.base_url, headers=self.headers, data=xml_payload, timeout=60
                )

                # Check for success
                if response.status_code == 200:
                    return response.text

                # Check specifically for 502 Bad Gateway (or 503 Service Unavailable)
                elif response.status_code in [502, 503, 504]:
                    wait_time = 2 ** (attempt + 1)  # Exponential Backoff: 2s, 4s, 8s
                    print(
                        f"  [API Warning] {response.status_code} Server Error on attempt {attempt + 1}. Retrying in {wait_time}s..."
                    )
                    time.sleep(wait_time)
                    continue

                # If it's a client error (4xx), do not retry. Raise immediately.
                else:
                    print(
                        f"  [API Error] Status {response.status_code}: {response.text}"
                    )
                    response.raise_for_status()

            except requests.exceptions.RequestException as e:
                # Handle network-level errors (e.g., connection reset)
                print(f"  [Network Error] Attempt {attempt + 1} failed: {e}")
                if attempt < max_retries - 1:
                    time.sleep(2)
                else:
                    return None

        print("  [API Error] Max retries exceeded.")
        return None


class NalaGPTWrapper:
    """
    Wrapper for NALA API Gemini endpoint to adapt it to LangChain model interface.
    """

    def __init__(self, api_key: str, model: str = "gpt-5") -> None:
        self.api_key = api_key
        self.model = model
        self.base_url = "https://nala.ntu.edu.sg/api/llm/"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/xml",
        }

    def invoke(self, system_prompt: str, user_text: str, max_retries: int = 5):
        """
        Constructs the XML payload with text.
        """
        # Escape XML special characters in text
        safe_user_text: str = (
            user_text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        )
        safe_system: str = (
            system_prompt.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
        )

        xml_payload = f"""
        <llm_request>
            <model>gpt-5</model>
            <system_prompt>{safe_system}</system_prompt>
            <hyperparams>
                <reasoning_effort>low</reasoning_effort>
                <verbosity>low</verbosity>
            </hyperparams>
            <user_prompt>{safe_user_text}</user_prompt>
        </llm_request>
        """

        for attempt in range(max_retries):
            try:
                # 60s timeout for large image uploads
                response = requests.post(
                    self.base_url, headers=self.headers, data=xml_payload, timeout=60
                )

                # Check for success
                if response.status_code == 200:
                    response_json = json.loads(response.text)
                    return response_json["raw"]["output"][1]["content"][0]["text"]
                # Check specifically for 502 Bad Gateway (or 503 Service Unavailable)
                elif response.status_code in [502, 503, 504]:
                    wait_time = 2 ** (attempt + 1)  # Exponential Backoff: 2s, 4s, 8s
                    print(
                        f"  [API Warning] {response.status_code} Server Error on attempt {attempt + 1}. Retrying in {wait_time}s..."
                    )
                    time.sleep(wait_time)
                    continue

                # If it's a client error (4xx), do not retry. Raise immediately.
                else:
                    print(
                        f"  [API Error] Status {response.status_code}: {response.text}"
                    )
                    response.raise_for_status()

            except requests.exceptions.RequestException as e:
                # Handle network-level errors (e.g., connection reset)
                print(f"  [Network Error] Attempt {attempt + 1} failed: {e}")
                if attempt < max_retries - 1:
                    time.sleep(2)
                else:
                    return None

        print("  [API Error] Max retries exceeded.")
        return None
