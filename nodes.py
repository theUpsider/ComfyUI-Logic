COMPARE_FUNCTIONS = {
    "==": lambda a, b: a == b,
    "!=": lambda a, b: a != b,
    "<": lambda a, b: a < b,
    ">": lambda a, b: a > b,
    "<=": lambda a, b: a <= b,
    ">=": lambda a, b: a >= b,
}


class Int:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {"value": ("INT", {"default": 0})},
        }

    RETURN_TYPES = ("INT",)

    RETURN_NAMES = ("INT",)

    FUNCTION = "execute"

    CATEGORY = "Logic"

    def execute(self, value):
        return value


class Compare:
    """
    This nodes compares the two inputs and outputs the result of the comparison.
    """

    @classmethod
    def INPUT_TYPES(s):
        """
        Comparison node takes two inputs, a and b, and compares them.
        """
        return {
            "required": {
                "a": (),
                "b": (),
                "comparison": (list(COMPARE_FUNCTIONS.keys()), {"default": "=="}),
            },
        }

    RETURN_TYPES = ("BOOLEAN",)

    RETURN_NAMES = "BOOLEAN"

    FUNCTION = "compare"

    CATEGORY = "Logic"

    def compare(self, a, b, comparison):
        """
        Compare two inputs and return the result of the comparison.

        Args:
            a (UNKNOWN): The first input.
            b (UNKNOWN): The second input.
            comparison (STRING): The comparison to perform. Can be one of "==", "!=", "<", ">", "<=", ">=".

        Returns:
            : The result of the comparison.
        """
        return COMPARE_FUNCTIONS[comparison](a, b)


class DebugPrint:

    """
    This node prints the input to the console.
    """

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        class InputTypeProxy(str):
            def __eq__(self, other):
                return True

            def __ne__(self, other):
                return False

        """
        Takes in any input.

        """
        return {"required": {"ANY": (InputTypeProxy("*"),)}}

    RETURN_TYPES = ()

    OUTPUT_NODE = True

    FUNCTION = "execute"

    CATEGORY = "Logic"

    def execute(self, ANY):
        print(ANY)
        return {}


# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "Compare": Compare,
    "Int": Int,
    "DebugPrint": DebugPrint,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "Compare": "Compare",
    "Int": "Int",
    "DebugPrint": "DebugPrint",
}
