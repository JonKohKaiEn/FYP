import requests
import time
import json
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.rate_limiters import InMemoryRateLimiter


class NalaGPTWrapper:
    """
    Wrapper for NALA API Gemini endpoint to adapt it to LangChain model interface.
    """

    def __init__(self, api_key: str, model: str = "gpt-5", reasoning_effort: str = "low") -> None:
        self.api_key = api_key
        self.model = model
        self.reasoning_effort = reasoning_effort
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
            <model>{self.model}</model>
            <system_prompt>{safe_system}</system_prompt>
            <hyperparams>
                <reasoning_effort>{self.reasoning_effort}</reasoning_effort>
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
                    # json_expr = parse("$..text")
                    # return json_expr.find(response_json)
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


class GeminiWrapper:
    """
    Wrapper for Google Gemini API using langchain-google-genai.
    """

    def __init__(
        self,
        api_key: str,
        model: str = "gemini-3.1-flash-lite-preview",
        thinking_level: str = "high",
        requests_per_minute: int = 15,
    ) -> None:
        self.api_key = api_key
        self.model = model
        self.llm = ChatGoogleGenerativeAI(
            model=self.model,
            api_key=self.api_key,
            max_retries=5,
            thinking_level=thinking_level,
            rate_limiter=InMemoryRateLimiter(
                requests_per_second=requests_per_minute / 60.0,
                check_every_n_seconds=0.5,
                max_bucket_size=requests_per_minute,
            ),
        )

    def invoke(self, system_prompt: str, user_text: str):
        """
        Sends a request to the Gemini API with a system prompt and user text.
        Returns the generated text, or None on failure.
        """
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_text),
        ]

        try:
            response = self.llm.invoke(messages)

            if response.content:
                # response.content can be a str or a list of content blocks
                content = response.content
                if isinstance(content, list):
                    content = "".join(
                        block.get("text", "") if isinstance(block, dict) else str(block)
                        for block in content
                    )
                return content

            print("  [API Warning] Empty response.")
            return None

        except Exception as e:
            print(f"  [API Error] {e}")
            return None
