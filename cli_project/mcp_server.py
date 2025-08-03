from pydantic import Field
from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts import base

mcp = FastMCP("DocumentMCP", log_level="ERROR")


docs = {
    "deposition.md": "This deposition covers the testimony of Angela Smith, P.E.",
    "report.pdf": "The report details the state of a 20m condenser tower.",
    "financials.docx": "These financials outline the project's budget and expenditures.",
    "outlook.pdf": "This document presents the projected future performance of the system.",
    "plan.md": "The plan outlines the steps for the project's implementation.",
    "spec.txt": "These specifications define the technical requirements for the equipment.",
}

# TODO: Write a tool to read a doc

@mcp.tool(
    name="read_doc_contents",
    description="Read the contents of a document and return it as a string."
)
def read_document(
    doc_id: str = Field(description="Id of the document to read")
):
    if doc_id not in docs:
        return f"Document with id '{doc_id}' not found."
    
    content = docs[doc_id]
    return content

# TODO: Write a tool to edit a doc
@mcp.tool(
    name="edit_document",
    description="Edit a document by replacing a string in the document's content with a new string."
)
def edit_document(
    doc_id: str = Field(description="Id of the document that will be edited"),
    old_str: str = Field(description="The text to replace. Must match exactly in the document"),
    new_str: str = Field(description="The new text to insert in the place of the old text in the document")
):
    if doc_id not in docs:
        return f"Document with id '{doc_id}' not found."

    return docs[doc_id].replace(old_str, new_str)


# TODO: Write a resource to return all doc id's
@mcp.resource(
    "docs://documents",
    mime_type="application/json",
)
def list_docs() -> list[str]:
    """
    List all document IDs available in the system.
    """
    return list(docs.keys())


# TODO: Write a resource to return the contents of a particular doc
@mcp.resource(
    "docs://documents/{doc_id}",
    mime_type="text/plain",
)
def get_doc(doc_id: str) -> str:
    """
    Get the contents of a specific document by its ID.
    """
    return docs.get(doc_id, "Document not found.")

# TODO: Write a prompt to rewrite a doc in markdown format

@mcp.prompt(
    name="format",
    description="Rewrite the contents of the document in Markdown format."
)
def format_document(
    doc_id: str = Field(description="Id of the document to format")
)-> list[base.Message]:
    # Make sure to format the string with the actual doc_id
    prompt = f"""
    Your task is to reformat a document with markdown syntax. Respond with exactly ONE markdown-formatted version of the document.
    
    The document to format is: <document_id> {doc_id} <document_id>

    
    Here is the content for each document:
    - report.pdf: "The report details the state of a 20m condenser tower."
    - deposition.md: "This deposition covers the testimony of Angela Smith, P.E."
    - financials.docx: "These financials outline the project's budget and expenditures."
    - outlook.pdf: "This document presents the projected future performance of the system."
    - plan.md: "The plan outlines the steps for the project's implementation."
    - spec.txt: "These specifications define the technical requirements for the equipment."
    
    Instructions:
    1. Find the content for <document_id> {doc_id} <document_id> in the list above
    2. Apply markdown formatting (headers, bold, italics, lists, etc.) to enhance readability
    3. Return ONLY the formatted content - do not repeat the instructions or explain what you did
    4. Do NOT place the content in a code block or use markdown fences (```)
    
    Format the document directly without mentioning tools or showing your work.
    """
    print(base.UserMessage(prompt))
    
    return [
        base.UserMessage(prompt)
    ]

# TODO: Write a prompt to summarize a doc


if __name__ == "__main__":
    mcp.run(transport="stdio")
