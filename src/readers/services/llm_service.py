from src.utils.common_utils import get_openai_llm_model, get_ollama_llm_model
from src.utils.qaenum.model_type import LLMTypes


class LLMModelService:
    def __init__(self, llm_type: LLMTypes = LLMTypes.OPENAI):
        """Initialize the model service with a default or specified LLM type."""
        self.llm_type = llm_type

    def get_llm_type(self):
        """Return the currently selected LLM type."""
        return self.llm_type

    def get_default_llm_model_name(self):
        """Fetch the default LLM model name based on the selected LLM type."""
        if self.llm_type not in LLMTypes:
            raise ValueError("Invalid LLM type.")
        return self.llm_type.value  # Fetch the value of the enum as the default model name

    def get_llm_model(self, model_name: str = None, llm_type: LLMTypes = None):
        """Fetch the LLM model based on the type and model name."""
        llm_type = llm_type or self.llm_type
        model_name = model_name or llm_type.value

        # Ensure model_name is a string, not a tuple
        if isinstance(model_name, tuple):
            model_name = model_name[0]  # Extract the first element if it's a tuple

        print(f"Getting LLM model: {model_name} of type: {llm_type}")

        # Map LLM types to their corresponding functions
        llm_function_map = {
            LLMTypes.OPENAI: get_openai_llm_model,
            LLMTypes.OLLAMA: get_ollama_llm_model,
        }

        llm_function = llm_function_map.get(llm_type)

        if not llm_function:
            raise ValueError("Invalid LLM type.")

        return llm_function(model_name)
