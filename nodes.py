import nodes

COMPARE_FUNCTIONS = {
    "a == b": lambda a, b: a == b,
    "a != b": lambda a, b: a != b,
    "a < b": lambda a, b: a < b,
    "a > b": lambda a, b: a > b,
    "a <= b": lambda a, b: a <= b,
    "a >= b": lambda a, b: a >= b,
}


class AlwaysEqualProxy(str):
    def __eq__(self, _):
        return True

    def __ne__(self, _):
        return False


class String:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {"value": ("STRING", {"default": "", "multiline": True})},
        }

    RETURN_TYPES = ("STRING",)

    RETURN_NAMES = ("STRING",)

    FUNCTION = "execute"

    CATEGORY = "Logic"

    def execute(self, value):
        return (value,)


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
        return (value,)


class Float:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {"value": ("FLOAT", {"default": 0, "step": 0.01})},
        }

    RETURN_TYPES = ("FLOAT",)

    RETURN_NAMES = ("FLOAT",)

    FUNCTION = "execute"

    CATEGORY = "Logic"

    def execute(self, value):
        return (value,)


class Bool:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {"value": ("BOOLEAN", {"default": False})},
        }

    RETURN_TYPES = ("BOOLEAN",)

    RETURN_NAMES = ("BOOLEAN",)

    FUNCTION = "execute"

    CATEGORY = "Logic"

    def execute(self, value):
        return (value,)


class Compare:
    """
    This nodes compares the two inputs and outputs the result of the comparison.
    """

    @classmethod
    def INPUT_TYPES(s):
        """
        Comparison node takes two inputs, a and b, and compares them.
        """
        s.compare_functions = list(COMPARE_FUNCTIONS.keys())
        return {
            "required": {
                "a": (AlwaysEqualProxy("*"), {"default": 0}),
                "b": (AlwaysEqualProxy("*"), {"default": 0}),
                "comparison": (s.compare_functions, {"default": "a == b"}),
            },
        }

    RETURN_TYPES = ("BOOLEAN",)

    RETURN_NAMES = ("BOOLEAN",)

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
        return (COMPARE_FUNCTIONS[comparison](a, b),)


class CompareInt:
    """
    This node compares two integer inputs and outputs the result of the comparison.
    """

    @classmethod
    def INPUT_TYPES(cls):
        """
        Comparison node specifically for integer inputs.
        """
        cls.compare_functions = list(COMPARE_FUNCTIONS.keys())
        return {
            "required": {
                "a": (Int, {"default": 0}),
                "b": (Int, {"default": 0}),
                "comparison": (cls.compare_functions, {"default": "a == b"}),
            },
        }

    RETURN_TYPES = ("BOOLEAN",)

    RETURN_NAMES = ("BOOLEAN",)

    FUNCTION = "compare"

    CATEGORY = "Logic"

    def compare(self, a, b, comparison):
        """
        Compare two integer inputs and return the result of the comparison.

        Args:
            a (int): The first integer input.
            b (int): The second integer input.
            comparison (str): The comparison operation to perform. 
                              Can be one of "a == b", "a != b", "a < b", "a > b", "a <= b", "a >= b".

        Returns:
            tuple: A tuple containing the result of the comparison as a boolean.
        """
        return (COMPARE_FUNCTIONS[comparison](a, b),)


class IfExecute:
    """
    This node executes IF_TRUE if ANY is True, otherwise it executes IF_FALSE.

    ANY can be any input, IF_TRUE and IF_FALSE can be any output.
    """

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "ANY": (AlwaysEqualProxy("*"),),
                "IF_TRUE": (AlwaysEqualProxy("*"),),
                "IF_FALSE": (AlwaysEqualProxy("*"),),
            },
        }

    RETURN_TYPES = (AlwaysEqualProxy("*"),)

    OUTPUT_TOOLTIPS = (
        "Based on the value of ANY, either IF_TRUE or IF_FALSE will be returned.",
    )

    RETURN_NAMES = ("?",)

    FUNCTION = "return_based_on_bool"

    CATEGORY = "Logic"

    def return_based_on_bool(self, ANY, IF_TRUE, IF_FALSE):
        return (IF_TRUE if ANY else IF_FALSE,)


class IfExecuteNode:
    """
    This node lets you choose from all nodes and execute the selected one when ANY is True.
    """

    @classmethod
    def INPUT_TYPES(cls):
        cls.node_names = list(nodes.NODE_CLASS_MAPPINGS.keys())
        return {
            "required": {
                "ANY": (AlwaysEqualProxy("*"),),
                "NODE_TRUE": (cls.node_names, {"default": cls.node_names[0]}),
                "NODE_FALSE": (cls.node_names, {"default": cls.node_names[0]}),
            },
        }

    RETURN_TYPES = ()

    OUTPUT_NODE = True

    CATEGORY = "Logic"

    FUNCTION = "execute"

    def execute(self, ANY, NODE_TRUE, NODE_FALSE):
        if ANY:
            return self.execute_node(NODE_TRUE)
        else:
            return self.execute_node(NODE_FALSE)

    def execute_node(self, node_name):
        node = nodes.NODE_CLASS_MAPPINGS[node_name]()
        return node.execute()


class DebugPrint:
    """
    This node prints the input to the console.
    """

    @classmethod
    def INPUT_TYPES(s):
        """
        Takes in any input.

        """
        return {"required": {"ANY": (AlwaysEqualProxy({}),)}}

    RETURN_TYPES = ()

    OUTPUT_NODE = True

    FUNCTION = "log_input"

    CATEGORY = "Logic"

    def log_input(self, ANY):
        print(ANY)
        return {}


# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "Compare-🔬": Compare,
    "Int-🔬": Int,
    "Float-🔬": Float,
    "Bool-🔬": Bool,
    "String-🔬": String,
    "If ANY return A else B-🔬": IfExecute,
    "DebugPrint-🔬": DebugPrint,
    # "If ANY execute A else B-🔬": IfExecuteNode,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "Compare-🔬": "Compare",
    "Int-🔬": "Int",
    "Float-🔬": "Float",
    "Bool-🔬": "Bool",
    "String-🔬": "String",
    "If ANY return A else B-🔬": "If ANY return A else B",
    "DebugPrint-🔬": "DebugPrint",
    # "If ANY execute A else B-🔬": "If ANY execute A else B",
}


print("\033[94mtheUpsiders Logic Nodes: \033[92mLoaded\033[0m")
