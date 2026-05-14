from src.utils.preprocess_string import preprocess_string
import logging

logging.basicConfig(level=logging.INFO)

SIMPLE_LAYER = [
"show",
"list",
"display",
"get",
"open",
"find",
"check",
"view",
"retrieve",
"look up",
"see",
"tell",
"give",
"print",
"download",
"upload",
"submit",
"send",
"add",
"remove",
"delete",
"update",
"edit",
"change",
"set",
"mark",
"record",
"save",
"load",
"start",
"stop",
"run",
"execute",
"summarize"
]

COMPLEX_LAYER = [
"explain",
"describe",
"clarify",
"teach",
"help",
"guide",
"walk through",
"analyze",
"compare",
"contrast",
"evaluate",
"assess",
"interpret",
"derive",
"solve",
"reason",
"justify",
"recommend",
"suggest",
"advise",
"plan",
"organize",
"outline",
"prioritize",
"design",
"generate",
"create",
"compose",
"brainstorm",
"prepare",
"study",
"review"
]


def classify_query(query: str) -> str:
    query = preprocess_string(query)
    query = query.split(" ")
    for word in query:
        logging.info(f"Classifying query: checking word '{word}'...")
        if word in SIMPLE_LAYER:
            return "simple"
        elif word in COMPLEX_LAYER:
            return "complex"
        
    
    return "unknown"